---
name: moneygame-tone-review
description: MoneyGameSurvivalGuide 원고(및 Additionals)가 집필 규칙의 톤&매너(평어체, 게임 메타포, 따뜻하고 대충 합리적인 태도)를 지키는지 점검하고, 자동 탐지 결과와 수동 체크리스트를 status/tone_review/ 아래 리포트로 저장할 때 사용한다.
---

# MoneyGame Tone Review

## Overview

이 스킬은 "이 원고가 내 톤&매너로 쓰였는지"를 단계별로 점검하고 결과를 `status/`에 저장한다.

기준 문서:
- `guides/WRITING_RULES.md` (톤&매너 최상위 기준)
- `guides/DISPLAY_GUIDE.md` (가독성/레이아웃)
- `assets/target_audience.md` (타깃 독자 전제)
- `AGENTS.md` (단계별 진행, 이해 확인 후 반영)
- `Additionals/RULES.md` (`Additionals/` 콘텐츠 출처/범위 규칙)

## What This Skill Produces

- 리포트: `status/tone_review/YYYY-MM-DD.md`

## Workflow (Step-by-step)

1. 범위 확정
   - 기본: `chapters/*.md`
   - 필요 시: 특정 `Additionals/...` 경로 포함(출처 규칙 준수)

2. 자동 탐지로 "의심 지점"을 뽑는다
   - 존댓말/격식체 종결(예: `습니다`, `합니다`, `됩니다`, `입니다`)
   - 명령/요청 어미(예: `세요`, `하십시오` 등)
   - 질문 어미(예: `인가요`, `나요`, `신가요`)는 톤 정책에 따라 "허용/불허"를 별도 표기한다.

3. 수동 체크리스트로 품질 판단을 한다
   - 평어체(서술) 유지 여부
   - 게임 메타포의 일관성/과잉 여부
   - 독자 불안 자극 vs 따뜻하고 합리적인 태도
   - 과도한 단정/공포/확신 어조 여부

4. 결과를 리포트로 저장한다
   - 요약(결론은 보수적으로)
   - 자동 탐지 결과(파일/라인 포함)
   - 사람이 봐야 하는 항목(결정 필요 사항)
   - 다음 액션(가장 작은 1단계)

## Command Snippets

필요 시 `references/patterns.md`를 참고해 `rg`로 자동 탐지를 수행한다.
