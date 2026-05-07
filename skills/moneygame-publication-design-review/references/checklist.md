# Publication Design Checklist

## Score Rubric (100)

1. Cover Market Fit (15)
   - 장르/대상 독자/핵심 약속이 썸네일에서 보인다.
   - 부제와 소개글, 이미지가 같은 메시지를 낸다.

2. Series Consistency (15)
   - 챕터 이미지들이 한 책의 시각 시스템처럼 보인다.
   - 색감, 인물/오브젝트 스타일, 조명, 질감이 크게 흔들리지 않는다.

3. Concept Clarity (15)
   - 이미지가 챕터 핵심 개념을 쉽게 기억하게 한다.
   - 본문과 다른 약속이나 오해를 만들지 않는다.

4. Ebook Readability (15)
   - 모바일 폭에서 이미지 의미가 유지된다.
   - 작은 글자, 복잡한 표, 과도한 디테일이 없다.
   - 캡션과 본문 연결이 자연스럽다.

5. Print Readiness (15)
   - 표지/본문 이미지가 인쇄 가능 수준으로 준비될 수 있다.
   - 흑백 출력에서도 구분이 가능하다.
   - 재단/여백/책등 확장 위험이 식별되어 있다.

6. Layout Rhythm (10)
   - 이미지 위치가 챕터 요약, 체크인 질문, 본문 흐름과 맞다.
   - 이미지가 독서 리듬을 끊지 않고 숨 쉴 공간을 만든다.

7. Financial Safety & Trust (10)
   - 수익 보장, 대박 암시, 공포 마케팅 시각 요소가 없다.
   - 초보 독자를 겁주기보다 차분히 안내한다.

8. Asset Management (5)
   - 이미지 경로가 존재한다.
   - 파일명과 챕터 연결이 명확하다.
   - archive/임시 이미지와 실제 사용 이미지가 구분된다.

## Severity Guide

- Critical: 출판 시 깨짐, 법적/신뢰도 위험, 표지 부적합, 핵심 이미지 누락
- High: 독자 첫인상 훼손, ebook/print 주요 가독성 문제, 스타일 불일치가 큼
- Medium: 특정 챕터 몰입 저하, 캡션/배치/메타포 개선 필요
- Low: 미세한 일관성, 파일명, 보조 캡션, 후순위 개선

## Quick Commands

- 이미지 목록: `rg --files chapters/images`
- 이미지 사용 위치: `rg -n "images/" chapters`
- 누락 파일 후보: 챕터의 `images/...` 경로와 실제 파일 목록 대조
- 이미지 크기 확인: `sips -g pixelWidth -g pixelHeight chapters/images/<file>` (macOS)
