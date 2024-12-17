from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

# headless 옵션  -- 적용안됨으로 폐기
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Headless 모드 활성화
# chrome_options.add_argument("--disable-dev-shm-usage")  # 리소스 제한을 해제
# chrome_options.add_argument("--window-size=1920x1080")  # 화면 해상도 설정
# browser = webdriver.Chrome(options=chrome_options)


# cityid = 14690
# cityid = input("코드 입력 >")
cityid = 14690
url = f"https://www.agoda.com/ko-kr/search?city={cityid}&checkIn=2024-12-17&los=2&rooms=1&adults=2&children=0&checkOut=2024-12-30"
browser = webdriver.Chrome()
# browser.maximize_window()
browser.get(url)


# 최대 20초 동안 호텔 리스트가 뜨는지 대기하기
WebDriverWait(browser,20).until(lambda x:x.find_element(By.ID,'searchPageRightColumn'))

# 초기 페이지 높이
prev_height = browser.execute_script("return document.body.scrollHeight")
time.sleep(3)
# 무한 스크롤 시작
while True:
    # 부드럽게 페이지 끝으로 스크롤 (smooth)
    browser.execute_script("""
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    """)

    # 스크롤이 완료되기를 기다림 (5초)
    time.sleep(5)  # AJAX 콘텐츠 로딩을 대기하는 시간 (상황에 따라 조절 가능)

    # 현재 스크롤 위치의 높이를 다시 가져옴
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    # 이전 스크롤 높이와 현재 높이가 같으면 스크롤 종료
    if prev_height == curr_height:
        print(f"추가 콘텐츠 없음. 스크롤 중지. 최종 높이: {curr_height}px")
        break

    # 현재 높이를 이전 높이로 갱신
    prev_height = curr_height

    print(f"스크롤 완료, 현재 높이: {curr_height}px")


soup = BeautifulSoup(browser.page_source,'lxml')
with open(f'MaWz/기능테스트/아고다.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())



# item_list = []
# f = open("c1025/mouses.csv",'a',encoding='utf-8-sig',newline="")
# writer = csv.writer(f)


# with open(f"MaWz/기능테스트/아고다.html",'r',encoding='utf8') as f:
#   soup = BeautifulSoup(f,'lxml')
# data = soup.select_one("div#contentContainer")
# items = data.select("div.adProduct_item__1zC9h")
# #### html파일 불러와서 마우스 정보 출력 (이름, 금액, 평점, 평가수, 찜) 총 5가지
# 광고 상품들 저장





# # 광고가 아닌 상품들 저장
# for i in range(5):
#   with open(f"c1025/mouse{i+1}.html",'r',encoding='utf8') as f:
#     soup = BeautifulSoup(f,'lxml')
#   data = soup.select_one("div.basicList_list_basis__uNBZx")
#   items = data.select("div.product_item__MDtDF")
#   # item = data.select_one("div.product_item__MDtDF")


#   for idx,item in enumerate(items):
#     try:
#       name = item.select_one("div.product_title__Mmw2K > a").text.strip()
#       cost = int(item.select_one("span.price_num__S2p_v").text.strip().replace(",","")[:-1])
#       star = float(item.select_one("span.product_grade__IzyU3").text.replace("별점","").strip())
#       riveiw = item.select_one("div.product_etc_box__ElfVA > a > em").text.strip()[1:-1].strip()
#       zzim = item.select_one("span.product_etc__LGVaW").text.replace("찜","").strip().replace(",","")

#       intr = rivint(riveiw)
#       print('번호 : ', idx+1)
#       print("이름 : ", name)
#       print("금액 : ", cost)
#       print("평점 : ", star)
#       print("평가수 : ", intr)
#       print("찜 수 : ", zzim)
#       print("-"*60)
#       writer.writerow([name,cost,star,intr,zzim])
#     except Exception as e:
#       print("정보 부족으로 패스")
#       print(e)
#       print("-"*60) 


# time.sleep(1000)



# # # 1.상단타이틀. csv파일로 저장
# # f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline="")
# # writer = csv.writer(f)
# # m_list = [ st.text  for st in stocks[0].select("th") ]
# # writer.writerow(m_list)