# Roadmap (DRAFT)

작성일: 2026-04-26 (Asia/Seoul)

이 문서는 『부의 게임, 대충 뛰어들어 끝까지 살아남기』 프로젝트의 "책 완성 + 파생 콘텐츠(강의/코칭/블로그/마케팅)"를 한 흐름으로 연결하는 실행 로드맵이다.

원칙:
- 이 문서는 확정본이 아니라 DRAFT이며, 이해/동의가 필요한 항목은 먼저 확인한다.
- 책 외 콘텐츠는 `Additionals/RULES.md`를 따른다. (책 기반, 책 이해 보조 목적, 출처 링크 필수)
- 작업은 단계별로 진행한다. (AGENTS.md의 "이해 확인 후 반영" 원칙 준수)

독자 레퍼런스:
- `assets/target_audience.md`를 타깃 독자 전제의 기준으로 사용한다. (언어/용어 난이도/불안 트리거/실행 제약)

구체화 방식(러프 -> 구체):
- Level 0(러프): 목표/산출물/결정 질문/다음 액션만 확정한다.
- Level 1(개요): 파일 트리(outlines/drafts/final)와 `## Sources`(챕터 링크)를 고정한다.
- Level 2(실행): 템플릿을 실제로 채우고(초안), 점검 리포트를 남긴다.

---

## 우선순위 실행 순서(러프)

원칙:
- 최우선은 책 원고 완료이다. (가장 중요한 코어 콘텐츠)
- 책 다음은 "강연 vs 코칭" 중 하나를 대표 상품(Flagship)으로 선택해 크게 시작한다.
- 대표 상품이 끝나면 다른 하나로 넘어간다.
- 마케팅은 전체를 한 번에 만들지 않고, 책/강연/코칭이 "완료"될 때마다 그 산출물을 기준으로 계획을 완성하고 실행한다.
- 전부 완료되면 장기 마케팅 플랜 + 다음 확장 아이템을 검토한다.

결정 필요(1개만 선택):
- 대표 상품(Flagship): `강연(1h/2h/3h)` vs `코칭(3회차 패키지)`

보류(2026-04-22 확정):
- 책 원고 품질(톤/가독성/팩트/일러스트)이 99% 이상 완료되기 전까지, 대표 상품(강연/코칭) 결정 및 2~5번 섹션의 Level 2 구체화는 진행하지 않는다.

업데이트(2026-04-26):
- `moneygame-completion-auditor` 기준 1차 완성도 점검 결과, 콘텐츠 완성도는 88.5점이다.
- 즉시 후속 패치로 렌더링 위험을 정리해 현재 추정 점수는 90.0점이다.
- 99% 출간 게이트는 아직 통과하지 못했다. 당시 주요 사유는 일부 Sources 보강, 3/5/10장 페이싱 정리였다.
- 다만 85% 콘텐츠 완성도 게이트는 넘었으므로, 전체 책을 포괄하는 강연자료(Google Slides) 기획은 작업 큐에 추가한다.
- 실제 최종 슬라이드 제작은 원고 99% 게이트 통과 후 또는 사용자 명시 승인 후 진행한다.

업데이트(2026-04-27):
- Round 2 1차 패치로 `chapters/03`, `05`, `07`, `09`, `11`, `12`에 최소 Sources를 추가했다.
- `chapters/05`, `12`의 직접 투자/수익률 오해 가능성이 있는 문장을 더 보수적으로 완화했다.
- 3/5/10장 페이싱 압축은 본문 대량 삭제 전 후보 문서로 분리했다: `status/pacing_compression/2026-04-27_round-2_candidates.md`
- 사용자 승인 범위에 따라 3장/5장 압축과 10장 브리지 보강을 반영했다.
- 추가 발견 사항 기준으로 10장 S&P 500/환율 수치 검산, 14장 질문 보강, 9장 생존선 템플릿, 이미지 사용 인벤토리 작성을 완료했다.
- Round 2B 당시 남은 리스크는 한국부동산원 R-ONE 동적 통계의 수동 재확인과 미사용 이미지 정리 정책 결정이었다.
- Round 3에서 6장 Sources 보강, R-ONE 2025.12 종료값 API 확인, 이미지 보관 정책, README 구조 보강을 반영했다.
- Completion audit Round 3 점수는 97.1점이며, Medium 이슈 0개 상태로 강연 슬라이드 기획을 완료했다: `status/completion_audit/2026-04-27_round-3.md`
- 강연자료 기획 산출물은 메시지 맵, 60분 슬라이드 초안, handout까지 작성했다.

