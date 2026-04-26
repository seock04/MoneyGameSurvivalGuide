---
name: moneygame-completion-auditor
description: MoneyGameSurvivalGuide 책 원고의 출간 전 완성도를 100점 기준으로 평가하고, 99%를 넘을 때까지 리뷰-수정-재평가 루프를 반복하기 위한 기준과 리포트를 만들 때 사용한다. 전체 원고 품질, 장별 구조, 사실/투자 안전성, 독자 경험, 표시 품질, 이미지/소스/README 정합성을 통합 점검한다.
---

# MoneyGame Completion Auditor

## Overview

이 스킬은 『부의 게임, 대충 뛰어들어 끝까지 살아남기』 원고가 출간 가능한 수준인지 정량/정성으로 평가한다.

목표:
- 책 전체 완성도를 100점 기준으로 산출한다.
- 99점 이상이 될 때까지 남은 결함을 우선순위화한다.
- "리뷰 -> 수정 -> 검증 -> 재평가" 루프를 작고 반복 가능하게 만든다.

핵심 제약:
- 99점은 "완벽"이 아니라, 출간을 막는 결함이 없고 독자 경험상 남은 문제의 영향이 매우 낮은 상태다.
- 점수만 올리기 위해 원고를 과도하게 늘리지 않는다.
- 투자 성과 보장, 공포 마케팅, 특정 상품 추천처럼 독자에게 위험한 표현은 점수와 무관하게 하드 게이트로 막는다.
- 대규모 수정 전에는 사용자에게 구조 변화의 이유와 범위를 설명한다.

## Required Inputs

먼저 아래 파일을 읽는다.

- `AGENTS.md`
- `README.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `assets/target_audience.md`
- `status/roadmap.md` (있으면)
- `status/expert_panel_review/`의 최신 overview/titles/장별 리뷰
- `status/fact_check/`의 최신 리포트
- `skills/moneygame-completion-auditor/references/rubric.md`
- `skills/moneygame-completion-auditor/references/templates.md`

## Output Paths

- 완성도 평가 리포트: `status/completion_audit/YYYY-MM-DD_round-N.md`
- 수정 계획: 리포트 안의 `Next Patch Queue`
- 점수 변화 기록: 리포트 안의 `Score History`

## Completion Rule

완성도는 아래 조건을 모두 만족해야 `99%+`로 판정한다.

1. 총점이 99.0점 이상이다.
2. 하드 게이트가 모두 통과 상태다.
3. `Critical` 이슈가 0개다.
4. `High` 이슈가 0개이거나, 사용자와 명시적으로 합의한 보류 사유가 있다.
5. 마지막 수정 이후 영향을 받은 챕터를 다시 읽고 점수를 갱신했다.

## Workflow

1. Scope 설정
   - 기본은 전체 책(`chapters/00_*.md`~`chapters/14_*.md`)이다.
   - 사용자가 특정 챕터만 요청하면 해당 범위만 평가하되, 최종 99% 판정은 전체 책 기준으로만 한다.

2. Baseline Audit
   - 목차/파일 존재/README 링크를 확인한다.
   - 각 챕터의 표준 구조를 확인한다.
   - 이미지, 표, Sources, 질문 섹션, 부록 참조, 마크다운 렌더링 위험을 빠르게 스캔한다.
   - 최신 전문가 패널 리뷰와 팩트체크에서 아직 반영되지 않은 항목을 확인한다.

3. Score
   - `references/rubric.md`의 10개 영역으로 점수를 매긴다.
   - 영역별 점수는 근거 파일과 위치를 함께 적는다.
   - 하드 게이트 위반은 점수와 별도로 기록한다.

4. Patch Queue
   - 이슈를 `Critical`, `High`, `Medium`, `Low`로 나눈다.
   - 한 라운드에서는 가장 영향이 큰 3~7개만 수정 대상으로 삼는다.
   - 수정은 독자 이탈, 사실 오류, 안전성, 렌더링 문제를 우선한다.

5. Update
   - 사용자가 원고 수정까지 요청했거나 현재 요청이 반복 개선이라면, 큐의 항목을 직접 수정한다.
   - 구조 변경, 챕터 추가/삭제, 목차 변경은 사용자 동의 없이 확정하지 않는다.
   - 수정 후 영향 범위를 다시 읽는다.

6. Re-score
   - 수정한 영역만 임시 점수로 올리지 말고 전체 점수에 미치는 영향을 재계산한다.
   - 점수 상승/하락 이유를 `Score History`에 남긴다.
   - 99점 미만이면 다음 라운드 큐를 만든다.

7. Stop Condition
   - `Completion Rule`을 모두 만족하면 최종 리포트에 `READY_FOR_FINAL_HUMAN_REVIEW`를 표시한다.
   - 99점 미만이면 `NEXT_ROUND_REQUIRED`를 표시하고 다음 라운드의 첫 작업을 하나만 지정한다.

## Integration With Existing Skills

- 장별 문학/재무/코칭/심리 패널 판단이 필요하면 `moneygame-expert-panel-review`의 기존 리포트를 우선 참고한다.
- 사실 확인이 필요한 수치/인용/최신 제도는 `moneygame-fact-check` 방식으로 출처를 검증한다.
- 톤이 흔들리는 부분은 `moneygame-tone-review`의 패턴을 참고한다.
- 로드맵이나 파생 콘텐츠 판단은 이 스킬의 범위가 아니다.

## References

- 세부 평가표: `skills/moneygame-completion-auditor/references/rubric.md`
- 리포트 템플릿: `skills/moneygame-completion-auditor/references/templates.md`
