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

### 한국부동산원 R-ONE 아파트 매매지수

- source: 한국부동산원 R-ONE `(월) 지역별 매매지수_아파트`.
- official metadata: R-ONE 통계 화면의 hidden parameter에서 `statblId=A_2024_00178`, `statblNm=(월) 지역별 매매지수_아파트`, `wrttimeMinYear=2006`, `wrttimeMaxYear=2026`, `isRegionData=Y`를 확인했다.
- data endpoint check: `POST /r-one/portal/stat/sttsDataPreviewList.do`로 2025.12 종료값을 재확인했다.
- 확인값:
  - 서울 동남권, 2025.12: 215.5
  - 경기, 2025.12: 144.9
- limitation: R-ONE preview endpoint는 현재 설정에서 최근 10개 월 컬럼만 반환했다. 2006.01 시작값은 같은 R-ONE 통계표의 장기 조회값으로 유지하되, 본문은 `평균가격이 아니라 가격지수 비교`, `강남권에 가까운 대체 지표`, `순위표가 아니라 지도`로 보수화해 해석 리스크를 낮춘다.
- result: 최신 출처와 종료값은 확인 완료. 출간 직전에는 R-ONE 화면에서 2006.01 시작값까지 한 번 더 수동 스냅샷 확인하면 된다.

## Sources

- FRED, "South Korean Won to U.S. Dollar Spot Exchange Rate (AEXKOUS)": https://fred.stlouisfed.org/series/AEXKOUS
- Slickcharts, "S&P 500 Total Returns by Year": https://www.slickcharts.com/sp500/returns
- Official Data, "S&P 500 Prices - Current and Historical": https://www.officialdata.org/us-economy/s-p-500-price
- 한국부동산원 R-ONE, "(월) 지역별 매매지수_아파트": https://www.reb.or.kr/r-one/portal/stat/easyStatPage/A_2024_00178.do
