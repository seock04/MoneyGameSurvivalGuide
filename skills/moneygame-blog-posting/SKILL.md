---
name: moneygame-blog-posting
description: MoneyGameSurvivalGuide 책 내용을 기반으로 '경제 전문 인플루언서' 페르소나의 블로그 포스팅을 100개 규모로 기획/작성하고, 산출물을 Additionals/blog_posts 아래(outlines/drafts/final)에 저장하도록 강제할 때 사용한다. 책 원고를 블로그로 옮길 때는 cross-format 콘텐츠 구조 기준을 참고해 문제, 결론, 근거, 실행 CTA가 첫 화면부터 분리되어 전달되도록 점검한다.
---

# MoneyGame Blog Posting

## Overview

이 스킬은 책 원고(`chapters/`)를 근거로 블로그 포스팅을 기획하고 작성한다. 책의 범위를 넘어가는 정보는 "책 이해 보조" 목적일 때만 허용하며, 모든 문서에 `## Sources`로 출처 링크를 포함한다.

핵심 제약:
- `Additionals/RULES.md`를 따른다. (책 기반, 출처 링크 필수, 독립 주장 금지)
- 작업은 단계별로 진행한다. 이해/동의가 없는 새 주장은 확정해서 넣지 않는다. (`AGENTS.md`)
- 책 원고를 그대로 붙여 넣지 않고, 블로그 독자가 첫 화면에서 `문제 -> 결론 -> 근거 -> 오늘의 실행`을 파악하도록 재배치한다.

## Output Locations (fixed)

- 기획: `Additionals/blog_posts/outlines/`
- 초안: `Additionals/blog_posts/drafts/`
- 확정: `Additionals/blog_posts/final/`

## Required Inputs (read first)

- `Additionals/RULES.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `assets/target_audience.md`
- `Additionals/blog_posts/outlines/persona_econ_influencer.md`
- `Additionals/blog_posts/outlines/post_template.md`

## Workflow (Step-by-step)

1. 100개 기획을 먼저 만든다(글부터 쓰지 않는다).
   - `Additionals/blog_posts/outlines/blog_100_plan.md`에 제목/핵심 1문장/주요 오해 1개/실행 1개/연결 챕터를 기록한다.
   - 각 항목은 반드시 최소 1개 `chapters/*.md` 링크를 포함한다.

2. 스프린트 단위로 작성한다(권장: 10개 단위).
   - `drafts/`에 10개 초안을 만들고, 톤/가독성/출처를 점검한 뒤 `final/`로 승격한다.

3. 각 글은 템플릿을 강제한다.
   - `Additionals/blog_posts/outlines/post_template.md` 구조를 따른다.
   - `## Sources`에 Book(챕터 링크) 최소 1개를 넣는다.
   - 책의 표, 비교 블록, 체크리스트를 가져올 때는 `핵심 메시지 -> 근거/예시 -> 실행 CTA` 순서로 다시 접는다.
   - 모바일 화면 기준으로 긴 표는 3열 이하, 카드형 비교, 또는 요약 박스로 바꾼다.

4. 이미지 2장을 생성하고 글에 삽입한다(권장: `image_gen`).
   - 목표: 포스팅마다 대표 이미지 1장(main) + 메시지 강화 이미지 1장(reinforce), 총 2장을 만든다.
   - 저장 위치(권장): `Additionals/blog_posts/assets/images/`
   - 파일명(권장):
     - `<post_slug>_main.png`
     - `<post_slug>_reinforce.png`
   - 삽입 위치(권장):
     - main: 제목/핵심 1문장 다음(포스팅 대표)
     - reinforce: 본문 중 "핵심 개념 1개" 직후 또는 "오늘의 퀘스트" 직전(메시지 강화)
   - 스타일(권장):
     - 따뜻하고 대충 합리적인(Reasonable) 분위기, 과장/공포/성공 과시 금지
     - 게임 메타포는 이해를 돕는 정도로만 쓰고, 장식 과잉은 피한다
     - 텍스트가 필요한 경우 최소화하고, 들어가더라도 짧게(문구 1줄)만 넣는다
   - 생성 원칙:
     - 이미지 생성이 가능하면: `image_gen`으로 2장 생성 후 파일로 저장하고 문서에 링크를 삽입한다.
     - 이미지 생성이 불가하면: (1) 이미지 프롬프트 2개를 문서에 남기고, (2) 이미지 자리표시 링크를 추가한 뒤, 나중에 이미지만 채우는 방식으로 진행한다.

5. 외부 자료를 쓰는 경우(선택):
   - 반드시 "책의 어떤 문장을 이해시키기 위한 보조인지"를 한 줄로 명시한다.
   - 외부 링크를 `## Sources`에 추가한다.

## File Naming

- 파일명은 ASCII 소문자 `snake_case`를 기본으로 한다. (`Additionals/RULES.md`)
- 권장: `YYYY-MM-DD_<slug>.md`

## References

필요 시 아래 참고 템플릿을 읽는다:
- `skills/moneygame-blog-posting/references/templates.md`
- 책/블로그/PPT/Word 간 전달 구조 판단이 필요하면 `skills/moneygame-reading-layout-auditor/references/content_shape_decision.md`를 읽는다.
- 최근 전체 원고 cross-format 검수 결과가 필요하면 `status/reading_layout_audit/2026-05-10_cross_format.md`를 참고한다.
