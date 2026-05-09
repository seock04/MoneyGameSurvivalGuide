---
name: moneygame-book-illustration-designer
description: MoneyGameSurvivalGuide 책의 표지와 챕터별 일러스트를 전문 책 일러스트 디자이너 관점으로 감사하고, 출판 전문가 우선 패널 의견을 반영해 ebook/종이책에 맞는 스타일을 확정한 뒤, 필요한 신규·교체 일러스트 제작 계획을 세우고 실제 이미지 생성 및 원고 삽입까지 진행할 때 사용한다.
---

# MoneyGame Book Illustration Designer

## Overview

이 스킬은 『부의 게임, 대충 뛰어들어 끝까지 살아남기』의 시각 시스템을 실제 ebook 출간물 기준으로 재설계하고 실행한다.

목표:
- 현재 원고 변화와 챕터 추가 이후 표지·장별 일러스트가 내용과 맞는지 점검한다.
- 출판 전문가 의견을 가장 크게 반영하되, 문학/재무/코칭/심리/행동경제/한글 패널 의견을 함께 듣는다.
- 최종 결정권은 `Lead Book Illustrator`가 가진다.
- 필요한 경우 기존 이미지를 유지, 보정, 교체, 추가 중 하나로 판정한다.
- 교체/추가가 결정된 이미지는 ebook 친화적 프롬프트로 생성하고, 프로젝트 파일로 저장한 뒤 원고에 연결한다.

## Required Inputs

먼저 아래 파일을 읽는다.

- `AGENTS.md`
- `README.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `assets/target_audience.md` (있으면)
- `chapters/00_표지.md`
- `chapters/00_목차.md`
- 전체 범위 작업이면 `chapters/*.md`
- 이미지 목록: `rg --files chapters/images`
- 이미지 사용 위치: `rg -n "images/" chapters`
- 기존 시각 리뷰:
  - `status/illustrations/`
  - `status/publication_design_review/`
  - `status/expert_panel_review/`

필요할 때만 아래 세부 파일을 읽는다.

- `references/personas.md`
- `references/checklist.md`
- `references/report_template.md`

## Output Paths

- 디자인 감사 리포트: `status/illustrations/YYYY-MM-DD_book_illustration_design_audit.md`
- 제작 계획: `status/illustrations/YYYY-MM-DD_book_illustration_generation_plan.md`
- 이미지 프롬프트: `status/illustrations/prompts/<asset_slug>.txt`
- 생성 이미지: `chapters/images/<asset_slug>.png`
- 교체 전 파일은 삭제하지 않고 필요 시 `chapters/images/archive/`에 보존한다.

## Fixed Workflow

1. Scope 설정
   - 기본은 표지 + 전체 챕터 일러스트다.
   - 사용자가 특정 챕터를 지정하면 해당 범위만 다룬다.
   - 챕터 구조가 최근 바뀐 경우 전체 흐름을 먼저 본다.

2. Manuscript & Asset Inventory
   - 각 챕터의 핵심 메시지, 현재 이미지, 이미지 위치, 캡션, 파일 존재 여부를 표로 정리한다.
   - 이미지가 현재 챕터 내용과 맞는지 `keep / revise prompt / replace / add / remove`로 판정한다.
   - 표지, hero, 보조 인포그래픽, 부록 참조 이미지, 마무리 이미지를 구분한다.

3. Expert Panel Consultation
   - `references/personas.md`의 패널을 사용한다.
   - 출판 전문가는 다른 전문가보다 높은 우선순위를 가진다.
   - 패널은 의견을 내지만 결정하지 않는다.
   - 최종 결정은 `Lead Book Illustrator`가 한다.

4. Style Direction Decision
   - ebook 우선 스타일을 한 문단으로 확정한다.
   - 색감, 구도, 질감, 인물 사용, 텍스트 사용, 게임 메타포 강도, 금지 요소를 명시한다.
   - 스타일은 책 전체에 반복 가능한 시스템이어야 한다.

5. Production Queue
   - 모든 이미지를 한 번에 갈아엎지 않는다.
   - 우선순위는 표지, 새 챕터/변경된 챕터 hero, 내용과 어긋난 이미지, ebook에서 읽기 어려운 이미지 순이다.
   - 한 라운드 제작 큐는 3~8개 이미지로 제한한다.

6. Prompting
   - 각 이미지마다 독립 프롬프트 파일을 저장한다.
   - 프롬프트는 영어로 작성해 생성 품질을 높이고, 파일 상단에 한국어 목적을 짧게 적는다.
   - 이미지 안에는 원칙적으로 읽어야 하는 텍스트를 넣지 않는다.
   - 특정 ETF 티커, 수익률, 상품명, 보장 암시, 공포 장면을 넣지 않는다.

7. Generate & Integrate
   - raster 이미지가 필요하면 `$imagegen`의 기본 built-in tool mode를 사용한다.
   - 프로젝트용 이미지는 반드시 `chapters/images/`에 저장한다.
   - 기존 이미지를 덮어쓰지 말고 `*_v2.png`, `*_ebook_v1.png`처럼 새 파일명으로 저장한다.
   - 원고의 이미지 경로와 캡션을 갱신한다.
   - 생성 후 이미지 파일 존재, 링크, `git diff --check`를 검증한다.

8. Report
   - `references/report_template.md` 형식으로 결과를 저장한다.
   - 유지한 이미지와 교체한 이미지를 분리해 기록한다.
   - 다음 라운드가 필요하면 남은 큐를 3~7개로 제한한다.

## Design Principles

- 핵심 정서: 따뜻하고 대충 합리적인 생존형 재테크.
- ebook 우선: 작은 화면에서 2초 안에 핵심 장면이 읽혀야 한다.
- 출판 신뢰: 너무 아동용, 게임 UI 과잉, NFT/코인 광고 같은 인상을 피한다.
- 게임 메타포: 로그인, 인벤토리, 퀘스트, 방어막, 지도, 나침반은 쓰되 장식보다 이해를 돕는 용도여야 한다.
- 재무 안전: 돈이 자동으로 불어나는 환상, 대박, 폭락 공포, 호화 소비 이미지를 피한다.
- 시리즈감: 같은 질감, 조명, 인물 비율, 여백, 색 온도를 유지한다.
- 본문 보조: 이미지는 본문을 대신하지 않고 이해와 기억을 돕는다.

## Hard Gates

아래 항목은 `High` 이상으로 기록한다.

- 표지가 책의 장르나 약속을 오해하게 만든다.
- 새 챕터 구조와 이미지가 맞지 않는다.
- 챕터 대표 이미지가 서로 다른 책처럼 보인다.
- ebook 모바일 폭에서 핵심 의미가 사라진다.
- 이미지 안의 작은 텍스트를 읽어야만 의미가 통한다.
- 투자 수익 보장, 대박, 공포 마케팅처럼 보이는 장면이 있다.
- 이미지 링크가 누락되었거나 실제 파일이 없다.

## References

- 패널 페르소나: `references/personas.md`
- 점검표: `references/checklist.md`
- 리포트 템플릿: `references/report_template.md`
