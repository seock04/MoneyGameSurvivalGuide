# Content Shape Decision

## Used By

This reference is the shared cross-format content-shaping standard for:

- `moneygame-reading-layout-auditor`: book, ebook, Word, PPT readability audit.
- `moneygame-blog-posting`: convert book material into blog posts with reader problem, core message, proof/example, and action CTA.
- `moneygame-coaching-design`: convert book material into coaching sessions, worksheets, and slide outlines with message, question, exercise, and next action.
- `moneygame-planner`: plan lecture, coaching, blog, and marketing roadmaps using medium-native message/evidence/action structures.

## Evidence Base

이 기준은 다음 연구와 실무 가이드를 바탕으로 적용한다.

- GOV.UK Content Design: 콘텐츠는 조직이 말하고 싶은 것보다 사용자가 알아야 하거나 해야 할 일을 중심으로 설계해야 한다. 필요하면 양을 줄이고, 큰 덩어리를 쪼개고, 형식을 바꾼다. 블로그나 다른 채널로 발행하는 선택도 콘텐츠 설계의 일부다.
- Cognitive Load Theory: 복잡한 정보는 제한된 작업 기억을 압박한다. 독자가 동시에 처리해야 하는 요소를 줄이고, 불필요한 처리 부담을 낮추는 방식으로 설계해야 한다.
- Signaling/Cueing Principle: 학습자는 핵심 조직과 관련 요소를 가리키는 신호가 있을 때 더 깊게 배운다. 소제목, 라벨, 강조, 순서 번호는 장식이 아니라 주의를 안내하는 신호다.
- Web scanning research and content design practice: 온라인 독자는 대체로 훑어 읽는다. 왼쪽 정렬의 명확한 소제목, 짧은 문단, 굵은 첫 단어, 목록 구조가 탐색을 돕는다.
- Assertion-Evidence slide research: 슬라이드에서는 주제어 제목과 불릿 묶음보다, 결론형 문장 제목과 이를 뒷받침하는 시각적 근거가 이해와 기억에 유리하다.
- Effective slide design guidance: 슬라이드는 한 장에 하나의 아이디어를 담고, 발표자가 말하는 동안 청중이 읽느라 듣지 못하는 상황을 피해야 한다.

## Core Principle

콘텐츠 내용만큼 중요한 것은 전달 방식이다.

좋은 내용도 독자가 어디를 보고, 무엇을 비교하고, 무엇을 기억하고, 어떤 행동을 해야 하는지 알 수 없다면 출간 품질 이슈다. 레이아웃 검수는 예쁘게 꾸미는 작업이 아니라 의미 전달을 설계하는 작업이다.

## Decision Flow

1. **Reader job**
   - 이 구간에서 독자가 해야 할 일을 하나로 정한다: 이해, 비교, 선택, 실행, 회고, 기억, 공유.
   - 하나의 구간에 reader job이 2개 이상 섞이면 소제목을 나눈다.

2. **Message unit**
   - 각 단위는 `핵심 메시지 -> 근거/예시 -> 실행/주의` 순서로 정리한다.
   - 핵심 메시지가 마지막에 숨어 있으면 앞으로 당긴다.
   - 근거가 4개 이상이면 묶음, 표, 별도 부록, 또는 블로그/PPT 확장 자료로 분리한다.

3. **Cognitive load**
   - 독자가 동시에 비교해야 하는 축이 3개를 넘으면 표나 반복 블록으로 바꾼다.
   - 문단 안에 숫자, 감정 묘사, 사례, 행동 지시가 함께 있으면 최소 2개 블록으로 나눈다.
   - 긴 설명 뒤에는 한 줄 회수 문장이나 요약 불릿을 둔다.

4. **Signal**
   - 소제목은 주제어보다 결론이나 독자 이득을 담는다.
   - 반복 라벨은 같은 순서를 유지한다. 예: `북극성 -> 목표 -> 실행 -> 기한 -> 안전장치`.
   - 굵은 글씨는 문장 전체가 아니라 스캔해야 할 라벨이나 핵심 단어에 쓴다.