## 0) 현재 상태 점검 (원고)

스냅샷:
- `chapters/`에 00~14까지 원고 파일이 존재한다.
- 대부분의 챕터에 `[체크인 질문]`, `[퀘스트 완료 레벨업 질문]` 구성이 들어 있다.
- 대표 일러스트(hero)는 챕터 상단에 삽입되어 있다. (일부는 placeholder 교체 작업이 남아 있다)
- 톤 정책(평어체)은 2026-04-22에 요약/질문/안내 문구까지 포함해 통일했다.
- 2026-04-26 completion audit Round 1 기준 점수는 88.5점이고, 즉시 렌더링 패치 후 추정 점수는 90.0점이다.

즉시 보완 후보:
- Sources가 없는 챕터 중 수치/인용/철학 설명이 있는 장의 최소 출처 보강.
- Chapter 03/05/10의 페이싱 압축 후보 표시.
- 챕터별 대표 일러스트(hero) 최종 사용 목록 정리.

완성 정의(초안):
- 모든 일반 챕터가 "요약/일러스트/체크인/본문/레벨업" 구조를 만족한다.
- 모든 챕터가 Markdown 렌더링 관점에서 가독성 이슈가 없다.
- 책 밖의 숫자/통계/사실 주장에는 출처가 정리되어 있다. (책 본문 내 또는 부록/외부 링크)

---

## 1) 책 완성 로드맵 (원고 품질)

### 운영 방식: Round 반복(품질 99% 게이트)

원고 품질은 한 번에 끝내지 않고, Step 1~5를 한 세트로 묶어 **여러 Round**로 반복한다.
각 Round가 끝날 때마다 "수정 반영 -> 재점검"을 돌려 품질 기준을 99% 이상으로 맞춘 뒤에만 강연 자료 로드맵으로 넘어간다.

Round 정의:
- Round N = Step 1(구조/가독성) → Step 2(일러스트) → Step 3(예외/누락) → Step 4(팩트/출처) → Step 5(Expert Panel Review)
- Round N 종료 조건: 각 Step의 수정 사항을 반영하고, 재점검에서 "치명 이슈 0" 상태가 된다.

Round 기록(권장):
- Round별 체크/결정/반영 로그를 1장으로 남긴다.
  - 예시 경로: `status/book_rounds/YYYY-MM-DD_round_N.md`
  - 포함: 변경 요약, 남은 오픈 이슈, 다음 Round의 우선순위

품질 99%의 실무 정의(초안):
- 구조: 일반 챕터(00_프롤로그, 01~12, 14)가 "요약/일러스트/체크인/본문/레벨업"을 모두 만족한다.
- 가독성: `guides/DISPLAY_GUIDE.md` 기준에서 렌더링 깨짐(강조 문법, 간격, 알럿)이 없다.
- 일러스트: hero placeholder가 없고, 챕터별 대표 일러스트가 스타일 가이드를 만족한다.
- 팩트/출처: 숫자 계산/인물 인용/철학·사상 언급에서 단정 리스크가 없고, 필요한 경우 출처 정책이 일관된다.
- 리뷰: Step 5(Expert Panel Review)에서 "Biggest risk: high"가 남지 않는다.

Step 1. 구조/가독성 일괄 점검
- 체크: `guides/WRITING_RULES.md`, `guides/DISPLAY_GUIDE.md` 기준으로 섹션 구조/간격/강조 문법
- 산출물: 챕터별 체크리스트(OK/수정 필요) 1장
  - 최신 체크리스트: `status/manuscript_audit/2026-04-21.md`

