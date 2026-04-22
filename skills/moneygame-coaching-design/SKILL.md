---
name: moneygame-coaching-design
description: MoneyGameSurvivalGuide 책 내용을 기반으로 '세계최고의 재무코치' 페르소나로 재무 코칭(1:1 반구조화 3회, 그룹 3회, 그룹+1:1 하이브리드)을 설계하고, 각 프로그램의 발표자료(슬라이드 아웃라인)와 워크시트를 Additionals/financial_coaching/ 아래에 생성/갱신할 때 사용한다.
---

# MoneyGame Coaching Design

## Overview

이 스킬은 책의 세계관(부의 게임, 자동 사냥, 인벤토리, 생존, 거인의 어깨, 생애 주기, 파이프라인)을 기반으로 코칭 상품을 설계하고, 실행에 필요한 자료(슬라이드/워크시트)를 생성한다.

핵심 제약:
- `Additionals/RULES.md`를 따른다. (책 기반, 독립 주장 금지, `## Sources`에 챕터 링크 필수)
- 단계별로 진행한다. 사용자가 이해/동의하지 않은 내용은 확정해서 넣지 않는다. (`AGENTS.md`)
- 특정 종목/상품 추천, 수익 보장, 매매 타이밍 예언을 하지 않는다.

## Output Locations (fixed)

- 설계(outlines): `Additionals/financial_coaching/outlines/`
- 초안(drafts): `Additionals/financial_coaching/drafts/`
- 확정(final): `Additionals/financial_coaching/final/`
- 슬라이드(아웃라인): `Additionals/financial_coaching/assets/slides/`
- 워크시트: `Additionals/financial_coaching/assets/worksheets/`
- 참고(references): `Additionals/financial_coaching/references/`

## Required Inputs (read first)

- `Additionals/RULES.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `assets/target_audience.md`
- `Additionals/financial_coaching/outlines/persona_world_class_financial_coach.md`
- `Additionals/financial_coaching/outlines/coaching_design_system.md`

## Persona (World-Class Financial Coach)

페르소나 상세는 아래 문서를 기준으로 한다:
- `Additionals/financial_coaching/outlines/persona_world_class_financial_coach.md`

## Coaching Formats (must support)

1. 3회차 1:1 반구조화 코칭
2. 3회차 그룹 코칭
3. 그룹 3회 + 1:1 1회 하이브리드 코칭

## Workflow (Step-by-step)

1. 범위/전제 확인(확정 전)
   - 대상(직장인/자영업/프리랜서), 위험 성향, 투자 경험
   - 코칭 범위(포함/비포함): 세금/보험/부동산/부채/투자 상품 언급 등
   - 성공 지표: 실행률, 불안 감소, 현금흐름 개선 등

2. 프로그램 설계를 먼저 만든다(자료부터 만들지 않는다)
   - 각 포맷별로 `outlines/`에 설계 문서를 만든다.
   - 각 문서에는 최소 2개 이상의 `chapters/*.md` Sources를 연결한다.

3. 슬라이드 아웃라인을 만든다
   - 각 회차별로 "핵심 메시지 1개 + 오해 1개 + 실습 1개"를 기준으로 슬라이드를 구성한다.
   - 슬라이드는 이 repo에서는 Markdown 아웃라인으로 관리한다.

4. 워크시트를 만든다
   - 인벤토리(재무상태/현금흐름), 목표(SMART/북극성), 자동 사냥(자동이체/리밸런싱), 리스크(비상금/레버리지 금지) 중심
   - 개인 정보 수집용이 아니라 "템플릿"과 "예시"로만 만든다.

5. 초안 -> 확정 승격
   - `drafts/`에서 파일을 다듬고, 최종 확정 시 `final/`로 이동한다.

## Templates

필요 시 다음 템플릿을 읽는다:
- `skills/moneygame-coaching-design/references/templates.md`
