# EPOCH 5th Datathon — 제출 저장소

**최종 코드와 발표 자료를 내는 곳입니다.** 리더보드 제출과는 별개입니다.

> 리더보드(예측 CSV)는 http://epoch-datathon.duckdns.org 에 올립니다.
> **여기는 코드와 발표 자료만** 올립니다. **둘 다 내야 점수의 50%를 받습니다.**

---

## 마감

```
2026. 10. 04. (일) 05:00
```

리더보드 마감과 같은 시각입니다. **04:50 에는 끝내주세요.**

---

## 무엇을 내나

| 무엇 | 형식 | 어디에 |
| --- | --- | --- |
| 최종 코드 | `.ipynb` | `submissions/teamNN/code/` |
| 발표 자료 | `.pptx` 또는 `.pdf` | `submissions/teamNN/slides/` |
| 최종 제출 CSV | `.csv` (선택) | `submissions/teamNN/submission/` |
| 팀 정보 | `README.md` 채우기 | `submissions/teamNN/README.md` |

`teamNN` 은 배정받은 팀 번호입니다 (`team01` ~ `team06`).

---

## 어떻게 내나

### 1. 저장소를 받습니다

```bash
git clone https://github.com/team-epoch/EPOCH_DATATHON_5th.git
cd EPOCH_DATATHON_5th
```

### 2. 자기 팀 폴더에만 파일을 넣습니다

**다른 팀 폴더는 건드리지 마세요.** 충돌이 나면 양쪽 다 밀립니다.

### 3. 커밋하고 올립니다

```bash
git add submissions/team03
git commit -m "team03 최종 제출"
git pull --rebase        # 먼저 받아야 충돌이 안 납니다
git push
```

> **`git pull --rebase` 를 먼저 하세요.** 여러 팀이 같은 시간에 올리므로
> 이걸 빼면 `rejected` 가 납니다. 그때도 같은 명령을 치면 풀립니다.

### 4. 안 되면

**깃이 막히면 시간을 쓰지 마세요.** 운영진에게 파일을 직접 주세요.
**마감 시각 기준은 파일을 준 시각입니다.** 깃에 올라간 시각이 아닙니다.

---

## 폴더 구조

```
EPOCH_DATATHON_5th/
├── README.md               ← 지금 보고 있는 파일
├── .gitignore
├── tools/
│   └── validate_submission.py   ← 제출 CSV 자가 검증
└── submissions/
    ├── README.md           ← 제출 규칙 상세
    ├── _template/          ← 새 팀이 생기면 이걸 복사
    ├── team01/
    ├── team02/
    ├── team03/
    ├── team04/
    ├── team05/
    └── team06/
```

---

## 코드를 낼 때

가이드 `02_제출 가이드` §6 과 같은 내용입니다.

- **운영진이 실행해볼 수 있어야 합니다.** 재현이 안 되면 감점입니다
- **절대 경로를 쓰지 마세요.** `C:\Users\...` → `../data/` 같은 상대 경로로
- **랜덤 시드를 고정하세요**
- **승인받지 않은 외부 데이터**를 쓴 흔적이 있으면 실격입니다
  (YouTube 계열은 승인 대상이 아닙니다)

### 데이터는 올리지 마세요

배포 데이터는 `.gitignore` 로 막혀 있습니다. **용량이 크고 모두가 이미 갖고 있습니다.**
코드가 `../data/videos.csv` 를 읽도록 써주시면 됩니다.

---

## 제출 CSV 자가 검증

리더보드에 올리기 전에 **로컬에서 먼저 확인**하세요. 제출 횟수를 아끼는 가장 확실한 방법입니다.

```bash
python tools/validate_submission.py sample_submission.csv 내제출.csv
```

통과하면 서버에서도 통과합니다.

---

*문의: 운영진 **양승빈***
