import pandas as pd

df = pd.read_excel('c:/section4/excel_s1.xlsx', header=0)
#print(df)

#컬럼 값 수정
#df['State'] = df['State'].str.replace(' ','|')
#print(df)

#평균 컬럼 추가
df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)
#print(df)

#합계 컬럼 추가
df['Sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)
#print(df)

#최대값 출력
#print(df[['2003','2004','2005']].max(axis=0))

#최소값 출력
#print(df[['2003','2004','2005']].min(axis=0))

#상세 정보 출력
#print(df.describe())

df.to_excel('c:/section4/result_s1.xlsx', index=None)
