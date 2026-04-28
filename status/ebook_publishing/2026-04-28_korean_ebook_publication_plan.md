# Korean Ebook Publication Plan: 2026-04-28

## Verdict

- status: READY_FOR_PUBLICATION_PREP
- primary_goal: 국내 전자책 플랫폼 출간
- recommended_format: EPUB3 리플로우
- secondary_format: PDF는 필요 시 별도 상품/별도 ISBN 검토
- recommended_route: e퍼플 1순위 대행·셀프 플랫폼 경로 검토, 이후 직접 출판사 경로 확장
- parallel_tracks: 강연, 코칭, 블로그 준비와 병행 가능

## Why This Track Matters

현재 원고는 Markdown 중심으로 정리되어 있고, completion audit Round 3 기준 `97.1`까지 올라왔다. 하지만 시장에 나가는 전자책은 단순히 `.md`를 `.epub`으로 바꾼 파일이 아니다. 실제 상품으로 팔리려면 다음 요소가 필요하다.

- EPUB/PDF 파일 자체의 기술 검수
- 표지, 판권면, 목차, 메타데이터
- ISBN 또는 플랫폼 대행 ISBN 경로
- 전자책 납본
- 유통사 상품 페이지용 소개/키워드/카테고리
- 재무/투자 분야의 오해 방지 문구
- 모바일 뷰어와 TTS 환경에서의 가독성

## Current Research Summary

### ISBN / 발행자번호

국립중앙도서관 ISBN·ISSN·UCI·납본 시스템은 처음 도서를 출판하는 발행처가 발행자번호를 받은 뒤 도서번호를 신청하는 흐름을 안내한다. 발행자번호 FAQ는 온라인 신청, 출판사신고확인증 첨부, 업무일 기준 3일 이내 배정, 배정 후 ISBN 신청 가능이라는 절차를 제시한다.

Implication:
- 직접 출판사 경로라면 발행자번호와 ISBN 준비가 선행된다.
- 대행 플랫폼 경로라면 ISBN을 누가 발급/관리하는지 계약 조건을 확인해야 한다.

### 전자책 납본

국립중앙도서관 온라인 자료 납본 안내는 ISBN을 부여받은 전자책을 납본 대상으로 안내한다. 납본 제도 안내는 국제표준자료번호를 부여받은 온라인 자료를 발행/제작한 경우 발행일 또는 제작일로부터 30일 이내 납본해야 한다고 설명한다.

Implication:
- 출간일을 정하면 납본 마감일도 함께 잡아야 한다.
- EPUB 파일, 서지정보, 필요 시 납본서/보상청구서 흐름을 체크해야 한다.

### EPUB 기술 기준

W3C EPUB 3.3은 EPUB를 구조화된 웹 콘텐츠를 단일 파일 컨테이너로 배포하는 포맷으로 정의한다. EPUBCheck는 EPUB 출판물 적합성 검사 도구다. Pandoc은 EPUB metadata에서 cover-image, css, accessibility 관련 필드를 지원한다.

Implication:
- 이 책은 텍스트 중심이므로 리플로우 EPUB3가 기본이다.
- `pandoc -> epubcheck -> 뷰어 QA` 파이프라인이 적합하다.

### 국내 유통 경로

교보문고 바로출판 안내에 따르면 POD는 개인도 접근하기 쉽지만, 전자책 계약·출간은 ISBN 발급이 가능한 출판사 중심이며 개인 저자는 제휴사를 통한 진행을 안내한다. e퍼플 FAQ는 일정 분량 이상의 완성 원고에 대해 전자책 무료 제작·유통 경로를 안내한다. YES24/교보/리디 등 실제 전자책 상품 페이지는 EPUB/PDF 형식, DRM, TTS, 지원기기, ISBN, 글자 수/파일 용량을 노출한다.

Implication:
- 직접 모든 서점과 계약하는 경로보다, 초기에는 유페이퍼/e퍼플/부크크 같은 전자책 유통 대행 경로를 검토하는 것이 실행 비용이 낮다.
- 현재 1차 후보는 e퍼플이다. 다만 `무료`가 선결제 없음인지, 판매 후 공제인지, 정산율에 포함된 구조인지는 계약 전 확인한다.
- 장기적으로 자체 출판사/사업자 경로를 열면 정산·브랜딩·유통 통제력이 올라간다.

## Publication Route Options

