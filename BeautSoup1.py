import urllib.request
from bs4 import BeautifulSoup

page = "http://python-data.dr-chuck.net/known_by_Dev.html"
for i in range(1,8): 
    htmldoc = urllib.request.urlopen(page).read()

    soup = BeautifulSoup(htmldoc, "html.parser")

    tags = soup('a')
    page = tags[17].get('href', None)
    print(page)

    