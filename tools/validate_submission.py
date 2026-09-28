#!/usr/bin/env python3
"""
제출 파일 자가 검증 — EPOCH 6th Datathon

제출 전에 로컬에서 돌려보세요. 여기서 통과하면 서버에서도 통과합니다.
제출 횟수를 아끼는 가장 확실한 방법입니다.

사용법
    python validate_submission.py sample_submission.csv my_submit.csv

종료 코드
    0  통과
    1  거부 (사유 출력)
"""
import sys

try:
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("pandas / numpy 가 필요합니다:  pip install pandas numpy")

EXPECTED_COLS = ["row_id", "prediction"]
MAX_MB = 10

ok_msgs, err_msgs, warn_msgs = [], [], []


def ok(m):   ok_msgs.append(m)
def err(m):  err_msgs.append(m)
def warn(m): warn_msgs.append(m)


def main(sample_path, submit_path):
    import os

    # ── 0. 파일 존재 / 크기 ────────────────────────────────
    for p in (sample_path, submit_path):
        if not os.path.exists(p):
            sys.exit(f"파일을 찾을 수 없습니다: {p}")

    size_mb = os.path.getsize(submit_path) / 1024 / 1024
    if size_mb > MAX_MB:
        err(f"파일이 {size_mb:.1f}MB 로 제한({MAX_MB}MB)을 넘습니다")
    else:
        ok(f"파일 크기 {size_mb:.2f}MB")

    # ── 1. 읽기 ───────────────────────────────────────────
    try:
        sample = pd.read_csv(sample_path)
    except Exception as e:
        sys.exit(f"sample_submission.csv 를 읽지 못했습니다: {e}")
    try:
        sub = pd.read_csv(submit_path)
    except Exception as e:
        sys.exit(f"제출 파일을 읽지 못했습니다: {e}")

    # ── 2. 컬럼 ──────────────────────────────────────────
    cols = list(sub.columns)
    if cols != EXPECTED_COLS:
        err(f"컬럼이 다릅니다\n"
            f"     기대: {EXPECTED_COLS}\n"
            f"     실제: {cols}")
        extra = [c for c in cols if c not in EXPECTED_COLS]
        if any(str(c).lower().startswith("unnamed") for c in extra):
            err("  ↳ 인덱스가 저장된 것 같습니다. to_csv(..., index=False) 를 쓰세요")
        low = {str(c).lower(): c for c in cols}
        for want in EXPECTED_COLS:
            if want not in cols and want in low:
                err(f"  ↳ '{low[want]}' 는 대소문자가 다릅니다. '{want}' 로 바꾸세요")
    else:
        ok("컬럼명 정상")

    if "row_id" not in cols or "prediction" not in cols:
        report()
        return 1

    # ── 3. 행 수 ─────────────────────────────────────────
    if len(sub) != len(sample):
        err(f"행 수가 다릅니다 — 기대 {len(sample):,} / 실제 {len(sub):,}")
    else:
        ok(f"행 수 {len(sub):,}")

    # ── 4. row_id 집합 ───────────────────────────────────
    s_ids, u_ids = set(sample["row_id"]), set(sub["row_id"])
    dup = len(sub) - sub["row_id"].nunique()
    if dup:
        err(f"row_id 중복 {dup}건 — 예시: "
            f"{sub['row_id'][sub['row_id'].duplicated()].head(3).tolist()}")

    missing, unknown = s_ids - u_ids, u_ids - s_ids
    if missing:
        err(f"누락된 row_id {len(missing):,}건 — 예시: {sorted(missing)[:5]}")
    if unknown:
        err(f"존재하지 않는 row_id {len(unknown):,}건 — 예시: {sorted(unknown)[:5]}")
        anyu = sorted(unknown)[0]
        if "_" in str(anyu):
            err(f"  ↳ 날짜 포맷을 확인하세요. 기대 형식 예: "
                f"{sorted(s_ids)[0]}")
    if not missing and not unknown and not dup:
        ok("row_id 집합 일치")

    # ── 5. prediction 값 ─────────────────────────────────
    p = pd.to_numeric(sub["prediction"], errors="coerce")

    n_nonnum = int(p.isna().sum() - sub["prediction"].isna().sum())
    if n_nonnum > 0:
        bad = sub.loc[p.isna() & sub["prediction"].notna(), "prediction"].head(3).tolist()
        err(f"숫자가 아닌 값 {n_nonnum}건 — 예시: {bad}")

    n_nan = int(sub["prediction"].isna().sum())
    if n_nan:
        rows = (sub.index[sub["prediction"].isna()][:5] + 2).tolist()  # +2: 헤더+1based
        err(f"결측(NaN) {n_nan}건 — 파일 기준 행 번호 예시: {rows}")

    n_inf = int(np.isinf(p.fillna(0)).sum())
    if n_inf:
        err(f"무한대(inf) {n_inf}건")

    valid = p.replace([np.inf, -np.inf], np.nan).dropna()
    if len(valid):
        oor = valid[(valid < 0) | (valid > 1)]
        if len(oor):
            rows = (oor.index[:5] + 2).tolist()
            err(f"0~1 범위를 벗어난 값 {len(oor)}건 — 행 {rows}, 값 {oor.head(3).tolist()}")
        else:
            ok(f"값 범위 정상 [{valid.min():.4f}, {valid.max():.4f}]")

        # ── 6. 거부되지는 않지만 점수를 깎는 패턴 ──────────
        uniq = valid.nunique()
        if uniq <= 2:
            warn(f"서로 다른 값이 {uniq}개뿐입니다. "
                 f"predict() 대신 predict_proba(X)[:, 1] 을 쓰셨나요? "
                 f"PR-AUC는 순위를 보므로 이진값이면 점수가 크게 떨어집니다")
        elif uniq < len(valid) * 0.01:
            warn(f"서로 다른 값이 {uniq}개로 매우 적습니다 ({len(valid):,}행 중)")

        if valid.std() < 1e-9:
            warn("모든 값이 사실상 동일합니다. PR-AUC가 기준선(0.20)에 머뭅니다")

        frac_high = float((valid > 0.5).mean())
        if frac_high > 0.6:
            warn(f"예측값의 {frac_high:.0%}가 0.5를 넘습니다. "
                 f"양성 비율은 20% 입니다 — [:, 0] 을 쓰신 게 아닌지 확인하세요")

    return report()


def report():
    print()
    for m in ok_msgs:
        print(f"  \033[32m✓\033[0m {m}")
    for m in warn_msgs:
        print(f"  \033[33m!\033[0m {m}")
    for m in err_msgs:
        print(f"  \033[31m✗\033[0m {m}")
    print()
    if err_msgs:
        print(f"\033[31m거부 — {len(err_msgs)}건을 고쳐주세요\033[0m\n")
        return 1
    if warn_msgs:
        print(f"\033[33m통과 — 다만 경고 {len(warn_msgs)}건을 확인해보세요\033[0m\n")
        return 0
    print("\033[32m통과 — 제출하셔도 됩니다\033[0m\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
