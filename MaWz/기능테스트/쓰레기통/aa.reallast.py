from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os

# Create directory if it doesn't exist
os.makedirs('./MaWz/기능테스트', exist_ok=True)

cityid = 14690
url = f"https://www.agoda.com/ko-kr/search?city={cityid}&checkIn=2024-12-17&los=2&rooms=1&adults=2&children=0&checkOut=2024-12-30"

browser = webdriver.Chrome()
browser.get(url)

# 최대 20초 동안 호텔 리스트가 뜨는지 대기하기
WebDriverWait(browser, 20).until(lambda x: x.find_element(By.ID, 'searchPageRightColumn'))

# 초기 페이지 높이
prev_height = browser.execute_script("return document.body.scrollHeight")
time.sleep(2)
browser.execute_script("""window.scrollTo({top: 100, behavior: 'smooth' });""")
time.sleep(2)

# 무한 스크롤 시작
while True:
    browser.execute_script("""
        window.scrollTo({
            top: document.body.scrollHeight -200,
            behavior: 'smooth'
        });
    """)
    time.sleep(5)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        print(f"추가 콘텐츠 없음. 스크롤 중지. 최종 높이: {curr_height}px")
        break
    prev_height = curr_height
    print(f"스크롤 완료, 현재 높이: {curr_height}px")

soup = BeautifulSoup(browser.page_source, 'lxml')

# CSV 파일을 먼저 생성하고 헤더 작성
csv_path = './MaWz/기능테스트/hotel_data.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    # 헤더 작성
    writer.writerow(['번호', '호텔명', '가격', '평점', '리뷰'])

# 검색 결과의 컨테이너 선택
data = soup.select_one("div#searchPageRightColumn")

# 호텔 섹션의 모든 PropertyCardItem 선택
items = data.select("li.PropertyCard.PropertyCardItem")

# 상품들 정보 추출 및 CSV 파일에 추가
with open(csv_path, 'a', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for idx, item in enumerate(items):
        try:
            no = idx + 1
            name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
            cost = int(item.select_one("span.sc-jrAGrp.sc-kEjbxe.eDlaBj.hZQUvX").text.strip().replace(",", ""))
            star = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").text.strip()
            star2 = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").find_next_sibling().text.strip()
            
            writer.writerow([no, name, cost, star, star2])
            print(f"데이터 추가 완료: {name}")
        except Exception as e:
            print(f"정보 추출 실패: {e}")
            continue

browser.quit()
print(f"CSV 파일이 생성되었습니다: {csv_path}")