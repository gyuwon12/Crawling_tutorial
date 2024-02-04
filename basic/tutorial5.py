# 검색어를 입력했을 때 헤드라인 쭉 가져오기 (여러 페이지)
# 우선 URL이 어떻게 변화되는 것을 확인해보자.
# 1페이지 => https://search.naver.com/search.naver?where=news&sm=tab_pge&query=애플&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=85&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1
# 2페이지 => https://search.naver.com/search.naver?where=news&sm=tab_pge&query=애플&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=27&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11
# 3페이지 => https://search.naver.com/search.naver?where=news&sm=tab_pge&query=애플&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=46&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=21
# 4페이지 => https://search.naver.com/search.naver?where=news&sm=tab_pge&query=애플&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=59&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=31
# 5페이지 => https://search.naver.com/search.naver?where=news&sm=tab_pge&query=애플&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=74&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=41
# ...
# 결과 분석 => 가운데 cluster_rank와 맨 뒤의 start = 1 -> 11 -> 21 -> 31 -> 41 -> 51 ...

import requests
from bs4 import BeautifulSoup

input_query = input("검색어를 입력하세요: ")
last_page = int(input("입력할 페이지의 개수를 입력하세요: "))

for i in range(last_page): # 10페이지동안
    page_number = 10 * i + 1 # 1, 11, 21, 31, ...
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}&start={page_number}") # &이 토큰 구분자라 이 토큰이 너무나도 중요함
    html = response.text

    soup = BeautifulSoup(html, "html.parser") 
    links = soup.select(".news_tit") # html 페이지에서 10개가 있어서 10개가 print 될거임, 그리고 리스트임

    for num, link in enumerate(links):
        title = link.text # 태그 안의 텍스트 요소만 뽑아옴
        url = link.attrs['href'] # 원본 링크 담기 -> 요 부분 암기!!
        print(f"article_number: {page_number + num} and Title: {title} / url: {url}")