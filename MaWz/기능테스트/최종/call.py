from FT import scrape_hotel_data

cityid = input("도시 코드를 입력해주세요. >>")

hotel_list = scrape_hotel_data(cityid)

print(hotel_list)