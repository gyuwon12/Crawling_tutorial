# 네이버 본문 크롤링 결과를 엑셀에 저장하기 

import requests
from bs4 import BeautifulSoup
import time
import openpyxl
from openpyxl.styles import Alignment

input_query = input("검색어를 입력하세요: ")
input_page_num = int(input("페이지 수를 입력하세요: "))

wb = openpyxl.Workbook()
work_sheet = wb.create_sheet(f'{input_query}') # 이건 시트 이름

# 열 너비 조정
work_sheet.column_dimensions['A'].width = 60
work_sheet.column_dimensions['B'].width = 60
work_sheet.column_dimensions['C'].width = 120

work_sheet['A1'] = '뉴스 링크'
work_sheet['B1'] = '뉴스 제목'
work_sheet['C1'] = '뉴스 본문'

count = 0 # 엑셀 저장용

for i in range(input_page_num): # 10페이지동안
    page_number = 10 * i + 1 # 1, 11, 21, 31, ...
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}&start={page_number}") # &이 토큰 구분자라 이 토큰이 너무나도 중요함
    html = response.text

    soup = BeautifulSoup(html, "html.parser") 
    links = soup.select(".info_group") # html 페이지에서 10개가 있어서 10개가 print 될거임, 그리고 리스트로 가져옴
    #print(len(links)) # 10개 담기 성공
    
    for link in links:
        if len(link.select("a")) >= 2:
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
                for p in ps:
                    p.decompose()
                article_content = article_content.text.strip()
            # 나머지는 일반화
            else:
                title = soup.select_one("#title_area").text
                article_content = soup.select_one("#newsct_article").text.strip()
            
            # 엑셀 추가하기
            work_sheet[f'A{count+2}'] = response.url
            work_sheet[f'B{count+2}'] = title
            work_sheet[f'C{count+2}'] = article_content
            # 자동 줄바꿈 기능 설정
            work_sheet[f'C{count+2}'].alignment = Alignment(wrap_text=True)
            count += 1
            time.sleep(0.2) # 안전성을 위하여

# 엑셀 저장
wb.save(f'네이버 뉴스 기사 본문 크롤링.xlsx') # r을 붙이면 모두 문자열 취급을 해라 이런 뜻