---
name: moneygame-planner
description: MoneyGameSurvivalGuide 프로젝트에서 책 원고 상태를 점검하고, 책 기반 파생 콘텐츠(강연/코칭/블로그/마케팅) 로드맵을 단계별로 설계하며 status/roadmap.md와 Additionals 구조에 맞게 산출물을 생성/갱신할 때 사용한다. 강연, 코칭, 블로그로 책 내용을 확장할 때는 cross-format 콘텐츠 구조 기준을 참고해 원고의 핵심 메시지가 각 매체의 형식에 맞게 전달되도록 계획한다.
---

# MoneyGame Planner

## Overview

이 스킬은 이 저장소의 규칙(집필/가독성/Additionals 출처 규칙)을 지키면서, "책 원고 완료(최우선) -> 대표 상품(강연/코칭 중 1개) -> 나머지 상품 -> 단계별 마케팅 -> 장기 운영/확장"을 하나의 로드맵으로 연결하고 `status/roadmap.md`를 지속적으로 갱신하는 데 사용한다.

핵심 제약:
- 단계별로 진행한다. 사용자가 이해하지 못하거나 동의하지 않은 내용은 확정해서 넣지 않는다.
- `Additionals/` 산출물은 반드시 책 기반이며, `## Sources`에 `chapters/` 링크를 포함한다. (상세: `Additionals/RULES.md`)
- 파생 콘텐츠 로드맵은 책 원고를 복제하는 계획이 아니라, 각 매체에 맞게 `핵심 메시지 -> 근거 -> 실행/실습`으로 재구성하는 계획이어야 한다.

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
   - `status/completion_audit/`의 최신 리포트 (있으면)
   - 파생 콘텐츠의 전달 구조를 계획할 때 `skills/moneygame-reading-layout-auditor/references/content_shape_decision.md`
   - 최근 전체 원고 cross-format 이슈를 반영해야 할 때 `status/reading_layout_audit/2026-05-10_cross_format.md`

2. 원고 상태를 최소 비용으로 점검한다:
   - 챕터 파일 존재/구조(요약/일러스트/질문/부록 연결)
   - 자리표시 주석(추후 삽입 예정) 목록
   - 누락된 섹션(예: 레벨업 질문)
   - 완성도 점수는 `moneygame-completion-auditor`의 기준을 따른다.

3. 콘텐츠 완성도 게이트를 적용한다:
   - 85% 미만: 책 원고 개선만 작업 큐에 둔다.
   - 85% 이상 99% 미만: 책 원고 99% 개선 큐를 최우선으로 유지하되, 전체 내용을 포괄하는 강연자료(Google Slides) 기획을 작업 큐에 추가할 수 있다.
   - 99% 이상: 강연/코칭/블로그/마케팅 중 대표 상품을 본격 실행한다.
   - Google Slides 기획은 `Additionals/financial_lectures/` 아래에 저장하고, 반드시 관련 `chapters/` 링크를 Sources로 포함한다.
   - 강연/코칭/블로그 착수 전, cross-format 검수에서 Priority 1~3으로 잡힌 원고 구간은 먼저 반영하거나 산출물에서 별도 재구성한다.

4. 로드맵은 DRAFT로 만들고 "결정이 필요한 질문"을 분리한다:
   - 청중, 채널, 코칭 범위처럼 결과를 뒤집는 항목은 먼저 질문으로 올린다.
   - 확인 전에는 보수적으로 가정하고, 가정은 문서에 명시한다.
   - 강연과 코칭 중 무엇을 대표 상품(Flagship)으로 먼저 완성할지도 결정 질문으로 분리한다.

5. 산출물은 저장소 규칙에 맞게 저장한다:
   - 로드맵: `status/roadmap.md`
   - 강연: `Additionals/financial_lectures/...`
   - 코칭: `Additionals/financial_coaching/...`
   - 블로그: `Additionals/blog_posts/...`
   - 마케팅: `Additionals/content_marketing/...`

## Templates

로드맵/산출물 템플릿은 필요 시 `references/`를 읽는다:
- `skills/moneygame-planner/references/templates.md`