5. **Media transfer**
   - 책: 감정선과 설명의 온도를 유지하되, 정보 덩어리는 숨 쉴 공간을 둔다.
   - 블로그: 검색 독자가 첫 화면에서 문제, 결론, 실행 이득을 파악할 수 있어야 한다.
   - PPT: 한 슬라이드에 하나의 주장만 남긴다. 제목은 결론문, 본문은 근거 1~3개 또는 시각 자료로 제한한다.

## Pattern Selection

| Reader job | Best shape | Avoid |
|---|---|---|
| 이해 | 짧은 설명 문단 + 한 줄 회수 문장 | 긴 비유와 정의를 한 문단에 압축 |
| 비교 | 2~3열 표 또는 H3 비교 블록 | `•`, `👉`, `→` 수동 기호로 이어붙인 비교 |
| 선택 | 상황별 반복 블록 | 여러 상황을 한 문단에서 쉼표로 나열 |
| 실행 | 번호 단계 + 체크리스트 | 실행 순서가 없는 긴 불릿 |
| 회고 | 질문 블록 + 충분한 여백 | 한 불릿에 질문 2개 이상 |
| 기억 | 결론형 소제목 + 요약 박스 | 마지막 문장에만 핵심 결론 배치 |
| 공유 | 블로그형 요약 + CTA | 맥락 없는 인용문 또는 과한 장식 |

## Book-Specific Rules

- 독자가 감정적으로 따라와야 하는 대목은 문단형 설명을 유지한다.
- 정보 처리 대목은 반복 구조를 쓴다.
- 사례가 3개 이상이면 각 사례를 `H3` 또는 굵은 라벨 블록으로 분리한다.
- 표는 비교 축이 짧고 셀 문장이 짧을 때만 쓴다. 긴 셀은 모바일 ebook에서 블록 목록보다 약하다.
- 부록은 압축해도 되지만, 모바일에서 참고표가 벽처럼 보이면 블록형으로 바꾼다.

## Blog Conversion Rules

- 글 첫 20% 안에 독자의 문제, 핵심 답, 읽을 이유가 보여야 한다.
- H2는 검색어와 독자 질문을 반영하되, 본문 H3는 실행 단위로 쪼갠다.
- 책의 긴 정서적 도입은 블로그에서는 1~2문단으로 압축한다.
- 블로그용 CTA는 책의 레벨업 질문을 변환해 만든다.

## PPT Conversion Rules

- 한 슬라이드 = 한 주장.
- 제목은 결론문으로 쓴다.
- 본문 텍스트는 발표자의 대본이 아니라 청중의 길잡이다.
- 표를 그대로 옮기지 않는다. 표는 핵심 숫자 1~3개, 그래프, 아이콘형 비교로 재구성한다.
- 상세 근거는 백업 슬라이드나 handout으로 보낸다.

## Format Implementation Matrix

같은 콘텐츠 구조라도 포맷별로 제대로 표현되는 문법이 다르다. 검수할 때는 겉모양보다 네이티브 구조를 우선 확인한다. 네이티브 구조는 접근성, 변환 안정성, 검색성, 재사용성을 높인다.

| Intent | Markdown | HTML | Word | PPT |
|---|---|---|---|---|
| 장/섹션 제목 | `#`, `##`, `###` | `h1`, `h2`, `h3` | Heading 1/2/3 styles | Title placeholder, section divider slide |
| 핵심 메시지 | H2/H3 뒤 첫 문단 또는 인용 블록 | `p.lead`, `strong`, `aside` | Lead paragraph style, Quote style | Assertion headline |
| 비교 | 2~3열 표 또는 H3 반복 블록 | `table` 또는 definition/list cards | Table style 또는 heading 반복 블록 | 2-column compare layout, one contrast per slide |
| 단계 | `1.`, `2.`, `3.` | `ol` | Numbered List style | Process layout, one step per slide if complex |
| 체크리스트 | `- [ ]` 또는 짧은 `-` 목록 | `ul` with checkbox styling | Checklist/List Bullet style | Icon checklist, max 3~5 items |
| 질문/회고 | `>` blockquote + blank lines | `blockquote`, `aside` | Quote/Callout style | Reflection slide, one question per slide |
| 주의/TIP | GitHub alert 또는 blockquote | `aside`, `details`, callout class | Callout text box style | Callout box, limited text |
| 이미지+캡션 | `![alt](path)` + caption text | `figure` + `figcaption` | Insert picture + Caption style | Image placeholder + short caption |
| 긴 근거 | `## Sources`, footnotes | `section`, `footer`, `details` | Endnotes/References style | Backup slide or notes |
| 실행 CTA | 마지막 짧은 문단 또는 질문 블록 | `aside` or CTA component | Callout/Action style | Closing action slide |

