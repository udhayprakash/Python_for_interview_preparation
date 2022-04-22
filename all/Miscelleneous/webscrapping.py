#!/usr/bin/python3
"""
Purpose: Program to generate sorted list of Artists from "Billboard Hot 100", based
     on the total number of letters in their track title.

     url: https://www.billboard.com/charts/hot-100/
"""
import os

# To install the packages, if not installed
os.system("pip install -U requests bs4 --user")


import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, "lxml")

details = {}
for index, heading in enumerate(soup.find_all(["h3"])):
    header_text = heading.text.strip()
    spanTag = heading.find_next_siblings("span")
    if spanTag:
        artist = spanTag[0].text.strip()
        details[header_text] = artist

details = dict(sorted(details.items(), key=lambda each: len(each[1]), reverse=True))

for title, artist in details.items():
    print("%55s ======> %s" % (title, artist))

sorted_artists_based_on_title_length = list(details.keys())
print("sorted_artists_based_on_title_length:", sorted_artists_based_on_title_length)
