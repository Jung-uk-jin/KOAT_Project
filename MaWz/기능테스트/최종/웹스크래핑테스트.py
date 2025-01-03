import os
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

# 디렉터리 설정 및 생성
base_path = r'C:/workspace/Koat/KOAT_Project/MaWz/기능테스트/최종'
html_path = os.path.join(base_path, '정보 추출.html')
csv_path = os.path.join(base_path, '정보 정리.csv')
os.makedirs(base_path, exist_ok=True)

# # 브라우저 옵션 설정
# chrome_options = Options()
# chrome_options.add_argument("--disable-dev-shm-usage")  # 리소스 제한 해제
# chrome_options.add_argument("--window-size=1920x1080")  # 화면 해상도 설정

# # 웹 스크래핑 설정
# city_id = 14690  # 도시 코드, 필요에 따라 변경 가능
# url = f"https://www.agoda.com/ko-kr/search?city={city_id}&checkIn=2024-12-17&los=2&rooms=1&adults=2&children=0&checkOut=2024-12-30"

# # 브라우저 실행
# browser = webdriver.Chrome(options=chrome_options)
# browser.get(url)

# # 최대 20초 동안 호텔 리스트가 뜨는지 대기하기
# WebDriverWait(browser, 20).until(lambda x: x.find_element(By.ID, 'searchPageRightColumn'))

# # 스크롤 작업
# prev_height = browser.execute_script("return document.body.scrollHeight")
# time.sleep(3)
# while True:
#     browser.execute_script("""window.scrollTo({top: document.body.scrollHeight - 300, behavior: 'smooth'});""")
#     time.sleep(5)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == curr_height:
#         print(f"추가 콘텐츠 없음. 스크롤 중지. 최종 높이: {curr_height}px")
#         break
#     prev_height = curr_height

# # 페이지 소스 저장
# soup = BeautifulSoup(browser.page_source, 'lxml')
# with open(html_path, 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())
# print(f"HTML 파일이 저장되었습니다: {html_path}")

# browser.quit()

# HTML 파일에서 데이터 추출
print("\n=== HTML 파일에서 데이터 추출 ===")
try:
    with open('C:/workspace/Koat/KOAT_Project/MaWz/기능테스트/최종/정보 추출.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    
    # 검색 결과의 컨테이너 선택
    data = soup.select_one("div#searchPageRightColumn")
    items = data.select("li.PropertyCard.PropertyCardItem")

    # CSV 파일 생성 및 데이터 저장
    with open(csv_path, 'w', encoding='utf-8-sig', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['번호', '호텔명', '가격', '링크'])  # CSV 헤더

        for idx, item in enumerate(items):
            try:
                no = idx + 1
                name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
                cost = int(item.select_one("ul > li:nth-child(3) > div > div > div > span.PropertyCardPrice__Value")
                           .text.strip().replace(",", ""))
                hlink = item.select_one("button.ab069-box img")
                href = hlink['src'] if hlink else "https://i.pinimg.com/736x/d0/14/73/d01473fbb3094de59b2402ea88672ef2.jpg"
                writer.writerow([no, name, cost, href])
                print(f"추출 완료: {no}, {name}, {cost}, {href}")
            except Exception as e:
                print(f"정보 추출 실패: {e}")
except Exception as e:
    print(f"HTML 파일에서 데이터 읽기 실패: {e}")

print(f"CSV 파일이 생성되었습니다: {csv_path}")
