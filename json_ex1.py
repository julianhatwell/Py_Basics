import json
from urllib import request

url = 'http://python-data.dr-chuck.net/comments_264783.json'
req = request.urlopen(url)

encoding = req.headers.get_content_charset()
obj = json.loads(req.read().decode(encoding))

adder = 0
for item in obj['comments']:
    num = int(item['count'])
    adder = adder + num
print(adder)