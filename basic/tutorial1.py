# Request 라이브러리 사용해보기

import requests

response = requests.get("https://www.naver.com")
html = response.text # 요거 불러오는게 아주 중요함
print(html)