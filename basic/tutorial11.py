# selenium을 활용하여 네이버 로그인 자동화

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 너무 빠르게 입력하면 매크로 의심 받아서 자동입력 방지가 필요
import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 제거 -> 외울 필요 없음
#chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 

service = Service(executable_path=ChromeDriverManager().install()) # 알아서 최신 버전 자동 설치
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩될 때까지 5초는 기다린다. 
driver.maximize_window() # 윈도우 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/") # 로그인 주소

# 아이디 입력창 찾기
id_input = driver.find_element(By.CSS_SELECTOR, "#id") # id 태그가 id 였음 
id_input.click() # 아이디 클릭하고,
id_input.send_keys("bgw8124") # 키보드를 입력하겠다

# 비번 입력창 찾기
pw_input = driver.find_element(By.CSS_SELECTOR, "#pw") # id 태그가 pw 였음 
pw_input.click() # 비번 클릭하고,
pw_input.send_keys("qkrrbdnjs8124") # 키보드를 입력하겠다

# 로그인 버튼 누르기
login_button = driver.find_element(By.CSS_SELECTOR, ".btn_login")
login_button.click()