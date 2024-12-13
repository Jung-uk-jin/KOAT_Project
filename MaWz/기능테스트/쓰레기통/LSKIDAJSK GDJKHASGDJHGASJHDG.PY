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

cityid = 14690
url = f"https://www.agoda.com/ko-kr/search?city={cityid}&checkIn=2024-12-17&los=2&rooms=1&adults=2&children=0&checkOut=2024-12-30"
browser = webdriver.Chrome()
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

  
with open(f"MaWz/기능테스트/아고다.html",'r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')
data = soup.select_one("div#searchPageRightColumn")
# item = data.select_one("div.PropertyCardItem")
items = data.select("li.PropertyCard.PropertyCardItem")
#### html파일 불러와서 마우스 정보 출력 (이름, 금액, 평점, 평가수, 찜) 총 5가지
# 광고 상품들 저장
# 호텔 섹션 PropertyCardItem


print(items)



# # 광고가 아닌 상품들 저장
# for i in range(5):
#   with open(f"c1025/mouse{i+1}.html",'r',encoding='utf8') as f:
#     soup = BeautifulSoup(f,'lxml')
#   data = soup.select_one("div.basicList_list_basis__uNBZx")
#   items = data.select("div.product_item__MDtDF")
#   # item = data.select_one("div.product_item__MDtDF")


for idx,item in enumerate(items):
  try:
    no = (idx + 1)
    name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
    print("이름 : ", name)
    cost = int(item.select_one("span.sc-jrAGrp.sc-kEjbxe.eDlaBj.hZQUvX").text.strip().replace(",",""))
    print("금액 : ", cost)
    star = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").text.strip()
    star2 = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").find_next_sibling().text.strip()
    # star = float(item.select_one("span.sc-jrAGrp.sc-kEjbxe.fzPhrN.ehWyCi").text.strip())
    print("평점 : ", star)
    print("평점2 : ", star2)
    # sc-jrAGrp sc-kEjbxe fzPhrN ehWyCi

    # # starment = item.select_one("div.ab069-box.ab069-fill-inherit.ab069-text-inherit > p.sc-jrAGrp.sc-kEjbxe.eDlaBj > span.sc-jrAGrp.sc-kEjbxe").text.strip()
    # # print("평가 : ", starment)

    # riveiw = item.select_one("#contentContainer > div:nth-child(4) > ol:nth-child(1) > li:nth-child(1) > div > div > a > div > div.Itemstyled__Item-sc-12uga7p-0.cNsNca.PropertyCard__Section.PropertyCard__Section--pricingInfo > div > div.Box-sc-kv6pi1-0.hRUYUu.PropertyCard__PricingHeadliner > div > div > p").text.strip().replace(",","").split(" ")
    # # riveiw = item.select_one("div.ReviewWithDemographic > p.sc-jrAGrp.sc-kEjbxe.iDzlXT").text.strip().split(" ")/
    # rev2 = riveiw[0]
    # print("리뷰수 : ", riveiw)
    # print("리뷰 건수 : ", riveiw[0])
    # # zzim = item.select_one("span.product_etc__LGVaW").text.replace("찜","").strip().replace(",","")

    # hlink = soup.select_one("#contentContainer > div:nth-child(5) > ol:nth-child(3) > li:nth-child(73) > div > div > a")
    # href = hlink['href']
    # print("링크 : ", hlink['href'])
    # print("-"*60)

    # 1.상단타이틀. csv파일로 저장
    f = open('MaWz/기능테스트/아고다저장.csv','a',encoding='utf-8-sig',newline="")
    writer = csv.writer(f)
    # m_list = [ st.text  for st in stocks[0].select("th") ]
    # writer.writerow(m_list)
    writer.writerow([no, name, cost, star, star2])
    # writer.writerow([no, name, cost, star, star2, rev2, href])
  except Exception as e:
    print("정보 부족으로 패스")
    print(e)
    print("-"*60) 


# href = hlink['href']
# print("링크 2: ", href)

# intr = rivint(riveiw)
# print('번호 : ', idx+1)


# time.sleep(1000)
