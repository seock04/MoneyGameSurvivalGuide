# Book Illustration Design Audit

작성일: 2026-05-09
범위:
- `chapters/00_표지.md`
- `chapters/00_프롤로그.md`
- `chapters/01_부의_게임_시작하기.md` ~ `chapters/15_에필로그.md`
- `chapters/images/`

## Verdict

- status: ROUND_1_APPLIED
- score: 91/100
- hard_gates: PASS_WITH_PRODUCTION_CAVEATS
- production_mode: ebook-first chapter hero refresh
- final_style_decision: 성인 실용서용 warm editorial watercolor-gouache 스타일을 기준으로, 구형 3:2 hero 중 원고 변화 영향이 큰 프롤로그와 3~7장을 16:9 ebook hero로 교체한다.

## Expert Panel Summary

### Publishing Lead

- Priority judgment: 전면 교체보다 판매·독서 경험에 직접 영향을 주는 대표 이미지의 시리즈감을 먼저 맞추는 편이 효율적이다.
- Must change: 프롤로그와 3~7장 hero는 이전 구조의 흔적과 비율 차이가 커서 ebook 시리즈감 보강이 필요하다.
- Can keep: 1~2장 v2 이미지, 8~15장 최신 이미지, 표지 SVG는 현재 원고 톤과 출판 신뢰 기준에서 유지 가능하다.

### Lead Book Illustrator Final Decision

- Style: 따뜻한 성인 실용서 일러스트. 수채·구아슈 질감, 넉넉한 여백, 읽어야 하는 텍스트 없는 상징 중심, sage green/deep teal/warm neutral 팔레트.
- Production queue: 프롤로그, 3장, 4장, 5장, 6장, 7장 hero를 우선 교체했다.
- Deferred: 표지 PNG/JPG 파생본, 책등/뒷표지, 8~15장 세부 통일 라운드는 최종 ebook/PDF 빌드 단계에서 확인한다.

### Other Expert Notes

- Literature: 새 hero는 각 장의 핵심 비유를 한 장면으로 압축해 장 시작부의 정서 진입을 돕는다.
- Finance safety: 수익 보장, 대박, 폭락 공포, 특정 상품 추천처럼 보이는 요소는 넣지 않았다.
- Coaching: 작은 행동, 점검, 재해석, 방향 설정처럼 독자가 할 수 있는 행동의 감각이 강화되었다.
- Psychology: 부끄러움과 자기비난보다 안전한 관찰과 재시도 분위기를 우선했다.
- Behavioral communication: 게임 메타포는 로그인, 지도, 나침반, 인벤토리 수준으로 낮추고 과한 판타지는 피했다.
- Korean/caption: 이미지 안 텍스트 대신 기존 캡션이 설명을 담당하도록 유지했다.

## Style Direction

- Format: 1672x941 PNG, 16:9 landscape, ebook chapter hero.
- Palette: warm neutral, sage green, deep teal, soft gold.
- Composition: 중앙 행동 1개와 보조 오브젝트 2~4개, 모바일 축소 시에도 핵심 장면이 읽히는 구도.
- Texture: watercolor-gouache editorial texture.
- Character policy: 보통 독자 1명 또는 손/부분 인물 중심. 과장된 성공 이미지 금지.
- Text policy: 이미지 안의 읽어야 하는 텍스트 금지. 설명은 alt/caption/본문으로 처리.
- Game metaphor policy: 장식보다 이해 보조용으로만 사용.
- Avoid: 럭셔리, 돈비, 폭락 화면, 티커, 수익률, 브랜드 로고, 공포 장면, 아동용 판타지.

## Asset Inventory

| 챕터 | 현재 이미지 | 역할 | 현재 적합도 | 결정 | 이유 |
|---|---|---|---:|---|---|
| 표지 | `cover_final_front.svg` | cover | 90 | keep | 텍스트 통제와 출판 신뢰 측면에서 생성 이미지보다 안전하다. |
| 프롤로그 | `ch00_hero.png` | hero | 72 | replace | 구형 스타일과 텍스트성 UI가 남아 있어 성인 ebook hero로 교체했다. |
| 1장 | `ch01_hero_v2.png` | hero | 90 | keep | 현재 시리즈 방향과 잘 맞는다. |
| 2장 | `ch02_hero_v2.png` | hero | 88 | keep | 자동화 메시지와 보조 이미지가 충분하다. |
| 3장 | `ch03_hero.png` | hero | 76 | replace | 5월 9일 흐름 보강 후 돈의 대본 재작성 장면을 더 직접 반영해야 했다. |
| 4장 | `ch04_hero.png` | hero | 76 | replace | 관점 바꾸기/액자 교체 메타포를 더 선명하게 반영했다. |
| 5장 | `ch05_hero.png` | hero | 78 | replace | 나침반 반복 압축 이후 북극성과 목표 설정 중심으로 재정렬했다. |
| 6장 | `ch06_hero.png` | hero | 78 | replace | 현재 좌표와 재무 상태 점검을 비난 없는 책상 장면으로 교체했다. |
| 7장 | `ch07_hero.png` | hero | 78 | replace | 복리의 과장 톤을 낮춘 원고에 맞게 차분한 시간/눈덩이 장면으로 교체했다. |
| 8~15장 | 기존 v1/v2 이미지 | hero/concept | 86~92 | keep | 최신 구조와 대체로 맞아 후속 라운드에서만 미세 조정한다. |

