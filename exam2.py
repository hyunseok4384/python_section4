import urllib.request as req
import simplejson as json
import os.path

url = "https://jsonplaceholder.typicode.com/comments"
savename = "c:/section4/exam2.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding='utf8'))
#items = json.loads(open(savename, 'r', encoding='utf-8').read())

with open('c:/section4/exam2.txt', 'w') as f:
    for item in items:
        print(item['name'] + " : " + item['email'])
        print(type(item)) #Dict
        r = json.dumps(item['name'])
        print(type(r)) #Str
        r2 = json.dumps(item['email'])
        print(type(r2)) #Str
        f.write(r + ' : ' + r2 + '\n')
