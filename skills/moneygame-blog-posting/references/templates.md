# Templates (Blog Posting)

## 100개 기획 항목 포맷(권장)

```md
| id | title | one_liner | misconception | action | chapter_sources |
|---:|---|---|---|---|---|
| 1 | ... | ... | ... | ... | Book: [Chapter 2](../../chapters/02_...md) |
```

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
