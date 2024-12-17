from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os

os.makedirs('./MaWz/기능테스트/최종/최최종', exist_ok=True)
# 페이지 소스 불러오기
with open('./MaWz/기능테스트/최종/최최종/webscrap.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# 검색 결과의 컨테이너 선택
data = soup.select_one("div#searchPageRightColumn")

# 호텔 섹션의 모든 PropertyCardItem 선택
# item = data.select_one("li.PropertyCard.PropertyCardItem")

# # 상품들 정보 추출 및 콘솔에 출력
# name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
# print('이름 : ', name)

# cost = int(item.select_one("ul > li:nth-child(3) > div > div > div > div > span").find_next_sibling().text.strip().replace(",",""))
# print('가격 : ', cost)

# hlink = item.select_one("button.ab069-box.ab069-bg-base-transparent.ab069-fill-inherit.ab069-text-inherit.ab069-w-full.ab069-cursor-pointer.ab069-text-start.ab069-p-none.ab069-border-none > img ")
# # print('asd : ', hlink)
# href = hlink['src']
# print("링크 : ", href)




# print(f"번호: {no}, 이름: {name}, 가격: {cost}, 평점: {star}, 리뷰 수: {star2}")



# # 호텔 섹션의 모든 PropertyCardItem 선택
items = data.select("li.PropertyCard.PropertyCardItem")
csv_path = './MaWz/기능테스트/최종/최최종/h_list.csv'
# # 상품들 정보 추출 및 콘솔에 출력
for idx, item in enumerate(items):
  with open(csv_path, 'a', encoding='utf-8-sig', newline="") as f:
    writer = csv.writer(f)
    try:
      no = idx + 1
        # 상품들 정보 추출 및 콘솔에 출력
      name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
      print('이름 : ', name)

      cost = int(item.select_one("ul > li:nth-child(3) > div > div > div > div > span").find_next_sibling().text.strip().replace(",",""))
      print('가격 : ', cost)

      hlink = item.select_one("button.ab069-box.ab069-bg-base-transparent.ab069-fill-inherit.ab069-text-inherit.ab069-w-full.ab069-cursor-pointer > img ")
      # print('asd : ', hlink)
      if hlink:
        href = hlink['src']
        print("링크 : ", href)
        print("-" * 60)
      else:
        href = "https://i.pinimg.com/736x/d0/14/73/d01473fbb3094de59b2402ea88672ef2.jpg"
        print("링크 : ", href)
        print("-" * 60)
      writer.writerow([no, name, cost, href])
        # print(f"번호: {no}, 이름: {name}, 가격: {cost}, 평점: {star}, 리뷰 수: {star2}")
    except Exception as e:
        print("정보 부족으로 패스")
        print(e)
        print("-" * 60)


















# # 호텔 섹션의 모든 PropertyCardItem 선택
# items = data.select("li.PropertyCard.PropertyCardItem")

# # 상품들 정보 추출 및 콘솔에 출력
# for idx, item in enumerate(items):
#     try:
#         no = idx + 1
#         name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
#         cost = int(item.select_one("span.sc-jrAGrp.sc-kEjbxe.eDlaBj.hZQUvX").text.strip().replace(",", ""))
#         star = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").text.strip()
#         star2 = item.select_one("div.a16dd-box.a16dd-fill-inherit.a16dd-text-inherit.a16dd-items-center > p.sc-jrAGrp.sc-kEjbxe").find_next_sibling().text.strip()
        
#         print(f"번호: {no}, 이름: {name}, 가격: {cost}, 평점: {star}, 리뷰 수: {star2}")
#     except Exception as e:
#         print("정보 부족으로 패스")
#         print(e)
#         print("-" * 60)
