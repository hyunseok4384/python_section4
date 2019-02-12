from pandas import Series, DataFrame
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r_data = {'City':['서울','대구','부산','대전'], 'Total1':[55000,49000,52000,50000], 'Total2':[65000,59000,62000,60000]}
print(type(r_data))
i_data = ['one','two','three','four']

#출력1
print(r_data)
print(i_data)

#DataFrame 정의
d_frame = DataFrame(r_data, index = i_data)
print(type(d_frame))
print(d_frame)
"""
      City  Total1  Total2
one     서울   55000   65000
two     대구   49000   59000
three   부산   52000   62000
four    대전   50000   60000
"""
print(d_frame.index)
print(d_frame.values)
print(d_frame['City']) #Columns 열 데이터를 가지고 온다
print(d_frame['Total1'])
print(d_frame.ix['one']) #ix는 행 데이터를 가지고 온다
print(type(d_frame.ix['one'])) #<class 'pandas.core.series.Series'>

#값 순회
for e in d_frame.values:
    for i,z in enumerate(e):
        print(i,z)
