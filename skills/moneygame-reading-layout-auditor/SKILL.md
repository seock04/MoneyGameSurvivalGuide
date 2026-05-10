---
name: moneygame-reading-layout-auditor
description: MoneyGameSurvivalGuide 책 원고가 실제 독자에게 보이는 형태에서 읽기 좋은지 검수할 때 사용한다. 종이책, 모바일 ebook, 태블릿 ebook, PC 화면을 모두 고려해 문단 길이, 목록/표/질문/이미지 배치, 챕터별 정보 밀도, Markdown 렌더링 위험, 세대별 목표처럼 나열형 콘텐츠의 재배치를 점검하고 status/reading_layout_audit/에 리포트를 남길 때 사용한다.
---

# MoneyGame Reading Layout Auditor

## Overview

이 스킬은 『부의 게임, 대충 뛰어들어 끝까지 살아남기』 원고를 "내용이 좋은가"가 아니라 "독자가 실제 화면과 종이에서 편하게 읽는가" 기준으로 검수한다.

핵심 목표:
- 모바일 ebook에서도 숨이 막히지 않는 문단/목록/표 리듬을 만든다.
- 종이책, 태블릿, PC에서 구조가 과하게 잘게 쪼개지거나 산만해지지 않는지 확인한다.
- 세대별 목표, 체크리스트, 단계형 설명처럼 정보가 나열되는 구간을 카드형/표형/소제목형/질문형 중 적절한 형태로 재배치하도록 제안한다.
- 원고 직접 수정 전, 문제 위치와 개선 방식을 리포트로 남긴다. 사용자가 특정 수정을 요청하면 해당 범위만 반영한다.

## Required Inputs

먼저 아래 파일을 읽는다.

- `AGENTS.md`
- `README.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `assets/target_audience.md` (있으면)
- 검토 범위의 `chapters/*.md`
- 최신 상태 참고: `status/roadmap.md`, `status/completion_audit/`, `status/manuscript_audit/` (있으면)

세부 기준은 필요할 때만 읽는다.

- `references/checklist.md`
- `references/report_template.md`

## Output Paths

- 전체 검수 리포트: `status/reading_layout_audit/YYYY-MM-DD_full.md`
- 특정 챕터 리포트: `status/reading_layout_audit/YYYY-MM-DD_chNN.md`
- 스크립트 원자료가 필요하면: `status/reading_layout_audit/YYYY-MM-DD_scan.md`

## Workflow

1. Scope 설정
   - 사용자가 "전체" 또는 "처음부터 끝까지"를 요청하면 `chapters/00_*.md`부터 `chapters/15_*.md`까지 검토한다.
   - 특정 챕터만 요청하면 해당 챕터와 앞뒤 챕터 1개씩을 함께 훑어 리듬 차이를 확인한다.

2. Quick Scan
   - `scripts/scan_markdown_layout.py`를 실행해 긴 문단, 긴 표 행, 과밀 목록, 이미지 누락, 질문/구분선 패턴을 찾는다.
   - 스크립트 결과는 최종 판단의 보조 신호로만 사용한다. 한국어 원고의 문학적 리듬은 반드시 사람이 다시 읽고 판단한다.

3. Multi-Format Review
   - 모바일 ebook: 한 화면에 긴 문단/목록이 뭉쳐 보이는지, 표가 좌우 스크롤 없이 읽히는지, 질문 섹션이 독립 공간처럼 보이는지 확인한다.
   - 태블릿 ebook: 이미지와 본문 사이의 간격, 소제목 깊이, 표/리스트의 폭을 확인한다.
   - PC 화면: 너무 잘게 쪼개져 산만하지 않은지, 빈 줄과 헤더가 과한지 확인한다.
   - 종이책: 페이지 중간에 표/목록이 과밀하게 걸릴 가능성, 이미지/캡션/질문 박스의 지면 리듬을 확인한다.

4. Content Shape Decision
   - 나열형 콘텐츠는 의미에 따라 재배치 방식을 선택한다.
   - 비교/분류는 표를 우선 검토하되, 모바일에서 표가 넓어지면 짧은 소제목 블록이나 카드형 목록을 제안한다.
   - 단계/순서는 번호 목록을 사용한다.
   - 독자가 직접 답해야 하는 항목은 질문 블록과 빈 줄을 늘린다.
   - 세대별/상황별 목표는 "세대 -> 핵심 목표 -> 실행 예시 -> 주의점" 같은 반복 구조로 묶어 스캔 가능하게 만든다.

5. Severity & Patch Queue
   - `references/checklist.md` 기준으로 이슈를 `Critical`, `High`, `Medium`, `Low`로 분류한다.
   - 한 라운드의 수정 후보는 독자 이탈을 줄이는 3~7개로 제한한다.
   - 문체, 투자 안전성, 기존 목차 구조를 바꾸는 수정은 사용자 동의 없이 확정하지 않는다.

6. Report
   - `references/report_template.md`를 따라 리포트를 저장한다.
   - 각 이슈에는 위치, 문제, 형식별 영향, 구체적 개선안을 함께 적는다.
   - 수정까지 수행했다면 변경 파일과 재검수 결과를 리포트에 추가한다.

## Hard Gates

아래 항목은 발견 즉시 `Critical` 또는 `High`로 기록한다.

- 모바일에서 한 문단 또는 한 목록 덩어리가 너무 길어 독자가 핵심을 놓친다.
- 넓은 표가 ebook에서 깨지거나 좌우 이동 없이는 의미를 파악하기 어렵다.
- 이미지 파일이 누락되어 렌더링이 깨진다.
- 질문 섹션, 요약, 본문, 레벨업이 시각적으로 구분되지 않는다.
- 세대별/상황별 설명이 같은 형식 없이 이어져 스캔이 어렵다.
- Markdown 강조 문법, HTML 블록, 경고 박스가 렌더링에서 본문처럼 노출될 위험이 있다.

## Review Principles

- 이 책의 기본 정서는 "따뜻하고 대충 합리적인 생존형 재테크"이다. 레이아웃도 독자를 몰아붙이지 않아야 한다.
- 게임 메타포는 장식보다 길안내 역할을 해야 한다.
- 모바일 ebook을 가장 엄격한 기준으로 삼되, 종이책과 PC에서 지나치게 조각난 인상을 만들지 않는다.
- 표는 보기 좋지만 작은 화면에서 약하다. 표가 4열 이상이거나 셀 내용이 길면 대체 배치를 검토한다.
- 긴 문단을 무조건 나누지 않는다. 핵심 문장, 예시, 행동 지시가 섞일 때 나누는 것이 우선이다.

## References

- 검수표: `references/checklist.md`
- 리포트 템플릿: `references/report_template.md`
- 빠른 스캔: `scripts/scan_markdown_layout.py`
