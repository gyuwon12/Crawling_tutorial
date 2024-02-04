import requests
from bs4 import BeautifulSoup
import time

input_querys = ['게이밍+마우스', '기계식+키보드', '27인치+모니터']

header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}

# url 특징
# https://www.coupang.com/np/search?component=&q=게이밍+마우스&channel=user
# https://www.coupang.com/np/search?q=게이밍+마우스&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=9&backgroundColor=
# https://www.coupang.com/np/search?q=게이밍+마우스&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=3&rocketAll=false&searchIndexingToken=1=9&backgroundColor=
# https://www.coupang.com/np/search?component=&q=기계식+키보드&channel=user


count=0
for input_query in input_querys:
    ranking = 1 # 100위 까지만
    for i in range(15):
        response = requests.get(f"https://www.coupang.com/np/search?component=&q={input_query}&channel=user&page={i}", headers=header)
        html = response.text
        
        soup = BeautifulSoup(html, "html.parser") 
        items = soup.select(".search-product ")
        
        for item in items:
            if "search-product__ad-badge" not in str(item): # 문자열로 바꿔서 광고 아닌 것만 가져오기
                count+=1
                # 상세페이지
                coupang_itme_link = "https://www.coupang.com" + item.select_one('a').attrs['href'] # /vp/products/7410134472?itemId=19632158579&vendorItemId=86315311963 이런식으로 가져와서 수정 필요
                response = requests.get(coupang_itme_link, headers=header)
                html = response.text
                
                # 본문 링크와 구별을 위해 변수 이름을 다르게 설정
                soup_sub = BeautifulSoup(html, "html.parser") 
                
                # 가격 -> 가격이 '반품'인 경우를 제외 처리 해야함.
                try:
                    price = soup_sub.select_one(".total-price").text
                except:
                    price = "가격 정보 없음"
                # 제품명
                item_name = soup_sub.select_one(".prod-buy-header__title").text
                
                # 브랜드명 -> 브랜드가 없을 경우를 처리 해야함(출력을 해보니까 알아서 처리가 됨 빈칸으로)
                try:
                    brand_name = soup_sub.select_one(".prod-brand-name").attrs['data-brand-name'] # 이렇게 해줘야 깔끔
                except:
                    brand_name = ""
                #print(brand_name, item_name, price)

                ranking += 1
                
                if ranking == 100:
                    break # 한 페이지 내에서 빠져나가기
        print(ranking)
        if ranking == 100:
            break # 10페이지까지 돌리는거 중단하기
        
print(count)