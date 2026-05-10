# Templates (Blog Posting)

## 100개 기획 항목 포맷(권장)

```md
| id | title | reader_problem | one_liner | proof_or_example | action_cta | chapter_sources |
|---:|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | Book: [Chapter 2](../../chapters/02_...md) |
```

## Cross-Format 적용 규칙

책 원고를 블로그로 바꿀 때는 `skills/moneygame-reading-layout-auditor/references/content_shape_decision.md`를 기준으로 다음 구조를 우선한다.

- 첫 화면: 독자 문제, 결론, 읽을 이유가 보여야 한다.
- 본문: 책의 긴 설명은 `핵심 메시지 -> 근거/예시 -> 실행 CTA`로 접는다.
- 표/비교: 모바일 기준 3열 이하가 원칙이다. 4열 이상이면 카드형 비교, 요약 박스, 이미지/도표로 바꾼다.
- 질문: 책의 체크인/레벨업 질문은 블로그의 댓글 질문, 저장용 체크리스트, 오늘의 퀘스트로 변환한다.
- 이미지: 대표 이미지는 글의 결론을 보여주고, 보강 이미지는 실행 행동 하나를 강화한다.

## Sources 섹션 포맷

```md
## Sources
- Book: [Chapter 2](../../chapters/02_부의_게임_자동_사냥_모드로_전환하세요.md)
- External: [자료명](https://example.com) - (책 내용 이해 보조 목적 명시)
```

## 이미지 생성 프롬프트 포맷(권장, 2장)

포스팅마다 이미지 2장을 만든다.
- main: 포스팅 대표(제목/핵심 메시지 요약)
- reinforce: 본문 중 핵심 메시지 강화(오해 컷 또는 실행 1개 강화)

```md
## Image Prompts

### main
- intent: 이 글의 대표 이미지(핵심 1문장 시각화)
- prompt:
  - style: warm, minimal, friendly illustration, "따뜻하고 대충 합리적인" 분위기, no fear marketing, no luxury flex
  - content: (글의 핵심 1문장 + 게임 메타포 1개 이내)
  - composition: simple, readable, subject centered
  - text: none (or 1 short line max)

### reinforce
- intent: 독자 행동(오늘의 퀘스트) 또는 오해 컷을 강화하는 이미지
- prompt:
  - style: same as main (consistent)
  - content: (오해 1개를 걷어내고 실행 1개를 남기는 장면)
  - composition: include a clear before/after contrast without harshness
  - text: none (or 1 short line max)
```

## 이미지 삽입 블록(권장)

```md
<div align="center">

![<alt_text>](../assets/images/<post_slug>_main.png)

</div>
```