| Route | 설명 | 장점 | 리스크 | 추천도 |
|---|---|---|---|---|
| A. 대행·셀프 플랫폼 우선 | 유페이퍼/e퍼플/부크크 등에서 제작·ISBN·유통 일부 대행 가능성 확인 | 빠름, 행정 부담 낮음, 테스트 출간에 적합 | 수수료/정산/브랜딩 통제 제한 | 1차 추천 |
| B. 자체 출판사 직접 유통 | 출판사 신고, 사업자, 발행자번호, ISBN, 서점 계약 직접 처리 | 장기 브랜드 자산, 통제력 높음 | 절차 많음, 계약/정산/납본 직접 관리 | 2차 확장 |
| C. PDF 직접 판매 | 크몽/탈잉/자체몰 등에서 PDF 판매 | 빠름, ISBN 없이도 가능할 수 있음 | 정식 서점 전자책 상품성과 다름, DRM/TTS 약함 | 보조 |

## Recommended Route

1차는 `A. 대행·셀프 플랫폼 우선`이 현실적이다. 그중 e퍼플을 먼저 확인한다. 이유는 원고와 강연/코칭/블로그를 병행해야 하므로 행정·유통 계약을 한 번에 크게 벌리기보다, EPUB 품질과 상품 메타데이터를 먼저 완성하는 편이 낫기 때문이다.

단, 장기적으로 이 책을 시리즈화하거나 강연/코칭 대표 상품의 기반 도서로 운영하려면 `B. 자체 출판사 직접 유통`도 병행 검토한다.

## MD to Market-Ready Ebook Pipeline

### 1. Source Freeze

- `chapters/` 원고를 출간 후보본으로 freeze한다.
- status 문서, audit 문서, 강연/코칭 자료는 EPUB에 포함하지 않는다.
- 표지: `chapters/images/cover_b_v2.png`
- 이미지: 본문에서 참조하는 이미지만 포함한다.

### 2. Ebook Manuscript Assembly

권장 출력 구조:

```text
build/ebook/
  manuscript.md
  metadata.yaml
  ebook.css
  assets/
dist/ebook/
  moneygame_survival_guide.epub
  moneygame_survival_guide.pdf
  validation/
```

통합 원고에는 다음 순서를 권장한다.

1. 표지
2. 판권면
3. 책소개 또는 프롤로그 전 안내
4. 목차
5. 프롤로그
6. 1~14장
7. Sources 또는 참고자료
8. 저자 소개

### 3. Formatting Rules for EPUB

- H1은 장 제목으로만 사용한다.
- 체크인/레벨업 질문의 `---` 구분선은 EPUB에서 과도하게 보이면 CSS로 간격 처리한다.
- GitHub Alert 문법은 EPUB HTML에서 깨질 수 있으므로 일반 blockquote 또는 박스 스타일로 변환한다.
- 표가 넓은 장은 모바일에서 깨질 수 있으므로, 핵심 표는 축소하거나 이미지/세로형 표/부록형으로 재구성한다.
- 외부 링크는 유지하되, 독자가 오프라인으로 읽어도 핵심 의미가 남도록 문장 자체가 완결되어야 한다.
- 모든 이미지에는 alt text가 필요하다.

### 4. EPUB Build

초기 권장 도구:

```bash
pandoc build/ebook/manuscript.md \
  --from markdown+yaml_metadata_block \
  --to epub3 \
  --toc \
  --toc-depth=2 \
  --metadata-file build/ebook/metadata.yaml \
  --css build/ebook/ebook.css \
  --epub-cover-image chapters/images/cover_b_v2.png \
  -o dist/ebook/moneygame_survival_guide.epub
```

검증:

```bash
epubcheck dist/ebook/moneygame_survival_guide.epub
```

EPUBCheck 오류 0개가 1차 게이트다.

### 5. Viewer QA

- Thorium Reader: 목차/이미지/표/링크 확인
- 교보 eBook 앱 또는 웹뷰어: 한글 줄바꿈, 표, TTS 흐름 확인
- YES24 크레마 앱: 목차, 이미지, DRM 적용 후 흐름 확인
- 리디 앱: 경제/경영 카테고리 상품처럼 보이는지 확인
- 모바일 좁은 화면: 표와 코드블록이 가로 스크롤 없이 읽히는지 확인

### 6. Metadata Package

필수 초안:

| Field | Draft |
|---|---|
| 제목 | 부의 게임, 대충 뛰어들어 끝까지 살아남기 |
| 부제 | 경제적 자유를 향한 따뜻하고 대충 합리적인 생존 가이드 |
| 저자 | TBD |
| 발행처 | TBD |
| 형식 | EPUB3 |
| 카테고리 | 경제/경영 > 재테크/투자 또는 자기계발 > 성공/처세와 비교 검토 |
| 키워드 | 재테크, 경제적 자유, 투자 심리, 자산 배분, 복리, 현금흐름, 인덱스 ETF |
| 가격 | 6,900원 1차 추천. 프로모션가는 4,900원~5,900원 후보 |
| DRM | 플랫폼 기본 DRM 적용 권장 |
| TTS | 가능하면 허용 권장. 이미지형 PDF보다 텍스트 EPUB 우선 |
| 미리보기 | 프롤로그 + 1장 일부 또는 1장 전체 후보 |

