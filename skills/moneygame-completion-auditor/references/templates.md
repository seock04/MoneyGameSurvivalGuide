# Completion Audit Templates

## Report Template

```md
# Completion Audit: <YYYY-MM-DD> Round <N>

## Verdict

- status: NEXT_ROUND_REQUIRED | READY_FOR_FINAL_HUMAN_REVIEW
- total_score: <0-100>
- hard_gates: PASS | FAIL
- critical_count:
- high_count:
- medium_count:
- low_count:

## Scope

- chapters:
- status inputs:
- guides:

## Scorecard

| 영역 | 배점 | 점수 | 근거 |
|---|---:|---:|---|
| 핵심 메시지와 책 구조 | 15 |  |  |
| 독자 여정과 이해 가능성 | 15 |  |  |
| 재무 정확성과 투자 안전성 | 15 |  |  |
| 톤과 심리적 안전성 | 12 |  |  |
| 실행 가능성 | 10 |  |  |
| 출처와 데이터 무결성 | 10 |  |  |
| 표시 품질과 마크다운 렌더링 | 8 |  |  |
| 시각 자료 완성도 | 5 |  |  |
| 파일/링크/메타 정합성 | 5 |  |  |
| 출간 전 polish | 5 |  |  |

## Hard Gate Check

| Gate | Pass/Fail | Evidence |
|---|---|---|
| 보장형 투자 표현 없음 |  |  |
| 직접 상품 추천 없음 |  |  |
| 최신 수치 출처 있음 |  |  |
| 일반 챕터 표준 구조 충족 |  |  |
| 부록 구조 예외 준수 |  |  |
| 렌더링 위험 해결 |  |  |
| README/파일 정합성 |  |  |
| Critical 팩트체크 없음 |  |  |

## Findings

### Critical
- location:
- issue:
- impact:
- fix:

### High
- location:
- issue:
- impact:
- fix:

### Medium
- location:
- issue:
- impact:
- fix:

### Low
- location:
- issue:
- impact:
- fix:

## Next Patch Queue

1. 
2. 
3. 

## Score History

| Round | Score | Change | Reason |
|---:|---:|---:|---|
| <N> |  |  |  |

## Next Round Trigger

- 
```

## Patch Queue Format

```md
### Patch <number>: <title>

- severity:
- files:
- reason:
- expected_score_impact:
- risk:
- validation:
```
