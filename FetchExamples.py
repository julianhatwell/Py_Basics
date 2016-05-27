import urllib.request
from bs4 import BeautifulSoup

indexpage = "http://www.pythonlearn.com/code/"
url = indexpage
htmldoc = urllib.request.urlopen(url).read()

soup = BeautifulSoup(htmldoc, "html.parser")
tags = soup('a')

for tag in tags:
    filename = tag.get('href', None)
    if filename.startswith('?') or filename.startswith('/'): continue
    if filename.endswith('/'): continue
    url = indexpage + filename
    htmldoc = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(htmldoc, "html.parser")
    print(filename)
    try: 
        print(soup.prettify())
    except: continue
    f = open(filename, 'w')
    f.write(soup.prettify())
    f.close