## Production Queue

| 우선순위 | 파일명 | 대상 위치 | 작업 | 핵심 장면 | 상태 |
|---:|---|---|---|---|---|
| 1 | `ch00_hero_ebook_v2.png` | 프롤로그 hero | replace | 작은 로그인/첫 실행 | done |
| 2 | `ch03_hero_ebook_v2.png` | 3장 hero | replace | 돈의 대본 재작성 | done |
| 3 | `ch04_hero_ebook_v2.png` | 4장 hero | replace | 낡은 액자에서 새 액자로 | done |
| 4 | `ch05_hero_ebook_v2.png` | 5장 hero | replace | 북극성, 나침반, 목표 | done |
| 5 | `ch06_hero_ebook_v2.png` | 6장 hero | replace | 현재 재무 좌표 점검 | done |
| 6 | `ch07_hero_ebook_v2.png` | 7장 hero | replace | 복리와 시간의 눈덩이 | done |

## Generated Assets

| 파일 | 삽입 위치 | 프롬프트 | 검증 |
|---|---|---|---|
| `chapters/images/ch00_hero_ebook_v2.png` | `chapters/00_프롤로그.md` | `status/illustrations/prompts/ch00_hero_ebook_v2.txt` | linked |
| `chapters/images/ch03_hero_ebook_v2.png` | `chapters/03_당신의_통장은_죄가_없다_기억이_문제지.md` | `status/illustrations/prompts/ch03_hero_ebook_v2.txt` | linked |
| `chapters/images/ch04_hero_ebook_v2.png` | `chapters/04_아들러_씨의_재무_상담소.md` | `status/illustrations/prompts/ch04_hero_ebook_v2.txt` | linked |
| `chapters/images/ch05_hero_ebook_v2.png` | `chapters/05_지도는_됐고_나침반이나_주세요.md` | `status/illustrations/prompts/ch05_hero_ebook_v2.txt` | linked |
| `chapters/images/ch06_hero_ebook_v2.png` | `chapters/06_당신의_재무_상태를_열어보세요.md` | `status/illustrations/prompts/ch06_hero_ebook_v2.txt` | linked |
| `chapters/images/ch07_hero_ebook_v2.png` | `chapters/07_지속_가능한_성장의_마법.md` | `status/illustrations/prompts/ch07_hero_ebook_v2.txt` | linked |

## Findings

### Critical

- 없음.

### High

- 없음.

### Medium

- location: `chapters/images/cover_final_front.svg`
- issue: 표지는 SVG 원본으로 유지하지만, ebook 플랫폼 제출용 PNG/JPG 파생본은 아직 만들지 못했다.
- recommendation: 최종 ebook 빌드 전 SVG를 1800x2700 이상 PNG/JPG로 내보낸다.

- location: 8~15장 hero/concept 이미지
- issue: 최신 16:9 계열로 대체로 안정적이지만, 이번 라운드의 새 hero와 질감이 완전히 같은지는 최종 ebook 미리보기에서 한 번 더 확인해야 한다.
- recommendation: 다음 라운드에서 8~15장만 대상으로 시리즈감 미세 조정을 검토한다.

### Low

- location: `chapters/images/ch00_hero.png`, `ch03_hero.png` 등
- issue: 교체된 구버전 이미지가 루트에 남아 있다.
- recommendation: 삭제하지 않고 보존하되, 출판 전달 패키지에서는 실제 참조 이미지 목록만 포함한다.

## Validation

- image links: PASS
- markdown diff: PASS
- caption check: PASS, 기존 캡션 유지
- ebook suitability: PASS for generated hero dimensions, 1672x941 PNG

## Next Round

1. 표지 SVG의 ebook 제출용 PNG/JPG 파생본을 만든다.
2. 8~15장 이미지와 새 0/3~7장 hero를 ebook 미리보기에서 나란히 확인한다.
3. 최종 PDF/EPUB 빌드 후 흑백/전자잉크에서 핵심 장면이 유지되는지 확인한다.
