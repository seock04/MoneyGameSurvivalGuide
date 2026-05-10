# Reading Layout Checklist

## Score Rubric (100)

| 영역 | 배점 | 평가 기준 |
|---|---:|---|
| 1. Mobile ebook readability | 20 | 긴 문단, 긴 목록, 넓은 표가 모바일 한 화면에서 독자를 압박하지 않는다. |
| 2. Tablet/PC scanability | 12 | H2/H3, 빈 줄, 목록 구조가 넓은 화면에서도 산만하지 않고 빠르게 훑어진다. |
| 3. Print rhythm | 12 | 종이책 페이지에서 이미지, 질문, 목록, 표가 과밀하거나 고립되어 보이지 않는다. |
| 4. Chapter opening flow | 10 | H1, 요약, 일러스트, 체크인 질문이 자연스럽게 이어진다. |
| 5. Dense content shaping | 15 | 세대별 목표, 체크리스트, 단계 설명 등 나열형 정보가 반복 구조로 정리되어 있다. |
| 6. Questions and reflection space | 8 | 체크인/레벨업 질문이 본문과 분리되고 질문 사이의 여백이 충분하다. |
| 7. Tables and lists | 8 | 표는 폭이 통제되고, 목록은 항목 수와 항목 길이가 과하지 않다. |
| 8. Images and captions | 5 | 이미지 위치, 캡션, 주변 여백이 독서 흐름을 돕는다. |
| 9. Markdown rendering safety | 5 | 강조 문법, HTML 블록, alert, 구분선이 깨질 위험이 낮다. |
| 10. Tone-layout alignment | 5 | 레이아웃이 불안, 조급함, 과잉 과제감을 만들지 않는다. |

## Format Heuristics

### Mobile ebook
- 한 문단은 가능하면 250~450자 이내를 우선한다.
- 번호/불릿 목록은 6개를 넘으면 중간 소제목 또는 표/묶음 전환을 검토한다.
- 표는 3열 이하가 가장 안정적이다. 4열 이상이거나 셀 문장이 길면 블록형 목록을 검토한다.
- 질문은 한 화면에서 하나씩 답할 수 있을 만큼 여백을 둔다.

### Tablet ebook
- 이미지와 본문 사이에 충분한 숨 공간이 있어야 한다.
- H2 아래 H3가 너무 촘촘히 이어지면 목차처럼 보일 수 있으므로 설명 문단을 둔다.
- 표와 목록은 시각적으로 정렬되어야 하지만, 본문 리듬을 끊지 않아야 한다.

### PC/web reader
- 너무 짧은 문단만 반복되면 블로그 조각처럼 보일 수 있다.
- 넓은 화면에서는 표가 유용하지만, ebook 변환을 고려해 과도한 열 확장을 피한다.
- 구분선이 너무 많으면 원고가 카드 뉴스처럼 보일 수 있다.

### Print
- 긴 표는 페이지 분할 시 읽기 어렵다. 1페이지 안에 의미 단위가 끝나는지 확인한다.
- 질문 블록과 이미지가 페이지 끝에 외롭게 걸릴 수 있는 구간을 표시한다.
- 캡션은 짧고 기능적이어야 하며 본문 설명을 반복하지 않는다.

## Dense Content Patterns

세대별 목표, 상황별 전략, 체크리스트처럼 항목이 길게 이어지는 구간은 아래 중 하나로 정리한다.

| 패턴 | 쓰임 | 주의 |
|---|---|---|
| 반복 소제목 블록 | 모바일 ebook 최우선, 각 항목 설명이 길 때 | H3가 과다해지면 H4 대신 볼드 라벨을 쓴다. |
| 3열 이하 표 | 짧은 비교, 한눈에 보는 요약 | 셀 안 문장이 길면 깨진다. |
| 번호 단계 | 순서가 중요한 실행 절차 | 단계마다 행동 동사가 선명해야 한다. |
| 질문 블록 | 독자가 자기 상황에 적용해야 할 때 | 한 불릿에 질문 하나만 둔다. |
| 요약 박스 | 긴 설명 뒤 핵심만 회수할 때 | 박스가 반복되면 강조 효과가 사라진다. |

## Severity Guide

| 등급 | 기준 |
|---|---|
| Critical | ebook/print 변환 시 깨질 가능성이 크거나, 핵심 정보를 읽기 어렵게 만든다. |
| High | 독자가 해당 구간에서 이탈할 가능성이 크다. 특히 모바일에서 과밀하다. |
| Medium | 내용은 읽히지만 배치 개선으로 이해와 스캔성이 크게 좋아진다. |
| Low | 취향성 polish, 미세한 여백, 문장 길이 조정, 캡션 보강이다. |

## Quick Commands

- 전체 빠른 스캔: `python3 skills/moneygame-reading-layout-auditor/scripts/scan_markdown_layout.py chapters/*.md`
- 5장 스캔: `python3 skills/moneygame-reading-layout-auditor/scripts/scan_markdown_layout.py chapters/05_지도는_됐고_나침반이나_주세요.md`
- 이미지 참조 확인: `rg -n "images/" chapters`
