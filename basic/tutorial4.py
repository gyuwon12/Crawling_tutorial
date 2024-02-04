# 검색어를 입력했을 때 헤드라인 쭉 가져오기 (1페이지)

import requests
from bs4 import BeautifulSoup

input_query = input("검색어를 입력하세요: ")

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}")
html = response.text

soup = BeautifulSoup(html, "html.parser") 
links = soup.select(".news_tit") # html 페이지에서 10개가 있어서 10개가 print 될거임, 그리고 리스트임
#print(links)
print(len(links))

for link in links:
    title = link.text # 태그 안의 텍스트 요소만 뽑아옴
    url = link.attrs['href'] # 원본 링크 담기 -> 요 부분 암기!!
    print(title, url)