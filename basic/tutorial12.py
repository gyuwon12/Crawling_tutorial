# 네이버 쇼핑 상품 정보 수집하기 1단계: 검색창 띄워두기

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 너무 빠르게 입력하면 매크로 의심 받아서 자동입력 방지가 필요
import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=ChromeDriverManager().install()) # 알아서 최신 버전 자동 설치
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩될 때까지 5초는 기다린다. 
driver.maximize_window() # 윈도우 최대화
driver.get("https://www.naver.com") # 네이버 쇼핑 페이지

# 검색어(아이폰 14) 입력해서 페이지 넘어가기
search = driver.find_element(By.CSS_SELECTOR, "#query")
search.click()
search.send_keys("아이폰14")
search.send_keys(Keys.ENTER) # 검색 후 엔터를 누르는 과정!

time.sleep(1) # 1초만 대기

# 페이지 끝까지 내리기
for _ in range(7):
    body = driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

# 쇼핑 더보기 눌러서 쇼핑 속 아이폰 14 목록만 쭉 보기
shopping = driver.find_element(By.CSS_SELECTOR, "a.api_more._link") # 쇼핑 더보기
shopping.click()

# 닫기
#driver.quit()
