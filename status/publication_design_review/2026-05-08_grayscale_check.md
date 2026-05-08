# Grayscale Preview Check

작성일: 2026-05-08

범위:
- `chapters/images/cover_final_front.svg`
- `chapters/images/ch07_compound_growth_graph_v1.png`
- `chapters/images/ch11_portfolio_map_v1.png`
- `chapters/images/ch14_inventory_map_v1.png`
- 그 외 챕터 대표 이미지 전반

## Summary

- status: PASS_WITH_FINAL_PDF_CHECK
- 결론: 현재 원고의 핵심 시각 자료는 본문 설명과 캡션을 함께 갖고 있어, 색이 사라져도 핵심 의미가 완전히 사라지는 구조는 아니다.
- 남은 제작 확인: 최종 PDF 조판본에서 실제 흑백 출력 또는 전자잉크 미리보기로 한 번 더 확인한다.

## Checks

| 항목 | 확인 결과 | 판단 |
|---|---|---|
| 표지 원본 | `cover_final_front.svg`는 짙은 녹색 텍스트, 밝은 배경, 굵은 제목 구조를 사용한다. | 흑백에서도 제목 위계가 유지될 가능성이 높다. |
| 7장 복리 그래프 | 본문 표와 캡션이 그래프 의미를 함께 설명한다. | 색상만으로 이해해야 하는 구조는 아니다. |
| 11장 포트폴리오 지도 | 이미지 아래 캡션과 본문에서 자산 역할을 설명한다. | 최종 PDF에서 지도 내부 대비만 추가 확인하면 된다. |
| 14장 인벤토리 지도 | 부록 본문 표가 핵심 정보를 텍스트로 제공한다. | 이미지가 보조 역할이므로 흑백 리스크가 낮다. |
| 긴 데이터 표 | 2026-05-08 패치에서 넓은 표를 좁은 표 단위로 분할했다. | 모바일/흑백 인쇄 모두에서 가독성 위험이 낮아졌다. |

## Notes

- `sips`로 PNG 이미지 크기를 확인했다.
- SVG 표지는 벡터 원본이므로 픽셀 크기 대신 `viewBox 1800x2700` 기준으로 관리한다.
- 실제 색 대비 수치는 최종 PDF나 EPUB 렌더러에서 달라질 수 있으므로, 출판 직전 미리보기 확인은 유지한다.
