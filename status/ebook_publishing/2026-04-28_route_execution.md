# Ebook Route Execution Board: 2026-04-28

## Decision

- primary_route: e퍼플 1순위 대행·셀프 플랫폼 출간
- secondary_route: 자체 출판사/직접 유통은 1차 출간 이후 확장 검토
- support_route: 강연/코칭용 PDF handout 또는 workbook은 별도 보조 상품으로 운영
- list_price_candidate: 6,900원
- public_author_display_candidate: 최호석(호호코치)

## Execution Principles

1차 목표는 `시장에 나갈 수 있는 정식 전자책 패키지`를 만드는 것이다. 플랫폼 가입, 본인 인증, 계약 동의, 정산 정보 입력은 저자 본인이 처리한다. 원고 통합, EPUB 준비, 상품 문구, 검수표, 계약 확인 질문지는 Codex가 준비한다.

e퍼플은 공식 안내에서 무료 제작, ISBN 무료발급, 온라인 서점 유통, 판매가 기준 40% 인세, 5만원 이상 적립 시 지급 조건을 제시한다. 단, 실제 신청 화면과 계약서가 최종 기준이다. 따라서 무료 제작은 `선결제 없음`으로 이해하되, 수정 비용, 판매 후 정산 구조, 유통 범위, 계약 기간은 제출 전에 확인한다.

## Track A. 1차 실행: e퍼플 출간 패키지

### A1. 플랫폼 조건 확인

| Item | Owner | Status | Output |
|---|---|---|---|
| e퍼플 회원가입 가능 여부 확인 | Author | not started | 계정 생성 또는 로그인 가능 상태 |
| 저자 정산 정보 요구 항목 확인 | Author | not started | 계좌/세금/본인 인증 필요 항목 목록 |
| 무료 제작 조건 확인 | Author + Codex | prepared | 계약 확인 질문지 |
| ISBN 발급 주체 확인 | Author + Codex | prepared | e퍼플 ISBN 사용 여부 |
| 수정판 업로드 비용 확인 | Author + Codex | prepared | 수정 비용/횟수 조건 |
| 서점 유통 범위 확인 | Author + Codex | prepared | 교보/YES24/알라딘/리디 포함 여부 |

### A2. 제출 자료 패키지

| Asset | Owner | Status | Notes |
|---|---|---|---|
| 원고 최종 MD freeze | Codex | not started | `chapters/` 기준 출간 후보본 고정 |
| 통합 원고 | Codex | not started | `build/ebook/manuscript.md` 후보 |
| 표지 파일 | Codex | ready | `chapters/images/cover_b_v2.png` |
| 저자명 | Author | draft | `최호석(호호코치)` 추천 |
| 정가 | Author | draft | `6,900원` 추천 |
| 책소개 50자 | Codex | draft | [2026-04-28_listing_copy_draft.md](2026-04-28_listing_copy_draft.md) |
| 책소개 300~500자 | Codex | draft | [2026-04-28_listing_copy_draft.md](2026-04-28_listing_copy_draft.md) |
| 상세 소개 1000~1500자 | Codex | draft | [2026-04-28_listing_copy_draft.md](2026-04-28_listing_copy_draft.md) |
| 저자 소개 | Author + Codex | waiting input | 이력/톤 입력 필요 |
| 키워드 | Codex | draft | metadata 문서 후보 |
| 카테고리 | Codex | draft | 경제/경영 > 재테크/투자 우선 |
| 미리보기 범위 | Author + Codex | not started | 프롤로그 + 1장 일부 후보 |
| 면책 문구 | Codex | draft | metadata 문서 후보 |

### A3. EPUB 품질 게이트

| Gate | Owner | Status | Pass Criteria |
|---|---|---|---|
| Pandoc 설치 또는 대체 빌드 방식 결정 | Codex | completed | `pandoc 3.9.0.2` 실행 가능 |
| EPUBCheck 설치 또는 jar 확보 | Codex | completed | `EPUBCheck v5.3.0` 실행 가능 |
| EPUB 1차 생성 | Codex | pending | `.epub` 생성 |
| EPUBCheck 검증 | Codex | pending | error 0 |
| 뷰어 QA | Author + Codex | pending | 목차, 이미지, 표, 링크, TTS 흐름 확인 |
| 제출 전 체크리스트 | Codex | pending | 플랫폼 업로드 전 누락 0 |

## Track B. 2차 실행: 자체 출판사/직접 유통 확장

