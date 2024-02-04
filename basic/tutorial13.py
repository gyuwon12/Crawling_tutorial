# 네이버 쇼핑 상품 정보 수집하기 2단계: 정보 가져와서 엑셀에 저장하기

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
driver.get("https://shopping.naver.com/home") # 네이버 쇼핑 페이지

# 검색어(아이폰 14) 입력해서 페이지 넘어가기
search = driver.find_element(By.XPATH, r'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
search.click()
time.sleep(1) # 1초만 대기
search.send_keys("아이폰14")
time.sleep(1) # 1초만 대기
search.send_keys(Keys.ENTER) # 검색 후 엔터를 누르는 과정!

# 스크롤 전 높이 확인
before_h = driver.execute_script("return window.scrollY") # 0 이겠지

# 무한 스크롤
while True:
    # 맨 아래로 스크롤
    body = driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.END)
    # 페이지 과부하 안걸리도록
    time.sleep(1)
    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY") # 현재 스크롤 높이를 저장 -> 0이겠지 처음엔

    if before_h == after_h:
        break
    # 계속 업데이트
    before_h = after_h
    
# 상품 정보 가져오기 -> list 형태로 담기게 됨
ad_list = driver.find_elements(By.CLASS_NAME, "adProduct_info_area__dTSZf") # 광고는 6개
basic_list = driver.find_elements(By.CLASS_NAME, "product_info_area__xxCTi")  # 노광고는 40개

print(len(ad_list), len(basic_list))

ad_item_name = []
ad_item_price = []
ad_item_link = []
basic_item_name = []
basic_item_price = []
basic_item_link = []

for element in ad_list:
    name = element.find_element(By.CLASS_NAME, "adProduct_title__amInq").text
    price = element.find_element(By.CLASS_NAME, "price_num__S2p_v").text
    link = element.find_element(By.CLASS_NAME, "adProduct_title__amInq > a").get_attribute('href')
    #print(price) # 1,472,500원 이렇게 나옴
    ad_item_name.append(name)
    ad_item_price.append(price)
    ad_item_link.append(link)
    
for element in basic_list:
    name = element.find_element(By.CLASS_NAME, "product_title__Mmw2K").text
    price = element.find_element(By.CLASS_NAME, "price_num__S2p_v").text
    link = element.find_element(By.CLASS_NAME, "product_title__Mmw2K > a").get_attribute('href')
    basic_item_name.append(name)
    basic_item_price.append(price)
    basic_item_link.append(link)
    
print(len(ad_item_name), len(ad_item_price), len(ad_item_link)) 
print(len(basic_item_name), len(basic_item_price), len(basic_item_link))


for name, price, link in zip(ad_item_name, ad_item_price, ad_item_link):
    print(f"상품 이름: {name} / 상품 가격: {price} ")
    
for name, price, link in zip(basic_item_name, basic_item_price, basic_item_link):
    print(f"상품 이름: {name} / 상품 가격: {price} ")