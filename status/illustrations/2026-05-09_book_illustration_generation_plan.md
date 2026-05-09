# Book Illustration Generation Plan

작성일: 2026-05-09
상태: ROUND_1_DONE

## 확정 스타일

출판 전문가 의견을 우선 반영해, 전체 책 일러스트는 `성인 실용서용 warm editorial watercolor-gouache` 방향으로 확정한다. 게임 메타포는 로그인, 나침반, 인벤토리, 지도처럼 이해를 돕는 오브젝트로만 사용하고, 과한 판타지 장식이나 성공 과시는 제외한다.

## Round 1 생성 완료

| 챕터 | 생성 파일 | 원고 반영 | 목적 |
|---|---|---|---|
| 프롤로그 | `chapters/images/ch00_hero_ebook_v2.png` | 완료 | 심리적 지연에서 작은 첫 실행으로 진입 |
| 3장 | `chapters/images/ch03_hero_ebook_v2.png` | 완료 | 돈의 기억과 마음속 대본 재작성 |
| 4장 | `chapters/images/ch04_hero_ebook_v2.png` | 완료 | 관점 바꾸기와 액자 교체 |
| 5장 | `chapters/images/ch05_hero_ebook_v2.png` | 완료 | 북극성, 나침반, 재무목표 |
| 6장 | `chapters/images/ch06_hero_ebook_v2.png` | 완료 | 현재 좌표와 재무 상태 점검 |
| 7장 | `chapters/images/ch07_hero_ebook_v2.png` | 완료 | 복리와 시간의 차분한 눈덩이 |

## 보류 항목

1. 표지 래스터 파생본
   - 현재 원고는 `cover_final_front.svg`를 사용한다.
   - ebook 플랫폼 제출용으로는 1800x2700 이상 PNG/JPG 파생본이 필요할 수 있다.
   - 이번 라운드에서 `sips`는 SVG 변환을 지원하지 않았고, `qlmanage`는 샌드박스 문제로 실행하지 못했다.

2. 8~15장 미세 조정
   - 최신 이미지들은 현재 원고와 대체로 맞아 유지한다.
   - 새 0/3~7장 hero와 나란히 본 뒤 색 온도나 질감 차이가 크면 다음 라운드에서 제한적으로 교체한다.

3. 종이책 확장
   - 책등과 뒷표지는 판형, 페이지 수, 인쇄소 규격 확정 뒤 제작한다.

## 검증

- 새 hero 6개는 모두 1672x941 PNG다.
- 원고 이미지 링크 검산을 통과했다.
- `git diff --check`를 통과했다.
- 이미지 안에는 읽어야 하는 본문 텍스트를 넣지 않았다.