이 트랙은 1차 출간 이후 판매 반응, 후속 시리즈 계획, 강연/코칭 대표 상품화 여부가 확인된 뒤 진행한다. 지금 당장은 행정 작업을 시작하지 않고, 결정 조건만 관리한다.

| Trigger | Meaning | Action |
|---|---|---|
| 전자책 판매가 꾸준히 발생 | 자체 브랜드 출판의 효용이 생김 | 출판사 신고/사업자 경로 검토 |
| 후속권 또는 워크북 계획 확정 | ISBN/브랜드 통제 필요성 증가 | 발행자번호 신청 준비 |
| 강연/코칭에서 책이 대표 상품이 됨 | 유통/정산/브랜딩 통제력 중요 | 직접 유통사 계약 가능성 조사 |
| e퍼플 수정/정산/브랜딩 제약이 커짐 | 대행 경로 한계 발생 | 자체 출판사 전환 시점 검토 |

2차 트랙의 보류 작업:
- 출판사명 후보 작성
- 사업자등록 필요 여부 확인
- 국립중앙도서관 발행자번호 신청 요건 확인
- EPUB/PDF/종이책별 ISBN 운영 정책 수립
- 납본 책임 주체 재정의

## Track C. 보조 실행: PDF Handout / Workbook

보조 상품은 정식 전자책을 대체하지 않는다. 강연과 코칭에서 독자가 직접 적고 실행하는 자료로 분리한다.

| Candidate | Source Chapters | Use Case | Status |
|---|---|---|---|
| 60분 강연 handout | 프롤로그, 1장, 5장, 6장, 9장, 10장, 14장 | 강연 참석자 배포 | slide planning 문서와 연결 가능 |
| 재무 인벤토리 workbook | 3장, 5장, 6장, 9장, 13장 | 코칭 사전 과제/후속 과제 | 별도 PDF 후보 |
| 블로그 teaser PDF | 1장, 5장, 10장 | 출간 전 이메일/블로그 리드마그넷 | 보조 마케팅 후보 |

PDF 보조 상품 기준:
- 정식 전자책 본문을 그대로 복제하지 않는다.
- 체크리스트, 질문지, 워크시트 중심으로 구성한다.
- ISBN이 필요한 정식 판매물인지, 무료 배포 자료인지 먼저 결정한다.
- 투자 조언 오해 방지 문구를 포함한다.

## Contract Check Questions For e퍼플

신청 전 또는 계약 화면에서 다음 질문에 답을 확보한다.

1. ISBN은 e퍼플 명의로 발급되는가, 저자 명의 발행처가 별도로 필요한가?
2. 무료 제작의 범위는 어디까지인가? 표지, EPUB 제작, 유통 등록이 모두 포함되는가?
3. 출간 후 오탈자 수정이나 개정판 업로드에 비용이 발생하는가?
4. 저자 인세는 판매 정가 기준 40%인지, 서점 할인/수수료 반영 후 기준인지?
5. 정산은 몇 개월 뒤 지급되는가? 최소 지급 금액은 얼마인가?
6. 계약 기간은 몇 년이며 자동 연장 조건은 무엇인가?
7. 판매 중단이나 계약 해지 요청 시 처리 기간은 얼마인가?
8. 유통 서점에 교보문고, YES24, 알라딘, 리디북스가 포함되는가?
9. EPUB 파일 원본을 저자에게 제공하는가, 플랫폼 유통 전용으로만 보관하는가?
10. TTS, DRM, 미리보기 범위는 누가 결정하는가?

## Immediate Next Actions

1. Codex: `build/ebook/`와 `dist/ebook/` 출력 구조를 설계한다. (완료: [2026-04-28_ebook_build_structure.md](2026-04-28_ebook_build_structure.md))
2. Codex: 플랫폼 제출용 listing copy 초안을 만든다. (완료: [2026-04-28_listing_copy_draft.md](2026-04-28_listing_copy_draft.md))
3. Author: e퍼플 회원가입/로그인 가능 여부를 확인한다.
4. Author: 계약 화면 또는 FAQ에서 위 질문의 답을 확인한다.
5. Codex: 1차 EPUB를 생성하고 EPUBCheck 결과를 기록한다.

## Sources

- e퍼플 FAQ: https://www.epubple.com/home/faq
- e퍼플 서비스 안내: https://www.epubple.com/home/home.page?cmd=home-service
- e퍼플 회원 약관/가입 화면: https://www.epubple.com/home/user.page?cmd=home-user-join
- e퍼플 작가 안내: https://www.epubple.com/home/writer
- National Library of Korea ISBN·ISSN·UCI·Legal Deposit System: https://www.nl.go.kr/seoji/
