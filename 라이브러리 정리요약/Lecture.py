"""
웹 크롤링 크롤링 차이
matplotlib
히스토그램, 박스플롯, 산포도
Nan
해피캠퍼스
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
from numpy.random import randn

n = 10000
x = np.random.rand(n)
y = np.random.rand(n)

plt.figure(figsize=(6,6))
plt.scatter(x,y, s=1)
xx = np.linspace(0,1,100)
plt.plot(xx, (1-xx*xx) ** 0.5, c='r')
pi = ((x**2+ y**2) <1).mean()*4

#
x = np.random.randint(1, 7, 10000)
plt.hist(x, bins = 6, width = 0.6)

#
z = 0
n = 2
for i in range(n):
    x = np.random.randint(1, 7, 10000)
    z = z +x
plt.hist(z, bins = n*5+1, width = 0.6)
plt.show()

np.random.randn(3)
x = np.random.randn(100000)
plt.hist(x, bins = 100, width = 0.03)
plt.show()

"""
df1 = pd.read_csv('cu.csv')
df1 = df1.dropna(how="any")
df1.info

df2 = pd.read_csv('weather.csv')
df2 = df2.dropna(how="any")
df2.info

df3 = pd.read_csv('lala.csv')
df3.info
df3["X"].isnull().value_counts()
pd.DataFrame.isnull(df3).value_counts()
"""

#
data = np.arange(12).reshape(4,3)
data[:2,1:]
print(data * 3)
print(data + 100)

li = [1, 2, 10]
print(li * 3)
arr = np.array(li)

data.mean()
data.mean(axis=0) # 열기준
data.mean(axis=1) # 행기준

data[data < 4] = 0
data < 4 # T, F

#
dic = {'city': ['서울', '부산', '대전', '대구', '광주'],
       'year': [2017, 2017, 2018, 2018, 2018],
       'temp': [18, 20, 19, 21, 20]}
data= pd.DataFrame(dic)
data.index = ['a', 'b', 'c', 'd', 'e']
data.colunms = ['도시', '연도', '날씨']

data.set_index(['city'], inplace=True)
data.loc['서울']
data.iloc[1:2]

cars = [50, 40, 20, 30, 10]
data['car'] = cars
data.drop('car', 1)

f = lambda x: x.max() - x.min()

df = pd.DataFrame(np.arange(12).reshape(4, 3),
                  columns = ['A', 'B', 'C'],
                  index = ['a', 'b', 'c', 'd'])
f = lambda x: x.max() - x.min()
df.apply(f)
df.apply(f)

s = pd.Series(dic)

# 겹치기
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

ax1.hist(np.random.randn(200), bins=20,
        color='k', rwidth=0.5)
ax2.scatter(np.arange(30), np.arange(30) +
            3*np.random.randn(30))
ax3.plot(np.arange(10), np.random.randn(10))
fig

ax1.hist(np.random.randn(200), bins=20,
        color='k', rwidth=0.5)
ax2.scatter(np.arange(30), np.arange(30) +
            3*np.random.randn(30))
ax3.plot(np.arange(10), np.random.randn(10))
fig

# 2*2 개의 그림
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500),
        bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)

# 1000개의 랜덤넘버의 누적 값을 그리는 예
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum(), 'k',
        label='one')
ax.plot(randn(1000).cumsum(), 'k--',
        label='two')
ax.plot(randn(1000).cumsum(), 'k.',
        label='three')
ax.legend(loc='best')

# 막대그래프를 서브그래프를 이용
fig, axes = plt.subplots(2, 1)
data = Series(np.random.rand(16),
             index = list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0], color='k',
          alpha=0.9)
data.plot(kind='barh', ax=axes[1], color='k',
          alpha=0.7)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0.2, 0.75), 0.5, 0.2,
                     color='k', alpha=0.3)
## (0.2, 0.75) 사각형의 시작점이 0.5 가로길이 0.2세로길이
circ = plt.Circle((0.7, 0.2), 0.15, color='b',
                  alpha=0.3)
## (0,7,0,2) 원의 중심 / 0.15 원의 반지를
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4],
                    [0.2, 0.6]], color='g', alpha=0.5)
# 꼭지점의 좌표
    
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

# 데이터프레임으로부터 막대그래프
df = DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns=pd.Index(['A', 'B', 'C', 'D'],
                                name='Genus'))
df.plot(kind='bar')
df.plot(kind='barh', stacked=True)

comp1 = np.random.normal(0, 1, size=200) #N(0,1)
comp2 = np.random.normal(10, 2, size=200) #(10,4)
values = Series(np.concatenate([comp1, comp2]))
# concat(1,2) -1번째 문자열에 두번째 문자열을 합치는 함수
values.hist(bins=100, alpha=0.3, color='k', density=True)
values.plot(kind='kde', style='k--')

## 109
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index() # replace F

frame = DataFrame(np.arange(8).reshape((2,4)),
                  index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
frame.sort_index()
frame.sort_index(1) # 열
frame.sort_index(axis=1, ascending=False)

frame2 = DataFrame({'b': [4, 7, 3, 2], 'a': [4, 9, 2, 5], 'c': [5, 3, 7, 9]})
frame2.sort_values(by='a')

obj = Series([100, 23, 100, 44, 22, 99, 33])
obj.rank(ascending=False)
obj.rank()
obj.rank(method='first')

frame3 = DataFrame({'b': [4, 7, 3, 2], 'a':[4, 9, 2, 5],
                   'c': [5, 3, 7, np.nan]})
frame3.rank(axis=1)
frame3.sum()
frame3.mean()

frame3.sum(skipna=False)
frame3.idxmax() # 최대치가 있는 인댁스값
frame3.idxmin()

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
ubiques = obj.unique()
obj.value_counts
obj.value_counts(sort=False)

mask = obj.isin(['b', 'c'])
obj[mask] # True인 값만 출력

obj[obj.isin(['b', 'c'])]
frame4 = DataFrame({'X': ['c', 'a', 'd' ,'a', 'a', 'b', 'b', 'c', 'c'],
                    'Y': ['f', 'g', 'd', 'g', 'h', 'e', 'd', 'h', 'f'],
                    'Z': ['a', 'e', 'd', 'g', 'd', 'e', 'q', 'b', 'c']})
frame4.apply(pd.value_counts)
frame4.apply(pd.value_counts).fillna(0)

frame5 = DataFrame([[np.nan, 6.5, 3.], [np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
frame5.dropna()
frame5.dropna(how='all')
frame5.dropna(axis=1)
frame5.dropna(axis=1,how='all')

frame6 = DataFrame(np.random.randn(7, 3))
frame6.iloc[:4, 1] = np.nan
frame6.iloc[:2, 2] = np.nan
frame6.iloc[0,0] = np.nan
frame6.dropna(thresh=2) # more than 2 -> drop
frame6.fillna({1:0.5, 2: -1}) # 1열 = 0.5 / 2열 = -1