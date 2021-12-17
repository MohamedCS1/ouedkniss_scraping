import time
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from itertools import zip_longest

data_text = []
number_text = []
links = []

chromedriver_path= "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(chromedriver_path)

# for i in range(0,100):

url = "https://www.ouedkniss.com/telephones/1"

driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

data = soup.find_all("div" ,{"class":"px-2 pt-1 pb-2"})
 
links_zone = soup.find_all("div" ,{"class":"full-h"})

for i in range(len(data)):
    data_text.append(data[i].text)

for i in range(len(links_zone)):
    links.append(links_zone[i].find("a").attrs["href"])

print(links)
# print(data_text)

# print(number_text)

# final_list = [data_text]

# exported = zip_longest(*final_list)

# with open("/home/moh/Desktop/phones.csv" ,"w") as file_phones:
    # write = csv.writer(file_phones)
    # write.writerow(["phones data" ,])
    # write.writerows(exported)