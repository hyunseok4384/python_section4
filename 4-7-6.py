import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

#조회 시작 날짜
start = datetime.datetime(2018,2,1)
end = datetime.datetime(2018,2,17)

#네이버 주식 정보 조회
gs_naver = web.DataReader('', 'google', start, end)

#카카오 주식 정보 조회
gs_kakao = web.DataReader('', 'google', start, end)

#출력
print(gs_naver)
print(gs_kakao)

#윈도우 제목
fig = plt.figure('Chart Test')

#차트 사이즈 지정
fig.set_size_inches(10,6,forward=True)

#차트설정1
plt.plot(gs_naver.index, gs_naver['Close'], 'b', label='Naver')

#차트설정2
plt.plot(gs_kakao.index, gs_kakao['Close'], 'r', label='Kakao')

#범례위치 지정
plt.legend(loc='upper left')

#차트 제목
plt.title('Naver & Kakao')

#x축 라벨
plt.xlabel('Date')

#y축 라벨
plt.xlabel('Close')

plt.show()
