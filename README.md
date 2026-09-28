# 🔥 EPOCH_Datathon_5th

이 레포지토리는 데이터 사이언스 연합동아리 **EPOCH 6기** 멤버의 Datathon 결과물을 기록하기 위해 개설되었습니다.
> **진행 기간**: `2026.09.29~2026.10.06`

## Datathon 개요
> **본 Datathon은 동일한 데이터셋을 기반으로 각 팀별로 Feature Engineering, Modeling, Tuning 등을 통해 타겟 변수의 값을 가장 정확하게 예측합니다.**

**예측 대상** — 어떤 YouTube 채널이 **앞으로 성장 국면(Rising)에 들어갈지**
**예측 단위** — `채널 × 기준일` 한 줄마다 확률 하나
**채점 기준일** — `2026-09-01` **하나**입니다

## Dataset
> 본 Datathon에서 사용될 데이터셋은 **EPOCH가 직접 수집한 YouTube 채널 스냅샷 데이터셋**입니다. Steam · IGDB 게임 데이터가 함께 제공됩니다.

### 데이터 정보

| 테이블 | 행 수 | 내용 |
| --- | --- | --- |
| `channels` | 1,871 | 채널 목록 |
| `videos` | 38,411 | 영상 메타 (`duration_sec` · `is_shorts` 포함) |
| `video_snapshots` | 18,051,339 | 영상 시계열 — **매우 큼. 통째로 읽지 마세요** |
| `video_5d_views` | 31,524 | 5일 지표 (`view_5d` · `like_5d` · `comment_5d`) |
| `channel_snapshots` | 77,177 | 채널 시계열 (구독자 · 총조회수) |
| `video_topics` | 14,840 | 영상 주제 |
| `video_games` / `apps` | 1,826 / 47 | Steam 매핑 · 게임 |
| `video_igdb_games` / `igdb_games` | 10,386 / 58 | IGDB 매핑 · 게임 |
| `app_snapshots` / `app_reviews` | 29,262 / 148,157 | Steam 시계열 · 리뷰 |
| `sample_submission.csv` | **849** | 제출 양식 |

**채점 대상은 849행**입니다. 그중 20%인 **170채널**이 Rising(label=1)입니다.
컬럼 상세는 `03_데이터 코드북`을 보세요.

## 제출 가이드라인
> **공통 경로**: `EPOCH_DATATHON_5th/Submission/`

각 팀은 **코드**와 **보드/발표 자료**를 해당 레포지토리에 제출해야 하며, 각 파일 양식은 아래와 같습니다.

**제출은 두 번입니다.** 대회 당일 새벽에 한 번, 화요일 대면 세션에 한 번.

### 1️⃣ 대회 당일 → `Preliminary_Round/`
- **코드**: `Submission/Preliminary_Round/TeamN/5th_datathon_code_팀명.ipynb`
- **발표 자료 (보드)**: `Submission/Preliminary_Round/TeamN/5th_datathon_board_팀명.pdf`
  - 주의: 템플릿으로 제공되는 `pptx` 확장자가 아닌 **`pdf` 확장자**로 제출
  - 템플릿: `5th_datathon_board_팀명.pptx`

### 2️⃣ 대면 세션 → `Final_Round/`
- **코드**: `Submission/Final_Round/TeamN/5th_datathon_code_팀명.ipynb`
- **발표 자료 (PPT)**: `Submission/Final_Round/TeamN/5th_datathon_ppt_팀명.pdf`
  - 주의: 대회 당일과 마찬가지로 **`pdf` 로 변환해서** 제출

> **둘 다 `pdf` 입니다.** 폰트가 깨지거나 표가 밀리는 사고를 막기 위해서입니다.
> 발표는 제출하신 `pdf` 를 그대로 띄웁니다.