Step 2. 일러스트 정책 확정
- 결정: Option A(일반 챕터마다 대표 일러스트 1장 필수)
- 산출물: 챕터별 일러스트 ToDo와 파일명 규칙
  - 정책 초안: `status/illustrations/2026-04-21.md`

Step 3. 에필로그 레벨업 질문 추가(여부 확정 후)
- 산출물: 14장에 `[퀘스트 완료 레벨업 질문]` 추가 (완료)

Step 4. 사실/수치 출처 정리
- 범위: 물가, 환율, 장기 수익률 등 "사실 주장"으로 읽히는 부분
- 산출물: 각 챕터 또는 부록/외부 링크에 Sources 정리(필요 시)
  - 오프라인 백로그(시작): `status/fact_check/2026-04-21.md`
  - 진행 로그(업데이트): `status/fact_check/2026-04-22.md`
  - Sources 표기 정책(결정): `status/fact_check/2026-04-22_sources_policy_decision.md`

Step 5. Expert Panel Review(품질 게이트)
- 목적: "원고가 맞는 말인가"보다 "독자가 끝까지 읽고, 불안에 휘둘리지 않고, 실행까지 갈 수 있는가"를 점검한다.
- 방식: `status/expert_panel_review/template.md` 템플릿으로 1챕터씩 리뷰를 남긴다.
  - 페르소나: Nobel/Finance/Coach/Psych/Humor 관점으로 강점/리스크/개선안을 동시에 확인한다.
  - 체크: 독자 불안 트리거, 논리 점프, 반복, 길이/호흡, 용어 난이도, 질문 품질(열린 질문/불렛 1문장) 등
- 산출물:
  - 챕터별 리뷰 리포트: `status/expert_panel_review/YYYY-MM-DD_chNN.md`
  - 수정 반영 로그(선택): "반영/보류/추가 확인" 3분류로 남긴다.

Step 6. 최종 통합 점검(가독성/링크/일관성)
- 체크: `guides/DISPLAY_GUIDE.md` 기준으로 간격/강조 문법/알럿 렌더링, `README.md` 목차 링크, 반복 문구의 일관성
- 산출물: 최종 점검 리포트 1장 + 수정 반영

### Round 2 작업 큐(2026-04-26 기준)

1. 렌더링 하드 게이트 해결 (완료)
   - 범위: `chapters/`의 `<div align="center">` 내부 `**` 강조
   - 목표: `DISPLAY_GUIDE.md` 기준에 맞게 `<strong>`으로 통일

2. Sources 최소 보강
   - 범위: 수치/인용/철학 설명이 있는 장 중 `## Sources`가 없는 챕터
   - 목표: 출처가 필요한 주장만 선별해 흐름을 해치지 않는 최소 Sources 추가
   - 상태: Round 2 1차 반영 완료 (`03`, `05`, `07`, `09`, `11`, `12`)

3. 페이싱 압축 후보 표시
   - 범위: Chapter 03, Chapter 05, Chapter 10
   - 목표: 삭제 전 후보 표시와 사용자 확인. 핵심 재미를 잃지 않도록 보수적으로 진행
   - 상태: 후보 문서 생성 후 승인 범위 반영 완료 (`03` A+B, `05` B, `10` A)

4. completion audit Round 2
   - 산출물: `status/completion_audit/YYYY-MM-DD_round-2.md`
   - 목표: 90점대 진입 여부와 남은 High 이슈 확인
   - 상태: 작성 및 Round 2B 업데이트 완료 (`status/completion_audit/2026-04-27_round-2.md`)

5. Round 2B 후속 보강
   - 10장 S&P 500/환율 수치 검산: 완료 (`status/fact_check/2026-04-27_ch10_table_check.md`)
   - 14장 체크인/레벨업 질문 보강: 완료
   - 9장 `내 생존선` 템플릿 추가: 완료
   - 이미지 사용 인벤토리 작성: 완료 (`status/illustrations/2026-04-27_usage_inventory.md`)
   - 상태: Round 3에서 후속 정리 완료

