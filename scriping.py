from os import close
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from itertools import zip_longest

data_text = []
numbers = []
links = []
description = []

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
 
links_zone = soup.find_all("div" ,{"class":"col-sm-6 col-md-4 col-12"})

for i in range(len(data)):
    data_text.append(data[i].text)

final_list = [data_text,numbers,description]

exported = zip_longest(*final_list)

with open("/home/moh/Desktop/phones.csv" ,"w") as file_phones:
    write = csv.writer(file_phones)
    write.writerow(["phones data" ,"number","description"])
    write.writerows(exported)

for i in range(len(links_zone)):
    links.append("https://www.ouedkniss.com"+links_zone[i].find("a").attrs["href"])

for link in links:
  driver = webdriver.Chrome(chromedriver_path)
  driver.get(link)
  time.sleep(1)
  page = driver.page_source
  driver.quit()
  soup = BeautifulSoup(page, 'html.parser')

  n = soup.find_all("a",{"class":"v-chip v-chip--clickable v-chip--link v-chip--no-color theme--light v-size--default"})

  d = soup.find_all("div",{"class":"__description mb-4"})
  
  for i in range(len(n)):
    # print(n[i])
    tempnumber = n[i].attrs["href"]
    numbers.append(tempnumber)
    
    final_list = [data_text,numbers,description]
    exported = zip_longest(*final_list)

    with open("/home/moh/Desktop/phones.csv" ,"w") as file_phones:
     write = csv.writer(file_phones)
     write.writerow(["phones data" ,"number","description"])
     write.writerows(exported)
     break

  if len(d) == 0 :
     description.append("null")
     final_list = [data_text,numbers,description]
     exported = zip_longest(*final_list)

     with open("/home/moh/Desktop/phones.csv" ,"w") as file_phones:
      write = csv.writer(file_phones)
      write.writerow(["phones data" ,"number","description"])
      write.writerows(exported)

  for i in range(len(d)):
    print(d[i].find("div").text)
    tempdes = d[i].find("div").text
    description.append(tempdes)
    
    final_list = [data_text,numbers,description]
    exported = zip_longest(*final_list)

    with open("/home/moh/Desktop/phones.csv" ,"w") as file_phones:
     write = csv.writer(file_phones)
     write.writerow(["phones data" ,"number","description"])
     write.writerows(exported)
     break