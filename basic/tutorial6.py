# 네이버 증권 웹사이트에서 현재가를 크롤링하기

# 삼성전자: https://finance.naver.com/item/sise.naver?code=005930 -> ? 뒤에가 태그인데 005930이 삼성전자 종목 번호임

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=005930"

# 종목 코드 리스트 - 삼성전자, SK하이닉스, 카카오뱅크, 현대차, 신한은행
code_list = [
    "005930", "000660", "323410", "005380", "055550"
]

for code in code_list:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal") # <strong class="tah p11" id="_nowVal">68,300</strong> 요런 형태, ID를 가져올것
    price = price.text # 68,300과 같이 ,형태의 문자열
    price = price.replace(",", "")

    print(price)
