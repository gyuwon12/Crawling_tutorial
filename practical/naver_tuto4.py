# 스포츠 뉴스 크롤링

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
        #print(naver_news_link) # -> https://n.news.naver.com/mnews/article/001/0014121001?sid=106 여기에서 redirection 일어남 -> 그래서 아래 responce.url 을 해주는 것
        response = requests.get(naver_news_link, headers={'User-agent':'Mozila/5.0'}) 
        html = response.text
        soup = BeautifulSoup(html, "html.parser")  # 똑같은거 반복
        # 만약에 연예뉴스 CSS 선택자라면 그에 맞도록
        # https://entertain.naver.com/read?oid=609&aid=0000758185 => 연예 뉴스
        # https://sports.news.naver.com/news.nhn?oid=117&aid=0003759276 => 스포츠 뉴스
        # https://n.news.naver.com/mnews/article/366/0000923560?sid=105 => not 연예, not 스포츠 뉴스
        
        # 1. 연예 뉴스
        if "https://entertain.naver.com" in response.url: 
            title = soup.select_one(".end_tit").text
            article_content = soup.select_one("#articeBody").text.strip()
        # 2. 스포츠 뉴스
        elif "https://sports.news.naver.com" in response.url: 
            title = soup.select_one("h4.title").text
            article_content = soup.select_one("#newsEndContents")
            # 본문 내용에 쓸데없는 div, p 삭제
            divs = article_content.select("div")
            ps = article_content.select("p")
            print(len(divs), len(ps))
            for div in divs:
                div.decompose()
            article_content = article_content.text
            for p in ps:
                p.decompose()
        # 나머지는 일반화
        else:
            title = soup.select_one("#title_area").text
            article_content = soup.select_one("#newsct_article").text.strip()
        
        print(f"{title}:\n {article_content}")
        time.sleep(0.2) # 안전성을 위하여