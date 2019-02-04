import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2638060100"
savename = "c:/section4/dadae.xml"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)

xml = open(savename,"r",encoding='utf-8').read()
soup = BeautifulSoup(xml,"html.parser")

info = {}
for dadae in soup.find_all("data"):
    #print(dadae)
    hour = dadae.find("hour").string
    #print(hour)
    max = dadae.find("tmx").string
    min = dadae.find("tmn").string
    print(hour,"시","최고온도",max,"최저온도",min)
    if not (hour in info):
        info[hour]=[max,min]
print(info)
