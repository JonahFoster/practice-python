# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

import requests
from bs4 import BeautifulSoup

# Get the html and turn it into a string
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

all_body_text = soup.select("div.parbase.cn_text > div.body > p")

for elem in all_body_text[7:]:
  print(elem.text)