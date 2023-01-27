# Use Exercise 17 and print the results to a text file

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

# Get the html and turn it into a string
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

# Find Titles
soup = BeautifulSoup(r_html, 'html.parser')
for title in soup.find_all("h3", class_="indicate-hover css-66vf3i"):
    print(title.text)

with open('nytimesheadings.txt', 'w') as open_file:
    for title in soup.find_all("h3", class_="indicate-hover css-66vf3i"):
        open_file.write(title.text)