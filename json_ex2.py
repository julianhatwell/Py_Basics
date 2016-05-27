import json
import urllib.request
import urllib.parse

url = 'http://python-data.dr-chuck.net/geojson?'
place = { 'sensor' : 'false',
            'address' : 'Universidad Nacional Autonoma de Mexico' }
data = urllib.parse.urlencode(place)
req = urllib.request.Request(url + data)

response = urllib.request.urlopen(req)

encoding = response.headers.get_content_charset()
obj = json.loads(response.read().decode(encoding))
print(json.dumps(obj['results'], indent = 4))
print(obj['results'][0]['place_id'])

f = open('geojsonresult.txt', 'w')
f.write(obj['results'][0]['place_id'])
f.close()

