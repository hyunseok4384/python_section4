import simplejson as json
#import json

#Dict(json)선언
data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website':'daum.com',
    'from':'Incheon'
})
#print(data)
#data = {'people': [{'name': 'Kim', 'website': 'naver.com', 'from': 'Seoul'}, {'name': 'Park', 'website': 'google.com', 'from': 'Busan'}, {'name': 'Lee', 'website': 'daum.com', 'from': 'Incheon'}]}

#Dict(json) -> str 직렬화
e = json.dumps(data, indent=4)
#print(type(e))
#print(e)

#Str -> Dict(json) 역직렬화
d = json.loads(e)
#print(type(d))
#print(d)

with open('c:/section4/member.json','w') as outfile:
    outfile.write(e)


with open('c:/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    print("====")
    #print(type(r))
    #print(r)
    for p in r['people']:
        print('Name : '+p['name'])
        print('Website : '+p['website'])
        print('From : '+p['from'])
        print('')
"""
====
Name : Kim
Website : naver.com
From : Seoul

Name : Park
Website : google.com
From : Busan

Name : Lee
Website : daum.com
From : Incheon
"""
