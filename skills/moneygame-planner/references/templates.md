# Templates

이 파일은 `moneygame-planner`가 반복적으로 쓰는 문서 골격을 제공한다.

## Roadmap 문서 골격 (`status/roadmap.md`)

`moneygame-planner`는 로드맵을 "처음에는 러프, 진행하면서 점점 구체화"하는 방식으로 운영한다.
즉, 한 번에 완성도를 올리는 문서가 아니라 "다음 액션 1개"를 계속 작게 만들어 내는 문서이다.

```md
# Roadmap (DRAFT)

작성일: YYYY-MM-DD (Asia/Seoul)

독자 레퍼런스:
- `assets/target_audience.md`

우선순위(러프):
- 1) 책 원고 완료(최우선)
- 2) 대표 상품 1개 선택(강연 vs 코칭) 후 끝까지 완성
- 3) 나머지 상품 완성
- 4) 단계별 마케팅(완료 시점마다)
- 5) 장기 운영 + 확장 아이템 검토

결정 질문:
- 대표 상품(Flagship): 강연 vs 코칭

구체화 규칙:
- Level 0(러프): 목표/산출물/결정 질문/다음 액션만 적는다.
- Level 1(개요): 파일 트리(outlines/drafts/final)와 Sources(챕터 링크)까지 고정한다.
- Level 2(실행): 각 산출물의 템플릿을 채우고(초안), 점검 리포트를 남긴다.

---

## 0) 현재 상태(스냅샷)

## 1) 책 원고 완료
- Definition of Done:
- Risks:
- Decision questions:
- Next action:

## 2) 강연 자료 완료(1h/2h/3h)
- DoD:
- Audience/Channel assumptions:
- Deliverables tree:
- Next action:

## 3) 코칭 설계 완료(3종)
- DoD:
- Scope/No-scope:
- Deliverables tree:
- Next action:

## 4) 블로그 100 기획/작성
- DoD:
- Parallel policy: 책/강연/코칭과 병행 가능(단, `Additionals/RULES.md` 준수)
- Sprint rules:
- Next action:

## 5) 마케팅 계획 완료
- DoD:
- Funnel/Calendar/Metrics:
- Next action:

## 6) 확장 아이템 후보 검토(전체 완료 후)
- Candidates:
- Evaluation rubric:
- Next action:
```

## Additionals 문서 골격

```md
# Title

## 목적
- 이 문서는 책의 어떤 내용을 강조하거나, 어떤 오해를 줄이기 위해 존재하는가

## 핵심 메시지 (1문장)

## 아웃라인
- ...

## Sources
- Book: [Chapter X](../../chapters/XX_....md)
```

## 강연 아웃라인 골격 (1h/2h/3h 공통)

```md
# Lecture (1h/2h/3h) Outline

## Audience

## Goal

## Cross-Format Source
- Content shape rules: `skills/moneygame-reading-layout-auditor/references/content_shape_decision.md`
- Latest audit: `status/reading_layout_audit/2026-05-10_cross_format.md`

## Flow
- Intro
- Core 1
- Core 2
- Action plan
- Q&A

## Slide Message Map
| # | assertion_title | evidence_or_visual | speaker_note_role | audience_action | sources |
|---:|---|---|---|---|---|
| 1 | ... | ... | ... | ... | Book: ... |

## Exercises (선택)

## Sources
- Book: ...
```

## 강연 콘텐츠 전환 규칙

책 원고를 강연 콘텐츠로 계획할 때는 다음 기준을 로드맵과 산출물 DoD에 넣는다.

- 한 슬라이드에는 하나의 주장만 둔다.
- 슬라이드 제목은 주제어가 아니라 결론문이어야 한다.
- 책의 긴 표는 슬라이드 본문에 붙이지 않는다. 핵심 숫자 1~3개, 차트, handout, 백업 슬라이드 중 하나로 변환한다.
- 발표자가 말할 내용은 speaker notes로 보내고, 화면에는 청중이 기억할 메시지만 남긴다.
- 강연 마지막에는 감동 요약보다 10분 안에 할 수 있는 실행 행동을 남긴다.

## 코칭 프로그램 골격 (3회차)

```md
# Coaching Program (3 sessions)

## 대상

## 약속(Outcome)

## 범위/비범위

## 1회차

## 2회차

## 3회차

## 자료/과제

## Sources
- Book: ...
```
