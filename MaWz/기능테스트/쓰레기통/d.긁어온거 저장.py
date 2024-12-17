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
    name = item.select_one("#contentContainer > div:nth-child(4) > ol:nth-child(1) > li:nth-child(2) > div > div > a > div > div.Itemstyled__Item-sc-12uga7p-0.ewNxOO.PropertyCard__Section.PropertyCard__Section--propertyInfo.withPackageBundle > div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-h-full.a16dd-flex.a16dd-flex-col.a16dd-px-m.a16dd-py-s > header > div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-inline > h3").text.strip()
    print("이름 : ", name)
    # cost = int(item.select_one("span.sc-jrAGrp.sc-kEjbxe.eDlaBj.hZQUvX").text.strip().replace(",",""))
    # print("금액 : ", cost)
    # star = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").text.strip()
    # star2 = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").find_next_sibling().text.strip()
    # # star = float(item.select_one("span.sc-jrAGrp.sc-kEjbxe.fzPhrN.ehWyCi").text.strip())
    # print("평점 : ", star)
    # print("평점2 : ", star2)
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


# ---------------------------------------------


# from bs4 import BeautifulSoup
# import csv

# # HTML 파일 불러오기 및 BeautifulSoup 객체 생성
# with open("MaWz/\uac01\ub2f4\ud14c\uc2a4\ud2b8/\uc544\uace0\ub2f4.html", 'r', encoding='utf8') as f:
#     soup = BeautifulSoup(f, 'lxml')

# # 검색 결과의 컨테이너 선택
# data = soup.select_one("div#searchPageRightColumn")

# # 호텔 섹션의 모든 PropertyCardItem 선택
# items = data.select("li.PropertyCard.PropertyCardItem")

# # 광고가 아닌 상품들 정보 추출 및 CSV 파일로 저장
# for idx, item in enumerate(items):
#     try:
#         no = idx + 1
#         name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
#         cost = int(item.select_one("span.sc-jrAGrp.sc-kEjbxe.eDlaBj.hZQUvX").text.strip().replace(",", ""))
#         star = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").text.strip()
#         star2 = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").find_next_sibling().text.strip()
        
#         with open('MaWz/\uac01\ub2f4\ud14c\uc2a4\ud2b8/\uc544\uace0\ub2f4\uc800\uc7a5.csv', 'a', encoding='utf-8-sig', newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow([no, name, cost, star, star2])
#     except Exception as e:
#         print("정보 부족으로 패스")
#         print(e)
#         print("-" * 60)
