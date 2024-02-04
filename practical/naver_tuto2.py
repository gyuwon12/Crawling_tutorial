# 검색어를 입력했을 때 네이버 뉴스 링크들 다 가져온 후 본문 크롤링

import requests
from bs4 import BeautifulSoup
import time

input_query = input("검색어를 입력하세요: ")

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}")
html = response.text

soup = BeautifulSoup(html, "html.parser") 
links = soup.select(".info_group") # html 페이지에서 10개가 있어서 10개가 print 될거임, 그리고 리스트로 가져옴
#print(len(links)) # 10개 담기 성공

for link in links:
    if len(link.select("a")) == 2:
        naver_news_link = link.select("a.info")[1].attrs['href'] # 9개 담기 성공
        # 다시 requets 보내기
        # 근데 그냥 불러오면 naver에서 bot으로 인지해서 headers 추가
        response = requests.get(naver_news_link, headers={'User-agent':'Mozila/5.0'}) 
        html = response.text
        soup = BeautifulSoup(html, "html.parser")  # 똑같은거 반복
        #print(soup) -> 잘 나옴
        article_content = soup.select_one("#newsct_article")
        time.sleep(0.2) # 안전성을 위하여
        #print(article_content.text) # -> 다 정상적으로 들어옴