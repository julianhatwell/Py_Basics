import re
import urllib.request
from bs4 import BeautifulSoup

page = "http://python-data.dr-chuck.net/comments_264782.html"
htmldoc = urllib.request.urlopen(page).read()

soup = BeautifulSoup(htmldoc, "html.parser")

tags = soup('span')
adder = 0
for tag in tags:
    num = int((tag.contents)[0])
    adder = adder + num
print(adder)