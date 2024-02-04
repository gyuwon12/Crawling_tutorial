# 네이버 증권 웹사이트에서 현재가를 크롤링하고 엑셀에 저장하기

# 삼성전자: https://finance.naver.com/item/sise.naver?code=005930 -> ? 뒤에가 태그인데 005930이 삼성전자 종목 번호임

import requests
from bs4 import BeautifulSoup
import openpyxl

# 1) 엑셀 만들기
workbook = openpyxl.Workbook()

# 2) 엑셀 워크 시트 만들기
work_sheet = workbook.create_sheet("종목 정리")

# 3) 데이터 추가하기
work_sheet['A1'] = "종목"
work_sheet['B1'] = "현재가"
work_sheet['C1'] = "시가총액"
work_sheet['D1'] = "잔고수량"
work_sheet['E1'] = "평가금액"
work_sheet['F1'] = "평가손익"
work_sheet['G1'] = "수익률"

url = "https://finance.naver.com/item/sise.naver?code=005930"

trade_list = ['삼성전자', 'SK하이닉스', '카카오뱅크', '현대차', '신한은행']

code_list = [
    "005930", "000660", "323410", "005380", "055550"
]

for i, code in enumerate(code_list):
    url = f"https://finance.naver.com/item/sise.naver?code={code}"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    
    # 현재가
    price = soup.select_one("#_nowVal").text # <strong class="tah p11" id="_nowVal">68,300</strong> 요런 형태, ID를 가져올것
    price = price.replace(",", "")
    
    # 시가 총액
    market_sum = soup.select_one("#_market_sum").text
    market_sum = market_sum + "억" # 18조 1900억
    
    # 엑셀에 현재가 데이터 추가하기
    work_sheet[f"A{i + 2}"] = trade_list[i]
    work_sheet[f"B{i + 2}"] = int(price) # B2, B3, B4 ...
    work_sheet[f"C{i + 2}"] = market_sum
    
    #print(i, price)

# 4) 엑셀 저장하기
workbook.save(r'/Users/gyuwonpark/Desktop/Crawling/기본/종목_정리.xlsx') # r을 붙이면 모두 문자열 취급을 해라 이런 뜻