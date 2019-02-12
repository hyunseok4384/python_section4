import pandas_datareader.data as web
import datetime

#조회 시작날짜 & 마감날짜
start = datetime.datetime(2018,2,1)

end = datetime.datetime(2018,2,15)

#Google 정보 호출
gs = web.DataReader('C', 'iex', start, end)
print(gs)

print(gs['Open'])
print(gs.ix['2018-02-13'])
print(gs.describe())
