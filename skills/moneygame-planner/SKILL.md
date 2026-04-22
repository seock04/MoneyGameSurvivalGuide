---
name: moneygame-planner
description: MoneyGameSurvivalGuide 프로젝트에서 책 원고 상태를 점검하고, 책 기반 파생 콘텐츠(강연/코칭/블로그/마케팅) 로드맵을 단계별로 설계하며 status/roadmap.md와 Additionals 구조에 맞게 산출물을 생성/갱신할 때 사용한다.
---

# MoneyGame Planner

## Overview

이 스킬은 이 저장소의 규칙(집필/가독성/Additionals 출처 규칙)을 지키면서, "책 원고 완료(최우선) -> 대표 상품(강연/코칭 중 1개) -> 나머지 상품 -> 단계별 마케팅 -> 장기 운영/확장"을 하나의 로드맵으로 연결하고 `status/roadmap.md`를 지속적으로 갱신하는 데 사용한다.

핵심 제약:
- 단계별로 진행한다. 사용자가 이해하지 못하거나 동의하지 않은 내용은 확정해서 넣지 않는다.
- `Additionals/` 산출물은 반드시 책 기반이며, `## Sources`에 `chapters/` 링크를 포함한다. (상세: `Additionals/RULES.md`)

## When To Use

- "현재 원고 상태를 점검해줘"처럼 진행 상황을 객관적으로 정리해야 할 때
- "강연(1h/2h/3h), 코칭(패키지), 블로그 100, 마케팅"을 한 계획으로 묶어야 할 때
- `status/roadmap.md`를 업데이트하고 다음 액션을 작게 쪼개야 할 때

## Workflow

1. 기준 문서부터 읽는다:
   - `AGENTS.md`
   - `guides/WRITING_RULES.md`
   - `guides/DISPLAY_GUIDE.md`
   - `assets/target_audience.md`
   - `Additionals/RULES.md`
   - `status/roadmap.md` (있으면)

2. 원고 상태를 최소 비용으로 점검한다:
   - 챕터 파일 존재/구조(요약/일러스트/질문/부록 연결)
   - 자리표시 주석(추후 삽입 예정) 목록
   - 누락된 섹션(예: 레벨업 질문)

3. 로드맵은 DRAFT로 만들고 "결정이 필요한 질문"을 분리한다:
   - 청중, 채널, 코칭 범위처럼 결과를 뒤집는 항목은 먼저 질문으로 올린다.
   - 확인 전에는 보수적으로 가정하고, 가정은 문서에 명시한다.
   - 강연과 코칭 중 무엇을 대표 상품(Flagship)으로 먼저 완성할지도 결정 질문으로 분리한다.

4. 산출물은 저장소 규칙에 맞게 저장한다:
   - 로드맵: `status/roadmap.md`
   - 강연: `Additionals/financial_lectures/...`
   - 코칭: `Additionals/financial_coaching/...`
   - 블로그: `Additionals/blog_posts/...`
   - 마케팅: `Additionals/content_marketing/...`

## Templates

로드맵/산출물 템플릿은 필요 시 `references/`를 읽는다:
- `skills/moneygame-planner/references/templates.md`
