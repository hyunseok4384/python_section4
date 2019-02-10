import pandas as pd

#기본 읽기
#df = pd.read_csv('c:/section4/csv_s1.csv')
#print(df)
"""
   Month   "1958"   "1959"   "1960"
0    JAN      340      360      417
1    FEB      318      342      391
2    MAR      362      406      419
3    APR      348      396      461
4    MAY      363      420      472
5    JUN      435      472      535
6    JUL      491      548      622
7    AUG      505      559      606
8    SEP      404      463      508
9    OCT      359      407      461
10   NOV      310      362      390
11   DEC      337      405      432
"""
#행 스킵
#df = pd.read_csv('c:/section4/csv_s1.csv',skiprows=[0,1])
#print(df)
#인덱스 0,1을 생략
"""
   FEB    318    342    391
0  MAR    362    406    419
1  APR    348    396    461
2  MAY    363    420    472
3  JUN    435    472    535
4  JUL    491    548    622
5  AUG    505    559    606
6  SEP    404    463    508
7  OCT    359    407    461
8  NOV    310    362    390
9  DEC    337    405    432
"""
#행 스킵, 헤더 생략
#df = pd.read_csv('c:/section4/csv_s1.csv',skiprows=[0],header=None)
#print(df)
"""
      0    1    2    3
0   JAN  340  360  417
1   FEB  318  342  391
2   MAR  362  406  419
3   APR  348  396  461
4   MAY  363  420  472
5   JUN  435  472  535
6   JUL  491  548  622
7   AUG  505  559  606
8   SEP  404  463  508
9   OCT  359  407  461
10  NOV  310  362  390
11  DEC  337  405  432
"""
#헤더 정의
#df = pd.read_csv('c:/section4/csv_s1.csv',skiprows=[0],header=None,names=["Month",2013,2014,2015])
#print(df)
"""
   Month  2013  2014  2015
0    JAN   340   360   417
1    FEB   318   342   391
2    MAR   362   406   419
3    APR   348   396   461
4    MAY   363   420   472
5    JUN   435   472   535
6    JUL   491   548   622
7    AUG   505   559   606
8    SEP   404   463   508
9    OCT   359   407   461
10   NOV   310   362   390
11   DEC   337   405   432
"""
#인덱스 컬럼 정의
#df = pd.read_csv('c:/section4/csv_s1.csv',skiprows=[0],header=None,names=["Month",2013,2014,2015],index_col=[0])
#print(df)
"""
       2013  2014  2015
Month
JAN     340   360   417
FEB     318   342   391
MAR     362   406   419
APR     348   396   461
MAY     363   420   472
JUN     435   472   535
JUL     491   548   622
AUG     505   559   606
SEP     404   463   508
OCT     359   407   461
NOV     310   362   390
DEC     337   405   432
"""
#특정 값 치환
#df = pd.read_csv('c:/section4/csv_s1.csv',skiprows=[0],header=None,names=["Month",2013,2014,2015],index_col=[0],na_values=['JAN'])
#print(pd.isnull(df))
#print(df)
"""
        2013   2014   2015
Month
NaN    False  False  False
FEB    False  False  False
MAR    False  False  False
APR    False  False  False
MAY    False  False  False
JUN    False  False  False
JUL    False  False  False
AUG    False  False  False
SEP    False  False  False
OCT    False  False  False
NOV    False  False  False
DEC    False  False  False
"""
#실습 정리 및 인덱스 재정의
#df = pd.read_csv('c:/section4/csv_s1.csv',skiprows=[0],header=None,names=["Month",2013,2014,2015])
#print(df)
#print(df.index)
#print(list(df.index))
#print(df.index.values)
#print(df.index.values.tolist())
#print(df.rename(index={0:'aa',1:'bb',2:'cc'}))
#print(df.rename(index=lambda x:x+1))