### 7. Listing Copy Needed

- 50자 소개
- 300~500자 책소개
- 1000~1500자 상세 소개
- 저자 소개
- 목차
- 독자 대상
- 이 책이 해결하는 문제
- 투자 조언 아님/교육 목적 문구

## 8-Week Execution Plan

| Week | Goal | Output |
|---:|---|---|
| 1 | 출판 경로 결정 | 대행 플랫폼 2~3곳 비교표, 직접 출판사 경로 체크 |
| 2 | 전자책 패키지 설계 | metadata 초안, 판권면 초안, 면책 문구 |
| 3 | MD 통합 원고 생성 | `build/ebook/manuscript.md` |
| 4 | EPUB 1차 생성 | `dist/ebook/*.epub`, EPUBCheck 1차 로그 |
| 5 | 모바일/뷰어 QA | QA 리포트, 표/이미지 수정 목록 |
| 6 | 상품 메타데이터 완성 | 책소개/저자소개/키워드/가격 후보 |
| 7 | 플랫폼 등록 준비 | ISBN/대행 계약/유통 등록 자료 |
| 8 | 등록/검수/납본 준비 | 플랫폼 제출, 납본 체크리스트 |

## Parallel Work With Other Tracks

- 강연 준비: 책소개 문구, 독자 대상, 핵심 메시지, handout을 전자책 상세페이지와 공유한다.
- 코칭 프로그램: 6장/9장/14장의 실행 템플릿을 부가 자료로 확장하되, 전자책 본문과 충돌하지 않게 한다.
- 블로그 글쓰기: 전자책 출간 전후로 챕터별 teaser 글을 발행한다.
- 마케팅: 표지, 50자 소개, 300자 소개, 목차 이미지를 공용 자산으로 만든다.

## Immediate Next Actions

1. 출판 경로 비교표 작성: `status/ebook_publishing/2026-04-28_route_comparison.md` (완료)
2. 전자책 메타데이터 초안 작성: `status/ebook_publishing/2026-04-28_metadata_draft.md` (완료: 저자명, 1차 경로, 정가 후보 반영)
3. EPUB 빌드 가능성 확인 및 Homebrew 설치: `pandoc 3.9.0.2`, `EPUBCheck 5.3.0` 사용 가능 (완료: `status/ebook_publishing/2026-04-28_toolchain_check.md`)
4. 1차/2차/보조 실행 보드 작성: `status/ebook_publishing/2026-04-28_route_execution.md` (완료)
5. `build/ebook/`와 `dist/ebook/` 출력 정책 확정: `status/ebook_publishing/2026-04-28_ebook_build_structure.md` (완료)
6. 플랫폼 제출용 listing copy 초안 작성: `status/ebook_publishing/2026-04-28_listing_copy_draft.md` (완료)
7. `metadata.yaml`과 `ebook.css` 초안 작성
8. 전자책용 판권면/면책 문구 초안 작성
9. e퍼플 가입/신청 화면 기준으로 무료 제작·유통 조건 확인
10. 저자 소개와 상품 페이지 문구 확정

## Sources

- National Library of Korea ISBN·ISSN·UCI·Legal Deposit System: https://www.nl.go.kr/seoji/
- National Library of Korea, 발행자번호 FAQ: https://www.nl.go.kr/seoji/contents/S20301000000.do?id=63&page=2&schBcid=FAQ_ISBN&schFld=bd_title&schM=view
- National Library of Korea, 온라인 자료(전자책 등 단행본) 납본 안내: https://www.nl.go.kr/seoji/contents/S50102010000.do
- National Library of Korea, 자료의 납본 제도 안내: https://nl.go.kr/seoji/contents/S20102010000.do
- Kyobo Book Centre, 바로출판 POD 서비스 소개: https://product.kyobobook.co.kr/pod/introduce
- e퍼플 FAQ: https://www.epubple.com/home/faq
- e퍼플 작가 안내: https://www.epubple.com/home/writer
- W3C, EPUB 3.3: https://www.w3.org/TR/epub-33/
- W3C/DAISY, EPUBCheck: https://github.com/w3c/epubcheck
- EPUBCheck running guide: https://w3c.github.io/epubcheck/docs/running/
- Pandoc EPUB metadata documentation: https://pandoc.org/demo/example33/11.1-epub-metadata.html
