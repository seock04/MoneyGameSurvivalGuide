---
name: moneygame-korean-ebook-publisher
description: MoneyGameSurvivalGuide 원고를 한국 전자책 시장에 실제 출판하기 위해 EPUB/PDF 제작, ISBN/납본, 국내 플랫폼 유통, 메타데이터, 검수 반려 리스크, 출간 일정과 병행 작업 계획을 점검하고 실행 문서로 남길 때 사용한다.
---

# MoneyGame Korean Ebook Publisher

## Role

한국 전자책 발간 전문가 관점으로 이 책을 실제 유통 가능한 상품으로 만든다. 목표는 "보기 좋은 파일"이 아니라 국내 전자책 플랫폼에 등록, 검수, 판매, 납본까지 갈 수 있는 출판 패키지다.

## Use When

- MD 원고를 EPUB/PDF 전자책 포맷으로 변환하려 할 때
- ISBN, 발행자번호, 출판사/개인 출판 경로, 납본, 유통사 등록 절차를 점검할 때
- 교보문고, YES24, 알라딘, 리디, 유페이퍼/e퍼플/부크크 등 국내 유통 경로를 비교할 때
- 전자책 표지, 판권면, 목차, 메타데이터, 미리보기, 가격, 카테고리, DRM/TTS 여부를 정리할 때
- 강연/코칭/블로그 준비와 병행 가능한 전자책 출간 로드맵을 만들 때

## Required Reads

작업 전 아래를 읽는다.
- `README.md`
- `guides/WRITING_RULES.md`
- `guides/DISPLAY_GUIDE.md`
- `Additionals/RULES.md` (파생 콘텐츠와 병행 계획을 만들 때)
- 최신 `status/completion_audit/`
- 최신 `status/roadmap.md`

외부 제도/플랫폼 요건은 변동 가능성이 있으므로, 실제 계획을 확정할 때는 반드시 현재 웹 자료를 확인한다.

## Workflow

1. 출판 경로를 먼저 분기한다.
   - 직접 출판사 경로: 출판사 신고/사업자/발행자번호/ISBN/유통 계약을 직접 처리한다.
   - 대행·셀프 플랫폼 경로: 유페이퍼, e퍼플, 부크크, 교보 바로출판 등에서 제작/ISBN/유통 일부를 대행할 수 있는지 확인한다.
   - 원고가 투자/재무 분야이므로 검수 리스크와 책임 소재를 보수적으로 본다.

2. 원고 패키징 준비 상태를 점검한다.
   - 표지, 제목, 부제, 저자명, 출판사명/발행처, 판권면, 저작권 문구
   - 목차와 챕터 순서
   - 이미지 경로, alt text, 표/그래프의 모바일 가독성
   - Sources/면책 문구/투자 조언 아님 문구
   - EPUB에 들어갈 원고와 status/작업로그의 분리

3. 전자책 제작 포맷을 결정한다.
   - 본문형 책은 리플로우 EPUB3를 기본 권장한다.
   - PDF는 고정 레이아웃이 꼭 필요하거나 부가 판매 채널용일 때 별도 ISBN/상품으로 분리할지 검토한다.
   - MD 원고는 `build/ebook/`에서 통합 원고로 변환하고, 최종 산출물은 `dist/ebook/`에 둔다.

4. EPUB 제작·검증 파이프라인을 제안한다.
   - metadata 파일, CSS, cover image, 통합 원고를 준비한다.
   - Pandoc 또는 Sigil/Calibre 기반으로 EPUB를 생성한다.
   - EPUBCheck로 오류 0개를 목표로 검증한다.
   - Thorium/교보/YES24/리디/알라딘 뷰어에서 목차, 이미지, 표, 링크, TTS 흐름을 확인한다.

5. 국내 출판 행정 체크를 한다.
   - 발행자번호/ISBN 신청 가능 상태
   - EPUB와 PDF를 모두 팔 경우 ISBN 분리 필요 여부
   - 발행일 이후 납본 기한과 온라인자료 납본 절차
   - 전자책 파일, 서지정보, 납본서/보상청구서 여부

6. 유통 등록 체크를 한다.
   - 상품명, 부제, 저자소개, 책소개, 목차, 카테고리, 키워드, 가격, DRM/TTS/인쇄 제한, 미리보기 범위
   - 표지 규격과 파일 용량
   - 재무/투자 카테고리에서 과장 광고, 수익 보장, 직접 상품 추천처럼 읽히는 문구 제거

7. 산출물을 남긴다.
   - 실행 계획: `status/ebook_publishing/YYYY-MM-DD_*.md`
   - 제작 체크리스트: `status/ebook_publishing/*checklist*.md`
   - 메타데이터 초안: `status/ebook_publishing/*metadata*.md`
   - 실제 빌드 파일은 별도 요청 전까지 만들지 않는다.

## Quality Gates

- EPUBCheck 오류 0개
- 본문 이미지 링크 누락 0개
- 목차 클릭 이동 정상
- 표/코드블록/인용/알럿이 모바일에서 깨지지 않음
- 투자 수익 보장/직접 매수 권유/공포 마케팅 문구 없음
- ISBN/납본/유통 등록에 필요한 메타데이터 필드가 비어 있지 않음

## References

상세 체크리스트와 현재 기준 출처는 필요 시 읽는다.
- `skills/moneygame-korean-ebook-publisher/references/checklist.md`
- `skills/moneygame-korean-ebook-publisher/references/current_sources.md`