#읽기
df2 = pd.read_csv('c:/section4/csv_s2.csv',sep=';',skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])
#print(df2)
"""
          Name  Test1  Test2  Test3  Final    Grade
0     Aloysius   40.0   90.0  100.0   83.0     "D-"
1   University   41.0   97.0   96.0   48.0     "D+"
2       Gramma   41.0   80.0   60.0   44.0      "C"
3     Electric   42.0   23.0   36.0   47.0     "B-"
4         Fred   43.0   78.0   88.0   45.0     "A-"
5        Betty   44.0   90.0   80.0   46.0     "C-"
6        Cecil   45.0   11.0   -1.0   43.0      "F"
7          Bif   46.0   20.0   30.0   50.0     "B+"
8       Andrew   49.0    1.0   90.0   83.0      "A"
9          Jim   48.0    1.0   97.0   97.0     "A+"
10         Art   44.0    1.0   80.0   40.0     "D+"
11         Jim   47.0    1.0   23.0   45.0     "C+"
12         Ima   45.0    1.0   78.0   77.0     "B-"
13       Benny   50.0    1.0   90.0   90.0     "B-"
14         Boy   40.0    1.0   11.0    4.0      "B"
15      Harvey   30.0    1.0   20.0   40.0      "C"
"""
#컬럼 내용 변경
#df2['Grade'] = df2['Grade'].str.replace('C','A++')
#print(df2)
"""
          Name  Test1  Test2  Test3  Final      Grade
0     Aloysius   40.0   90.0  100.0   83.0       "D-"
1   University   41.0   97.0   96.0   48.0       "D+"
2       Gramma   41.0   80.0   60.0   44.0      "A++"
3     Electric   42.0   23.0   36.0   47.0       "B-"
4         Fred   43.0   78.0   88.0   45.0       "A-"
5        Betty   44.0   90.0   80.0   46.0     "A++-"
6        Cecil   45.0   11.0   -1.0   43.0        "F"
7          Bif   46.0   20.0   30.0   50.0       "B+"
8       Andrew   49.0    1.0   90.0   83.0        "A"
9          Jim   48.0    1.0   97.0   97.0       "A+"
10         Art   44.0    1.0   80.0   40.0       "D+"
11         Jim   47.0    1.0   23.0   45.0     "A+++"
12         Ima   45.0    1.0   78.0   77.0       "B-"
13       Benny   50.0    1.0   90.0   90.0       "B-"
14         Boy   40.0    1.0   11.0    4.0        "B"
15      Harvey   30.0    1.0   20.0   40.0      "A++"
"""
#평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) #x방향 통계
#print(df2)

#합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1) #x방향 합계
print(df2)
"""
          Name  Test1  Test2  Test3  Final    Grade    Avg    Sum
0     Aloysius   40.0   90.0  100.0   83.0     "D-"  78.25  313.0
1   University   41.0   97.0   96.0   48.0     "D+"  70.50  282.0
2       Gramma   41.0   80.0   60.0   44.0      "C"  56.25  225.0
3     Electric   42.0   23.0   36.0   47.0     "B-"  37.00  148.0
4         Fred   43.0   78.0   88.0   45.0     "A-"  63.50  254.0
5        Betty   44.0   90.0   80.0   46.0     "C-"  65.00  260.0
6        Cecil   45.0   11.0   -1.0   43.0      "F"  24.50   98.0
7          Bif   46.0   20.0   30.0   50.0     "B+"  36.50  146.0
8       Andrew   49.0    1.0   90.0   83.0      "A"  55.75  223.0
9          Jim   48.0    1.0   97.0   97.0     "A+"  60.75  243.0
10         Art   44.0    1.0   80.0   40.0     "D+"  41.25  165.0
11         Jim   47.0    1.0   23.0   45.0     "C+"  29.00  116.0
12         Ima   45.0    1.0   78.0   77.0     "B-"  50.25  201.0
13       Benny   50.0    1.0   90.0   90.0     "B-"  57.75  231.0
14         Boy   40.0    1.0   11.0    4.0      "B"  14.00   56.0
15      Harvey   30.0    1.0   20.0   40.0      "C"  22.75   91.0
"""
