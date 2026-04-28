# Ebook Build Structure: 2026-04-28

## Purpose

이 문서는 `chapters/`의 Markdown 원고를 플랫폼 제출 가능한 EPUB 패키지로 만들기 위한 출력 구조를 정의한다. 실제 파일 생성 전, 어떤 파일이 원천이고 어떤 파일이 빌드 산출물인지 분리해 둔다.

## Recommended Directory Layout

```text
build/ebook/
  manuscript.md
  metadata.yaml
  ebook.css
  assets/
    images/

dist/ebook/
  moneygame_survival_guide.epub
  validation/
    epubcheck_YYYY-MM-DD.md
    viewer_qa_YYYY-MM-DD.md
```

## Source Inputs

| Input | Path | Use |
|---|---|---|
| 표지 | `chapters/images/cover_b_v2.png` | EPUB cover image |
| 목차 | `chapters/00_목차.md` | 책 목차 정리용 |
| 프롤로그 | `chapters/00_프롤로그.md` | 본문 포함 |
| 본문 | `chapters/01_*.md` ~ `chapters/14_*.md` | 본문 포함 |
| 메타데이터 | `status/ebook_publishing/2026-04-28_metadata_draft.md` | `metadata.yaml` 작성 기준 |
| 면책 문구 | `status/ebook_publishing/2026-04-28_metadata_draft.md` | 판권면/안내문 후보 |

## Manuscript Assembly Order

1. 표지
2. 판권면
3. 책소개 또는 시작 안내
4. 목차
5. 프롤로그
6. 1장부터 14장까지 본문
7. Sources 또는 참고자료 안내
8. 저자 소개

## EPUB Conversion Rules

- H1은 각 장 제목에만 사용한다.
- GitHub Alert 문법은 일반 인용구나 CSS 박스로 변환한다.
- 체크인/레벨업 질문의 구분선은 EPUB에서 과해 보이면 CSS 여백으로 대체한다.
- 본문 이미지는 누락 없이 `assets/images/`로 복사한다.
- 모든 이미지에 alt text를 둔다.
- 표는 모바일 가독성을 먼저 본다. 너무 넓은 표는 세로형 목록이나 부록형 표로 변환한다.
- 외부 링크는 유지하되, 링크 없이도 문장 의미가 남아야 한다.

## Metadata YAML Draft

```yaml
title: "부의 게임, 대충 뛰어들어 끝까지 살아남기"
subtitle: "경제적 자유를 향한 따뜻하고 대충 합리적인 생존 가이드"
author:
  - "최호석(호호코치)"
lang: "ko-KR"
date: ""
subject:
  - "재테크"
  - "경제적 자유"
  - "투자 심리"
  - "자산 배분"
  - "복리"
rights: "Copyright © 최호석. All rights reserved."
```

## Build Command Candidate

`pandoc` 설치 후 1차 후보 명령은 다음과 같다.

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

검증 후보:

```bash
epubcheck dist/ebook/moneygame_survival_guide.epub
```

## Blockers

- `pandoc 3.9.0.2` 설치 완료.
- `EPUBCheck 5.3.0` 설치 완료.
- 저자 소개와 최종 상품 소개가 아직 확정되지 않았다.
- e퍼플 제출 시 EPUB 파일 직접 제출이 가능한지, 원고 파일만 제출하는지 확인이 필요하다.

## Next

1. `metadata.yaml`과 `ebook.css` 초안을 만든다.
2. 통합 원고 `build/ebook/manuscript.md`를 만든다.
3. 플랫폼 제출 방식 확인: EPUB 직접 제출인지, hwp/doc 원고 제출인지 확인한다.
4. EPUB 직접 제출 가능하면 `build/ebook/` 구조대로 1차 파일을 만든다.
5. 원고 제출 방식이면 통합 Markdown을 플랫폼 요구 형식으로 변환하는 별도 절차를 만든다.
