---
name: moneygame-publication-design-review
description: MoneyGameSurvivalGuide 책의 표지, 챕터별 삽화, 이미지 일관성, 전자책/종이책 출판 적합성, 인쇄·모바일 가독성, 이미지 배치와 캡션, 디자인 누락 요소를 전문 페르소나 패널로 리뷰하고 상세 개선 제안을 status/publication_design_review/에 저장할 때 사용한다.
---

# MoneyGame Publication Design Review

## Overview

이 스킬은 『부의 게임, 대충 뛰어들어 끝까지 살아남기』를 실제 ebook 또는 종이책으로 출판한다고 가정하고, 표지와 챕터별 삽화 및 시각 디자인을 전문적으로 점검한다.

목표:
- 표지와 챕터 삽화가 책의 약속, 독자, 장르, 판매 환경에 맞는지 평가한다.
- ebook과 종이책 모두에서 깨질 수 있는 이미지·레이아웃·가독성 위험을 찾는다.
- 부족한 시각 자료, 중복 이미지, 일관성 문제, 인쇄 적합성 문제를 우선순위화한다.
- 원고 직접 수정이 아니라 **상세 리뷰와 제안**을 먼저 제공한다.

## Required Inputs

먼저 아래 파일을 읽는다.

- `AGENTS.md`
- `README.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `assets/target_audience.md` (있으면)
- `chapters/00_표지.md`
- `chapters/00_목차.md`
- 검토 범위의 `chapters/*.md`
- 사용된 이미지 목록: `rg --files chapters/images`
- 필요 시 기존 이미지 리포트: `status/illustrations/`, `status/expert_panel_review/`

세부 페르소나와 체크리스트는 필요할 때만 읽는다.

- `references/personas.md`
- `references/checklist.md`
- `references/report_template.md`

## Output Paths

- 리뷰 리포트: `status/publication_design_review/YYYY-MM-DD.md`
- 특정 범위 리포트: `status/publication_design_review/YYYY-MM-DD_cover.md`, `YYYY-MM-DD_ch01-14.md` 등

## Workflow

1. Scope 설정
   - 기본은 표지 + 전체 챕터 이미지 흐름이다.
   - 사용자가 특정 챕터나 표지만 요청하면 그 범위만 검토한다.
   - 00~14 전체 검토는 사용자가 명시했거나 출판 전 점검을 요청했을 때 수행한다.

2. Asset Inventory
   - 각 챕터의 이미지 경로, 위치, 캡션 유무, 반복 사용 여부를 표로 정리한다.
   - 실제 파일 존재 여부를 확인한다.
   - 표지, 히어로 이미지, 본문 보조 이미지, 부록 이미지로 분류한다.

3. Publication Fit Review
   - ebook: 모바일 폭, 흑백 모드, 작은 화면, alt/caption 필요성, 이미지 과밀 여부를 점검한다.
   - print: 인쇄 해상도, 여백/재단 위험, 흑백 출력 가독성, 표지 썸네일과 실물 책등 확장성을 점검한다.
   - 디자인 일관성: 색감, 캐릭터/오브젝트 스타일, 메타포 체계, 챕터별 시각 리듬을 점검한다.

4. Persona Panel
   - `references/personas.md`의 5개 페르소나로 리뷰한다.
   - 각 페르소나는 좋은 점 1개와 개선점 1개 이상을 제시한다.
   - 개선점은 “왜 출판 경험에 문제가 되는지”와 “어떻게 고칠지”를 분리한다.

5. Score & Priority
   - `references/checklist.md`의 기준으로 100점 만점 평가를 한다.
   - 이슈를 `Critical`, `High`, `Medium`, `Low`로 분류한다.
   - 표지/대표 이미지/챕터 첫 이미지/인쇄 불가 요소를 우선순위 높게 둔다.

6. Report
   - `references/report_template.md`를 따라 리포트를 저장한다.
   - 원고나 이미지 파일은 사용자 승인 없이 직접 교체하지 않는다.
   - 필요한 경우 “다음 패치 큐”를 3~7개로 제한해 제안한다.

## Hard Gates

아래 문제가 있으면 점수와 별개로 반드시 `Critical` 또는 `High`로 기록한다.

- 표지 이미지가 책의 장르·약속을 오해하게 만든다.
- ebook에서 주요 이미지가 너무 작아 핵심 내용을 읽을 수 없다.
- 인쇄용으로 쓰기 어려운 저해상도 이미지가 표지나 챕터 대표 이미지에 사용된다.
- 본문 핵심 이해가 이미지 안의 텍스트에만 의존한다.
- 이미지 파일이 누락되어 렌더링 시 깨진다.
- 표지, 챕터 이미지, 부록 이미지의 스타일이 서로 다른 책처럼 보인다.
- 투자 성과를 보장하거나 공포를 과하게 자극하는 시각 은유가 있다.

## Review Principles

- 책의 핵심 정서는 “따뜻하고 대충 합리적인 생존형 재테크”이다.
- 디자인은 화려함보다 신뢰, 명료함, 모바일 가독성, 인쇄 안정성을 우선한다.
- 게임 메타포는 유지하되, 과도한 판타지 장식보다 개념 이해를 돕는 방향으로 쓴다.
- 이미지가 본문을 대신 설명하게 하지 않는다. 이미지는 본문의 이해와 기억을 보조해야 한다.
- 표지와 1장 첫인상은 판매 환경에서 썸네일로 먼저 판단된다는 점을 항상 고려한다.

## References

- 페르소나: `references/personas.md`
- 점검표: `references/checklist.md`
- 리포트 템플릿: `references/report_template.md`
