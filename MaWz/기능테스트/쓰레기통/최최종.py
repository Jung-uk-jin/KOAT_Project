from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os

# 디렉터리 생성
os.makedirs('./MaWz/기능테스트/최종/최최종', exist_ok=True)

# 브라우저 옵션 설정
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Headless 모드 활성화
chrome_options.add_argument("--disable-dev-shm-usage")  # 리소스 제한 해제
chrome_options.add_argument("--window-size=1920x1080")  # 화면 해상도 설정

cityid = 17172
url = f"https://www.agoda.com/ko-kr/search?city={cityid}&checkIn=2024-12-17&los=2&rooms=1&adults=2&children=0&checkOut=2024-12-30"

# 브라우저 실행
browser = webdriver.Chrome(options=chrome_options)
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
            top: document.body.scrollHeight - 200,
            behavior: 'smooth'
        });
    """)
    time.sleep(5)  # AJAX 콘텐츠 로딩을 대기하는 시간
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        print(f"추가 콘텐츠 없음. 스크롤 중지. 최종 높이: {curr_height}px")
        break
    prev_height = curr_height
    print(f"스크롤 완료, 현재 높이: {curr_height}px")

# 페이지 소스 저장
soup = BeautifulSoup(browser.page_source, 'lxml')
with open('./MaWz/기능테스트/최종/최최종/webscrap.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

browser.quit()

# 검색 결과의 컨테이너 선택
data = soup.select_one("div#searchPageRightColumn")

# 호텔 섹션의 모든 PropertyCardItem 선택
items = data.select("li.PropertyCard.PropertyCardItem")

# 상품들 정보 추출 및 CSV 파일로 저장
csv_path = './MaWz/기능테스트/최종/최최종/h_list.csv'
try:
    with open(csv_path, 'a', encoding='utf-8-sig', newline="") as f:
        writer = csv.writer(f)
        for idx, item in enumerate(items):
            try:
                no = idx + 1
                name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
                cost = int(item.select_one("span.sc-jrAGrp.sc-kEjbxe.eDlaBj.hZQUvX").text.strip().replace(",", ""))
                star = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").text.strip()
                star2 = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").find_next_sibling().text.strip()
                # print([no, name, cost, star, star2])
                writer.writerow([no, name, cost, star, star2])
            except Exception as e:
                print("정보 부족으로 패스")
                print(e)
                print("-" * 60)
except Exception as e:
    print("CSV 파일 생성 중 오류 발생:", e)