## Markdown Rules

- Use actual Markdown syntax, not visual symbols. Prefer `-` over `•`, and `- **결과**:` over `👉 결과:`.
- Leave blank lines before and after headings, blockquotes, HTML blocks, images, and tables.
- In HTML blocks inside Markdown, use `<strong>` instead of `**bold**` because some renderers do not parse Markdown inside HTML.
- Avoid deeply nested lists in ebook text. If a list needs 2 levels and more than 5 items, consider H3 blocks.
- Keep tables mobile-safe: 3 columns or fewer when cells contain sentences. Use repeated blocks for long-cell comparisons.

## HTML Rules

- Use semantic tags first: `article`, `section`, `h2`, `h3`, `p`, `ul`, `ol`, `blockquote`, `figure`, `figcaption`, `table`, `aside`.
- Do not build headings with styled `div` or `span`; this breaks navigation and accessibility.
- Use `figure/figcaption` for images that support meaning. Decorative images should be avoided in mobile-first outputs unless they carry the book's atmosphere at a chapter opening.
- Use `aside` for TIP, caution, or summary boxes. It should be short and independent.
- Tables need headers (`th`) and should not be used for layout.

## Word Rules

- Use Word styles, not manual formatting. Heading 1/2/3, Normal, List Bullet, List Number, Quote, Caption, and Table styles should carry the structure.
- Use page breaks or section breaks only for real section transitions. Do not use repeated blank paragraphs to force layout.
- Use built-in captions for images/tables so cross-references and lists of figures can be generated later.
- Use table styles for true tables. For mobile-derived long comparison blocks, use headings and lists rather than a wide table.
- Keep callout boxes editable and style-based. Avoid image screenshots of text.

## PPT Rules

- Use a slide layout, not a pile of free-floating text boxes. Title, body, image/chart, and notes should have separate roles.
- Use assertion-evidence structure when teaching or persuading: the title states the conclusion, and the body proves it with a visual or 1~3 short supports.
- Put script, nuance, and caveats in speaker notes or backup slides, not in tiny slide text.
- Avoid copying book paragraphs into slides. Convert paragraphs into a claim, a visual, and a spoken explanation.
- Use tables only for small comparisons. If a table has more than 3 columns or dense text, split it into multiple slides or convert it to a visual comparison.

## Blog Rules

- Use H2/H3 headings that match reader questions and search intent.
- Start with the conclusion or the reader's problem; do not keep the answer until the end.
- Use short paragraphs, bullets, and summary blocks for scanning.
- Convert book reflection questions into CTA or comment prompts.
- Keep Sources or external references at the end unless the claim depends on immediate credibility.

## Format Red Flags

- Markdown: visible `**`, broken HTML block, `•` lines that collapse into paragraphs, wide tables.
- HTML: layout-only tables, headings made with `div`, missing image alt/caption, dense paragraph walls.
- Word: manual bold/size headings, blank lines used as layout, screenshots of text, tables that span beyond page width.
- PPT: topic-only titles, slide as teleprompter, more than one main claim, tiny footnotes, paragraph pasted into body.

## Source Links

- GOV.UK Content Design: https://www.gov.uk/guidance/content-design/what-is-content-design
- GOV.UK Writing for GOV.UK: https://www.gov.uk/guidance/content-design/writing-for-gov-uk
- Cognitive Load Theory review: https://link.springer.com/article/10.1007/s10648-010-9145-4
- Signaling/Cueing Principle: https://dspace.library.uu.nl/handle/1874/424007
- Assertion-Evidence slides: https://pure.psu.edu/en/publications/assertion-evidence-slides-appear-to-lead-to-better-comprehension--2/
- Ten simple rules for effective presentation slides: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009554
