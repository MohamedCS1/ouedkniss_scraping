import time
from bs4 import BeautifulSoup
from selenium import webdriver

chromedriver_path= "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(chromedriver_path)
url = "https://www.ouedkniss.com/telephones/1"

driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'lxml')

phone_name = soup.find_all("h1")
print(phone_name)