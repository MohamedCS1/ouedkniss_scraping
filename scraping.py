from os import close, sysconf_names
import os
from os.path import join
import os.path
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from itertools import zip_longest



numberpage = input("Enter number pages--> ")


directory = "proccesing"
    
parent_dir = "/home/moh/Desktop"

if os.path.isdir("/home/moh/Desktop/proccesing"):
    print("run...")
else:
     
 path = os.path.join(parent_dir, directory)
 os.mkdir(path) 
 print("Directory '% s' created" % directory)
 print("run...")

data_text = []
numbers = []
links = []
description = []
final_list = []
counter = 0

for i in range(1,int(numberpage)+2):
 if i == int(numberpage)+1:

  temp_a = []
  temp_b = []
  temp_c = []
  
  for j in range(1,int(numberpage)+2):

   if j == int(numberpage)+1:
      for n in range(1,int(numberpage)+1):
        if n == int(numberpage)+1:
          os.exit("finish your csv in '/home/moh/Desktop/proccesing/phonesfinal.csv'")
        os.remove('/home/moh/Desktop/proccesing/phones'+str(n)+'.csv')    

      
    
   with open('/home/moh/Desktop/proccesing/phones'+str(j)+'.csv','rt')as f:
     data = csv.reader(f)
     for row in data:
        temp_a.append(row[0])
        temp_b.append(row[1])
        temp_c.append(row[2])

   final_list = [temp_a,temp_b,temp_c]
   exported = zip_longest(*final_list)

   with open("/home/moh/Desktop/proccesing/phonesfinal.csv" ,"w") as file_phones:
      write = csv.writer(file_phones)
      write.writerows(exported)
      file_phones.close()

 counter = counter + 1
 data_text.clear()
 numbers.clear()
 links.clear()
 description.clear()
 final_list.clear()

 chromedriver_path= "/usr/lib/chromium-browser/chromedriver"
 # for i in range(0,100):

 url = "https://www.ouedkniss.com/telephones/"+str(i-1)

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

 with open("/home/moh/Desktop/proccesing/phones"+str(counter)+".csv" ,"w") as file_phones:
     write = csv.writer(file_phones)
     write.writerow(["phones data" ,"number","description"])
     write.writerows(exported)
     file_phones.close()

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

   d = soup.find_all("div",{"class":"__description mb-4"}) + soup.find_all("div",{"class":"__description mb-4 --collapsed"})


   if len(n) == 0 :
      numbers.append("null")
      final_list = [data_text,numbers,description]
      exported = zip_longest(*final_list)

      with open("/home/moh/Desktop/proccesing/phones"+str(counter)+".csv" ,"w") as file_phones:
       write = csv.writer(file_phones)
       write.writerow(["phones data" ,"number","description"])
       write.writerows(exported)
       file_phones.close()
  
   for i in range(len(n)):
    # print(n[i])
     tempnumber = n[i].attrs["href"]
     numbers.append(tempnumber)
    
     final_list = [data_text,numbers,description]
     exported = zip_longest(*final_list)

     with open("/home/moh/Desktop/proccesing/phones"+str(counter)+".csv" ,"w") as file_phones:
      write = csv.writer(file_phones)
      write.writerow(["phones data" ,"number","description"])
      write.writerows(exported)
      file_phones.close()
      break

   if len(d) == 0 :
      description.append("null")
      final_list = [data_text,numbers,description]
      exported = zip_longest(*final_list)

      with open("/home/moh/Desktop/proccesing/phones"+str(counter)+".csv" ,"w") as file_phones:
       write = csv.writer(file_phones)
       write.writerow(["phones data" ,"number","description"])
       write.writerows(exported)
       file_phones.close()

   for i in range(len(d)):
    # print(d[i].find("div").text)
     tempdes = d[i].find("div").text
     description.append(tempdes)
    
     final_list = [data_text,numbers,description]
     exported = zip_longest(*final_list)

     with open("/home/moh/Desktop/proccesing/phones"+str(counter)+".csv" ,"w") as file_phones:
      write = csv.writer(file_phones)
      write.writerow(["phones data" ,"number","description"])
      write.writerows(exported)
      file_phones.close()
      break