6. Round 3 마감 점검
   - 6장 Sources 보강: 완료
   - R-ONE 2025.12 종료값 API 확인: 완료
   - 미사용 이미지 정책: 삭제하지 않고 `chapters/images/archive/` 이동 완료
   - README Structure 보강: 완료
   - completion audit Round 3: 완료 (`status/completion_audit/2026-04-27_round-3.md`)
   - Medium closeout: 완료 (`status/manuscript_audit/2026-04-27_round-3_medium_closeout.md`)
   - 다음 작업: 실제 Google Slides 제작

강연 자료 로드맵 진행 조건:
- 최종 제작은 Step 1~5 Round 반복으로 품질 기준 99% 이상을 만족하고, Step 6 최종 통합 점검까지 통과한 뒤에 진행한다.
- 단, completion audit 점수가 85% 이상이면 전체 책을 포괄하는 강연자료(Google Slides) 기획은 작업 큐에 올릴 수 있다.

---

## 2) 강연 자료 로드맵 (1h / 2h / 3h)

메모:
- 책 원고 완료 후, 강연과 코칭 중 "대표 상품"으로 강연을 선택한 경우 이 섹션을 Level 2까지 구체화한다.
- 대표 상품이 코칭이라면 강연은 러프(Level 0~1)로만 유지하고, 코칭 완료 후에 본격화한다.

저장 위치:
- `Additionals/financial_lectures/` 아래에만 저장
- 모든 자료는 `## Sources`에 연결되는 `chapters/` 링크를 포함

공통 설계(초안):
- 1시간: "책 핵심 1줄 + 즉시 실행 3가지" 중심
- 2시간: 1시간 + 실습(인벤토리/자동이체/리스크) + Q&A
- 3시간: 2시간 + 사례/워크숍(목표/배분/심리) + 액션플랜 작성

### 2-A) 전체 책 기반 Google Slides 기획(85% 게이트 통과로 큐 추가)

상태:
- 2026-04-27 completion audit Round 3에서 콘텐츠 완성도 95.6점으로 강연 기획 착수 상태가 됐다.
- 원고 99% 출간 게이트 전이므로 실제 최종 Google Slides 제작이 아니라, 전체 구조와 슬라이드 메시지 맵, 60분 초안부터 만든다.

기획 문서:
- `Additionals/financial_lectures/outlines/full_book_google_slides_plan.md`

작업 큐:
1. 전체 책을 12개 파트로 나눈 슬라이드 메시지 맵 작성
   - 산출물: `Additionals/financial_lectures/outlines/full_book_slide_message_map.md`
   - 상태: 완료
2. 60분 버전 Google Slides 초안 작성
   - 산출물: `Additionals/financial_lectures/drafts/full_book_60m_google_slides.md`
   - 상태: 완료
3. 120분/180분 확장안 작성
   - 산출물:
     - `Additionals/financial_lectures/drafts/full_book_120m_google_slides.md`
     - `Additionals/financial_lectures/drafts/full_book_180m_workshop.md`
4. 실제 Google Slides 제작
   - 전제: 원고 99% 게이트 통과 또는 사용자 명시 승인

산출물 트리(권장):
- `Additionals/financial_lectures/outlines/lecture_1h_outline.md`
- `Additionals/financial_lectures/outlines/lecture_2h_outline.md`
- `Additionals/financial_lectures/outlines/lecture_3h_outline.md`
- `Additionals/financial_lectures/assets/` (슬라이드 이미지/도표)
- `Additionals/financial_lectures/final/` (확정 대본/슬라이드 구조)

확인 질문(결정 필요):
- 청중: 20~40 직장인 일반인가, 자영업/프리랜서 포함인가
- 강연 목표: 투자 실행 촉진인지, 불안 완화/철학 전달인지
- 법적/윤리적 범위: 특정 상품 언급을 금지할지 허용할지

---

## 3) 재무 코칭 로드맵 (3회차 패키지 3종)

