import time
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

name_text = []
price_text = []
location_text = []


chromedriver_path= "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(chromedriver_path)


url = "https://www.ouedkniss.com/telephones/1"

driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

phone_name = soup.find_all("h1")

phone_price = soup.find_all("span" ,{"dir":"ltr"})

phone_location = soup.find_all("div",{"class":"mt-2 d-flex flex-column flex-gap-1 line-height-1"})

# print(phone_name)

for i in range(len(phone_name)):
    name_text.append(phone_name[i].text)


for i in range(len(phone_price)):
    price_text.append(phone_price[i].text)


for i in range(len(phone_location)):
    location_text.append(phone_location[i].text)

# print(name_text)

# print(price_text)

# print(location_text)

with open("/home/moh/Desktop/phones.csv" ,"w") as file_phones:
    write = csv.writer(file_phones)
    write.writerow(["phone name" ,"phone price" ,"phone location"])
    write.writerows([name_text ,price_text ,location_text])