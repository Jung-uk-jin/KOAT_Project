import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_hotel_data(city_id):
    """
    특정 도시의 호텔 데이터를 스크래핑하는 함수입니다.
    
    Args:
        city_id (int): 도시 코드
    
    Returns:
        list: 호텔 정보 목록 (번호, 이름, 가격, 링크) 형태의 리스트
    """
    
    # 브라우저 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--disable-dev-shm-usage")  # 리소스 제한 해제
    chrome_options.add_argument("--window-size=1920x1080")  # 화면 해상도 설정

    # 웹 스크래핑 설정
    url = f"https://www.agoda.com/ko-kr/search?city={city_id}&checkIn=2024-12-17&los=2&rooms=1&adults=2&children=0&checkOut=2024-12-30"

    # 브라우저 실행
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)

    # 최대 20초 동안 호텔 리스트가 뜨는지 대기하기
    WebDriverWait(browser, 20).until(lambda x: x.find_element(By.ID, 'searchPageRightColumn'))

    # 스크롤 작업
    prev_height = browser.execute_script("return document.body.scrollHeight")
    time.sleep(3)
    while True:
        browser.execute_script("""
        window.scrollTo({
            top: document.body.scrollHeight - 300,
            behavior: 'smooth'
        });
        """)
        time.sleep(5)
        curr_height = browser.execute_script("return document.body.scrollHeight")
        if prev_height == curr_height:
            print(f"추가 콘텐츠 없음. 스크롤 중지. 최종 높이: {curr_height}px")
            break
        prev_height = curr_height

    # BeautifulSoup로 페이지 소스를 파싱 (HTML 저장 없이 바로 처리)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    browser.quit()

    # 검색 결과의 컨테이너 선택
    data = soup.select_one("div#searchPageRightColumn")

    # 호텔 섹션의 모든 PropertyCardItem 선택
    items = data.select("li.PropertyCard.PropertyCardItem")
    
    hotel_data = []
    
    # 호텔 정보 추출 및 화면에 출력
    for idx, item in enumerate(items):
        try:
            no = idx + 1
            name = item.select_one("h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss").text.strip()
            try:
                cost = int(item.select_one("ul > li:nth-child(3) > div > div > div > div > span").find_next_sibling().text.strip().replace(",", ""))
            except (ValueError, AttributeError):
                cost = None
            hlink_element = item.select_one("button.ab069-box.ab069-bg-base-transparent.ab069-fill-inherit.ab069-text-inherit.ab069-w-full.ab069-cursor-pointer > img")
            hlink = hlink_element['src'] if hlink_element else None
            
            if not all([name, cost, hlink]):
                print(f"정보 부족으로 데이터 건너뜀: 이름: {name}, 가격: {cost}, 링크: {hlink}")
                continue
            
            hotel_data.append([no, name, cost, hlink])
            print('이름 : ', name)
            print('가격 : ', cost)
            print("링크 : ", hlink)
            print("-" * 60)
            
        except Exception as e:
            print(f"정보 추출 실패: {e}")
            continue
    
    print(hotel_data)
    return hotel_data