메모:
- 책 원고 완료 후, 강연과 코칭 중 "대표 상품"으로 코칭을 선택한 경우 이 섹션을 Level 2까지 구체화한다.
- 대표 상품이 강연이라면 코칭은 러프(Level 0~1)로만 유지하고, 강연 완료 후에 본격화한다.

저장 위치:
- `Additionals/financial_coaching/` 아래에만 저장
- 모든 문서에 `## Sources`로 책 챕터 링크 포함

공통 구성 원칙(초안):
- 3회차는 "진단 -> 설계 -> 실행/유지"로 일관되게 간다.
- 개인 정보/민감 정보는 이 repo에 저장하지 않는다. (익명화/템플릿만 저장)

A) 3회차 1:1 반구조화 코칭
- 1회차: 북극성/목표 + 현재 인벤토리(현금흐름/재무상태) 정리
- 2회차: 자동 사냥 시스템(저축/투자/리스크) 설계
- 3회차: 유지 전략(심리/리밸런싱/리스크) + 다음 12주 플랜

B) 3회차 그룹 코칭
- 1회차: 공통 프레임 + 목표/심리 체크인
- 2회차: 인벤토리 워크숍 + 자동 사냥 시스템 워크숍
- 3회차: 리스크/배분 워크숍 + 개인 액션플랜 공유

C) 그룹 + 1:1 하이브리드
- 그룹 3회차 + 개인 1:1 1회(사전 또는 사후)
- 목적: 그룹 워크숍에서 만든 계획을 개인 상황에 맞게 "최소 수정"으로 적용

산출물 트리(권장):
- `Additionals/financial_coaching/outlines/coaching_3x_1on1.md`
- `Additionals/financial_coaching/outlines/coaching_3x_group.md`
- `Additionals/financial_coaching/outlines/coaching_3x_hybrid.md`
- `Additionals/financial_coaching/references/` (질문 리스트, 진행 가이드)

확인 질문(결정 필요):
- 코칭의 성공 지표: 실행률, 불안 감소, 현금흐름 개선 등 무엇이 1순위인가
- 코칭 범위: 투자상품 추천/매매 타이밍/세금 등 포함 여부

---

## 4) 블로그 글 100개 로드맵

병행 원칙:
- 블로그는 책/대표 상품(강연/코칭)과 **병행**해도 된다.
- 단, `Additionals/RULES.md`를 준수한다. (책 기반, `## Sources`에 챕터 링크 포함, 독립 주장 금지)
- 병행의 목적은 "새 아이디어 추가"가 아니라, 책/강연/코칭의 내용을 다른 형식으로 반복 노출해 이해와 실행을 돕는 것이다.

저장 위치:
- `Additionals/blog_posts/` 아래에만 저장
- 모든 글은 `## Sources`에 책 챕터 링크를 포함
- 책 밖의 정보는 "설명 보조"로만 사용하고 외부 링크를 병기한다.

구성(초안):
- 100개를 한 번에 쓰지 않고, 10개 단위 스프린트로 작성/검증한다.
- 각 글은 "핵심 1문장 -> 오해/함정 -> 실행 1개" 구조로 통일한다.

카테고리 설계(초안, 확정 전):
- 심리/장애물(지연): 20개
- 시스템(자동 사냥/인벤토리): 30개
- 리스크/생존: 20개
- 거인의 어깨/배분: 20개
- 벌기/파이프라인: 10개

산출물 트리(권장):
- `Additionals/blog_posts/outlines/blog_100_plan.md` (100개 제목/한줄요약/출처 링크)
- `Additionals/blog_posts/drafts/` (10개 단위)
- `Additionals/blog_posts/final/`

확인 질문(결정 필요):
- 블로그 플랫폼: 브런치/네이버/티스토리/미디엄 등
- 톤: 책과 동일 톤 100% 유지 vs 블로그용 더 짧고 직설적인 톤 허용 여부

---

## 5) 마케팅 전략 및 실행 로드맵 (단계별로 완성)

