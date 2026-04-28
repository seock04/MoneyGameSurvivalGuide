# Ebook Toolchain Check: 2026-04-28

## Checked Commands

| Tool | Result | Meaning |
|---|---|---|
| `brew` | available: `/opt/homebrew/bin/brew` | Homebrew 설치 경로 확인 |
| `pandoc` | installed: `3.9.0.2` | EPUB3 자동 빌드 가능 |
| `epubcheck` | installed: `5.3.0` | EPUB 적합성 검증 가능 |
| `openjdk` | installed by Homebrew: `25.0.2` | `epubcheck` 의존성으로 설치됨 |
| `java -version` | system runtime not linked | 전역 Java는 아직 인식되지 않지만 `epubcheck` 명령은 정상 실행됨 |

## Decision

선택지는 `Option A. Homebrew 설치`로 확정했다.

설치 완료:

```bash
brew install pandoc epubcheck
```

설치 결과:

```text
pandoc 3.9.0.2
EPUBCheck v5.3.0
openjdk 25.0.2
```

## Recommendation

전자책 빌드 툴체인은 준비되었다. 이제 `build/ebook/` 통합 원고를 만들고, 첫 EPUB를 생성한 뒤 EPUBCheck 결과를 기록한다.

### Selected Option A. Homebrew 설치

```bash
brew install pandoc
brew install epubcheck
```

장점:
- 명령이 단순하다.
- 반복 빌드/검증에 적합하다.

상태:
- completed

### Option B. EPUBCheck jar 직접 사용

상태:
- not needed

### Option C. GUI 보조

- Sigil로 EPUB 수동 편집/검수
- Thorium Reader로 뷰어 QA

장점:
- 최종 화면 확인에 유리하다.

상태:
- later, viewer QA 단계에서 검토

## Next

1. `build/ebook/` 통합 원고 생성 스크립트 또는 수동 빌드 절차 작성
2. `metadata.yaml`과 `ebook.css` 초안 작성
3. 첫 EPUB 생성
4. `epubcheck dist/ebook/moneygame_survival_guide.epub` 실행
5. 결과를 `status/ebook_publishing/*validation*.md`에 기록
