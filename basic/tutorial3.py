# 뉴스 제목과 링크 가져오기

import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=애플")
html = response.text

soup = BeautifulSoup(html, "html.parser") 
links = soup.select(".news_tit") # html 페이지에서 10개가 있어서 10개가 print 될거임, 그리고 리스트임
#print(links)
print(len(links))

for link in links:
    title = link.text # 태그 안의 텍스트 요소만 뽑아옴
    url = link.attrs['href'] # 원본 링크 담기 -> 요 부분 암기!!
    print(title, url)