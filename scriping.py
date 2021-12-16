import requests
from bs4 import BeautifulSoup
import csv
from itertools import  zip_longest

result = requests.get("https://www.ouedkniss.com/telephones/1")

src = result.content

print(src)