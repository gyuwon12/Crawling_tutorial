# 검색어를 입력했을 때 네이버 뉴스 링크들 다 가져오기

import requests
from bs4 import BeautifulSoup

input_query = input("검색어를 입력하세요: ")

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}")
html = response.text

soup = BeautifulSoup(html, "html.parser") 
links = soup.select(".info_group") # html 페이지에서 10개가 있어서 10개가 print 될거임, 그리고 리스트로 가져옴
#print(len(links)) # 10개 담기 성공

# 1단계: a 태그가 2개 이상인 것 골라내기 / 거기에서 href 뽑기
naver_news_link = []

for link in links:
    if len(link.select("a")) >= 2:
        naver_news_link.append(link.select("a.info")[1].attrs['href']) # 9개 담기 성공
         
#print(len(naver_news_link)) #-> 9개 잘 담기고
#print(naver_news_link[0]) #-> https://n.news.naver.com/mnews/article/366/0000923560?sid=105 요렇게 잘 나오고