> ⚠️ **폴더 이름의 `Preliminary` · `Final` 은 리더보드의 「연습 / 본선」과 다릅니다.**
> 폴더는 **제출 시점**을 가리킵니다 — `Preliminary_Round` = 대회 당일, `Final_Round` = 대면 세션.
> 리더보드의 연습·본선은 **제출 횟수와 정답 구간**을 가르는 별개의 구분입니다.

### 폴더 구조:
```
EPOCH_DATATHON_5th/
├── Submission/
│   ├── Preliminary_Round/
│   │   ├── Team1/
│   │   ├── .../
│   │   └── Team6/
│   └── Final_Round/
│       ├── Team1/
│       ├── .../
│       └── Team6/
└── tools/
    └── validate_submission.py
```

### 🗓️ 제출 일정

- **대회 당일 제출 마감**: `2026-10-04 (일) 05:00:00` → `Preliminary_Round/`
  - 제출 파일: 코드(`ipynb`), 보드(`pdf`)
  - 리더보드 마감과 **같은 시각**입니다. 보드 발표가 바로 이어집니다
- **대면 세션 제출 마감**: `2026-10-06 (화) 세션 시작 전` → `Final_Round/`
  - 제출 파일: 최종 코드(`ipynb`), 발표 자료(`pdf`)

> **마감은 서버 시간 기준입니다.** 여러분 PC의 시계는 인정되지 않습니다.
> 리더보드 상단에 서버 시간이 표시됩니다. **최소 5분 여유를 두세요.**

### 🏁 리더보드

제출물과 **별개**입니다. 예측 CSV는 아래에 올립니다.

| 기간 | 시각 | 횟수 |
| --- | --- | --- |
| 연습 | `09.29 (화) 20:00 ~ 10.03 (토) 00:00` | 하루 3회 |
| 점검 | `10.03 (토) 00:00 ~ 19:00` | 제출 불가 |
| 본선 | `10.03 (토) 19:00 ~ 10.04 (일) 05:00` | 하루 10회 (자정 초기화 · 최대 20회) |

> http://epoch-datathon.duckdns.org
> **연습 점수는 최종에 반영되지 않습니다.** 파이프라인을 미리 맞춰보는 기간입니다.

## 💯 평가 기준

* 리더 보드 - `50%`
* 전문가 평가 - `30%`
* 동료 평가 - `20%` (대회 당일 보드 `10%` · 대면 세션 발표 `10%`)

> **평가지표와 배점 상세는 본선 시작 시점(`10.03 19:00`)에 `05_평가 가이드`로 전면 공개됩니다.**
> 연습 기간에는 공개하지 않습니다.

## ⚠️ 코드 제출 시 주의

- **운영진이 실행해볼 수 있어야 합니다.** 재현이 안 되면 감점입니다
- **절대 경로**(`C:\Users\...`)를 상대 경로로 바꿔주세요
- **랜덤 시드**를 고정해주세요
- **승인받지 않은 외부 데이터**를 쓴 흔적이 있으면 실격입니다 (YouTube 계열은 승인 대상이 아닙니다)
- **배포 데이터는 올리지 마세요.** `.gitignore`로 막혀 있습니다

## 📤 올리는 법

```bash
git clone https://github.com/team-epoch/EPOCH_DATATHON_5th.git
cd EPOCH_DATATHON_5th

# 자기 팀 폴더에만 파일을 넣습니다
git add Submission/Preliminary_Round/Team3
git commit -m "Team3 대회 당일 제출"
git pull --rebase        # 먼저 받아야 충돌이 안 납니다
git push
```

> **`git pull --rebase`를 먼저 하세요.** 여러 팀이 같은 시간에 올리므로 이걸 빼면 `rejected`가 납니다.
> **깃이 막히면 시간을 쓰지 마세요.** 운영진에게 파일을 직접 주시면 됩니다.
> **마감 기준은 파일을 준 시각**이지 깃에 올라간 시각이 아닙니다.

---

*문의: 운영진 **양승빈***
