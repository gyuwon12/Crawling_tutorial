# Beautifulsoup 사용 예제
import requests
from bs4 import BeautifulSoup

# 서버에 요청
response = requests.get("https://n.news.naver.com/mnews/article/005/0001628592?sid=100")
html = response.text # 요거 불러오는게 아주 중요함

# html 필요한거 뽑기, Id값이 header인 것을 뽑고, text 내용만 뽑기
soup = BeautifulSoup(html, "html.parser") # 안에다가 html이랑 번역 선생님 넣어주기
word = soup.select_one("#title_area") # select는 여러개, _one은 원하는거 하나 / id는 앞에다가 #을 붙여줘야함. <a> <div>같은 태그들은 # 쓰는거 아님
# class는 . <- 쩜임
print(word) # <h2 class="media_end_head_headline" id="title_area"><span>당정, ‘묻지마 흉기 범죄’에 “가석방 없는 종신형 추진”</span></h2>
print(word.text) # 당정, ‘묻지마 흉기 범죄’에 “가석방 없는 종신형 추진” 부분