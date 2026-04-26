# Chapter 10 Table Check: 2026-04-27

## Purpose

Round 2 audit에서 남은 High 이슈였던 `chapters/10_거인들의_어깨_위에서_대충_날기.md`의 환율, S&P 500, 부동산 비교 표를 점검한다.

## Checked

### 원/달러 환율 표

- source: FRED `AEXKOUS`, annual, South Korean Won to One U.S. Dollar.
- FRED notes: daily figures average, noon buying rates in New York City.
- 확인값:
  - 1995: 772.6853
  - 1998: 1400.4036
  - 2007: 928.9717
  - 2009: 1274.6252
  - 2014: 1052.2924
  - 2020: 1180.5554
  - 2025: 1421.3963
- result: 본문 반올림값은 유지 가능하다.

### S&P 500 Total Return 표

- source: Slickcharts `S&P 500 Total Returns by Year`.
- 확인값:
  - 1995: 37.58
  - 2000: -9.10
  - 2008: -37.00
  - 2013: 32.39
  - 2020: 18.40
  - 2022: -18.11
  - 2023: 26.29
- result: 본문 표는 유지 가능하다.

### S&P 500 가격지수 비교

- source: Official Data `S&P 500 Historical Prices`, 1월 가격표.
- 확인값:
  - 2006: 1,278.73
  - 2026: 6,929.12
  - 1996: 614.42
- applied:
  - 2006.01~2026.01 상승 배수: 약 5.42배
  - 2006.01~2026.01 연평균 상승률: 약 8.82%
  - 2006~2025 환율 단순 반영 원화 감각: 약 8.07배, 약 11.01%
  - 1996.01~2026.01 상승 배수: 약 11.28배
  - 1996.01~2026.01 연평균 상승률: 약 8.41%
- result: 본문 수치를 위 값으로 갱신했다.

## Partially Checked

### 한국부동산원 R-ONE 아파트 매매지수

- source: 한국부동산원 R-ONE `(월) 지역별 매매지수_아파트`.
- current status: 동적 통계 페이지라 원문 링크는 확인했지만, 자동 추출로 표 값을 재현하지는 못했다.
- current action: 본문 문구는 `평균가격이 아니라 가격지수 비교`, `강남권에 가까운 대체 지표`, `순위표가 아니라 지도`로 보수화되어 있어 유지한다.
- next action: 최종 출간 전 R-ONE에서 같은 기간/지역/지수 기준을 수동 확인한다.

## Sources

- FRED, "South Korean Won to U.S. Dollar Spot Exchange Rate (AEXKOUS)": https://fred.stlouisfed.org/series/AEXKOUS
- Slickcharts, "S&P 500 Total Returns by Year": https://www.slickcharts.com/sp500/returns
- Official Data, "S&P 500 Prices - Current and Historical": https://www.officialdata.org/us-economy/s-p-500-price
- 한국부동산원 R-ONE, "(월) 지역별 매매지수_아파트": https://www.reb.or.kr/r-one/portal/stat/easyStatPage/A_2024_00178.do