원칙:
- 마케팅은 책의 범위를 넘는 새로운 주장을 만들기 위한 것이 아니라, 책/상품이 발견되고 이해되고 실행되도록 돕는 구조로 만든다.
- "전체를 한 번에" 만들지 않고, 책/강연/코칭이 완료될 때마다 해당 산출물을 기준으로 마케팅 계획을 완성한다.

공통 산출물(기본 4종):
1) 메시지 1장(One-pager)
2) 퍼널/CTA 1장
3) 운영 캘린더(12주 또는 4주 런칭)
4) 측정 지표(최소 지표)

권장 저장 위치(초안):
- `Additionals/content_marketing/outlines/message_one_pager.md`
- `Additionals/content_marketing/outlines/funnel_and_cta.md`
- `Additionals/content_marketing/outlines/launch_calendar.md`
- `Additionals/content_marketing/outlines/12_week_calendar.md`
- `Additionals/content_marketing/outlines/metrics.md`
- `Additionals/content_marketing/outlines/faq.md`
- `Additionals/content_marketing/outlines/long_term_plan.md`

### 5-A) 책 원고 완료 후(책 기준)

Step 1. 메시지 1장(책)
- 산출물: "누구에게/어떤 문제를/어떤 약속으로/어떤 방식으로" 1장

Step 2. 퍼널/CTA(책)
- 산출물: 다음 행동 1개(예: 강연 대기/코칭 대기/뉴스레터 등) 중심으로 1장

Step 3. 운영 캘린더(책)
- 산출물: 12주 운영 캘린더(초안)

Step 4. 측정 지표(책)
- 산출물: 콘텐츠/전환 최소 지표 1장

### 5-B) 대표 상품 완료 후(강연 또는 코칭 기준)

Step 1. 메시지 1장(상품)
- 산출물: "누구에게/무엇이 달라지는지/어떤 방식으로 진행되는지" 1장

Step 2. FAQ 1장(상품)
- 산출물: 기대/한계, 범위/비범위, 참여 전 준비물

Step 3. 런칭 캘린더(상품)
- 산출물: 4주(예고 -> 안내 -> 신청 -> 마감/후기) 캘린더

Step 4. 측정 지표(상품)
- 산출물: 신청/참여/재참여 최소 지표 1장

### 5-C) 책+강연+코칭 완료 후(장기 운영)

Step 1. 장기 마케팅 플랜(초안)
- 산출물: 핵심 채널 믹스(블로그/뉴스레터/강연/코칭) + 제작/재사용 규칙

Step 2. 측정/리소스 계획(초안)
- 산출물: 월/분기 단위 운영 리듬과 최소 리소스(시간/제작) 1장

확인 질문(결정 필요):
- 핵심 채널 1순위는 무엇인가(블로그/유튜브/뉴스레터/인스타 등)
- "코치/강사 브랜드"를 전면에 둘지, "책"을 전면에 둘지

---

## 6) 확장 아이템 후보 검토 (전체 완료 후)

목표(Level 0):
- "다음 확장 아이템" 후보를 3~5개로 뽑고, 우선순위를 정한다.

평가 기준(초안):
- 타깃 독자 적합성: `assets/target_audience.md`의 제약(시간/불안/실행 단위)과 맞는가
- 책과의 연결: 책의 어떤 챕터를 재사용/강화하는가
- 제작 난이도/유지 비용: 꾸준히 운영 가능한가
- 리스크: 과장/공포/오해를 키우지 않는가

후보 예시(확정 전):
- 뉴스레터 12주 과정(요약+실행)
- 웨비나 월 1회(Q&A)
- 워크시트 번들(인벤토리/리밸런싱/자동이체)
- 온라인 강의(녹화)

---

## 7) 다음 액션 (가장 작은 1단계)

최우선은 책 원고 99% 게이트 통과다:
- Round 2-2: Sources가 없는 챕터 중 수치/인용/철학 설명이 있는 장의 최소 출처 보강 범위를 먼저 확정한다.
- 병행 가능 큐: 전체 책 기반 Google Slides 메시지 맵을 작성한다. 단, 실제 최종 슬라이드 제작은 원고 99% 게이트 이후로 둔다.
