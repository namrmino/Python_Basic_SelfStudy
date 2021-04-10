from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt
import re
import datetime

## DataFrame 생성, colunms, row, index 수
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
df.iloc[0,1] = np.NaN; df.iloc[2,3] = np.NaN

pd.to_excel('a.xlsx')
pd.to_csv('a.csv')
pd.read_csv('')
df = pd.read_excel('pdata.xlsx')
df = df.set_index('Date')

data = np.arange(12).reshape(4,3)
data[:2,1:]
print(data * 3)
print(data + 100)

# columns
dft = df.columns[2:].tolist()

list = [1, 2, 10]
print(list * 3)
arr = np.array(list)

# dictionary
dic = {'city': ['서울', '부산', '대전', '대구', '광주'],
       'year': [2017, 2017, 2018, 2018, 2018],
       'temp': [18, 20, 19, 21, 20]}
data= pd.DataFrame(dic)
data.index = ['a', 'b', 'c', 'd', 'e']
data.colunms = ['도시', '연도', '날씨']
data.set_index(['city'], inplace=True)

## 정보 추출
df.shape
df.describe()
df['W'].value_counts()

pd.DataFrame.info(df)
pd.DataFrame.mean(df, axis=0)
pd.DataFrame.mean(df, axis=1)
pd.DataFrame.std(df)
pd.DataFrame.isnull(df)

df_num = df.select_dtypes(include=[np.number])
df_num = df.select_dtypes(include=[np.object])

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(categories='auto'), cat_attribs),
    ])

## 읽기
df['W']
df[['W', 'Z']]
df['new'] = df['W'] + df['Y']

df.loc['C']; df.iloc[2]
df.loc['B', 'Y']
df.loc[['A', 'B'],['W', 'Y']]; df.iloc[[0,1],[0,2]]

df.iloc[1:3]

## 수정
# 열추
cars = [50, 40, 20, 30, 10]
data['car'] = cars
data['high'] = data.car  >= 30

f = lambda x: x.max() - x.min()
data.apply(f)
data.apply(f, 1)

df = pd.DataFrame(np.arange(12).reshape(4, 3),
                  colunms = ['A', 'B', 'C'],
                  index = ['a', 'b', 'c', 'd'])

data[data < 4] = 0
data < 4 # T, F

re.split('~', '2011.01.01~2011.12.31')
'2011.01.01'.replace('.', '-')
# 오름차순 정렬
calendar = calendar.sort_values(by=["year", "week"], ascending=True)
# 인덱스 초가화
calendar = calendar.reset_index(drop=True)
# 옆으로 붙이기
df_c = pd.concat([df_a.reset_index(drop=True), df_b], axis=1)
# Key기준 Inner Join
df_c = df_a.set_index('A').join(df_b.set_index('B'), how='inner').reset_index()
# 특정 칼럼 요약
df_b = df_a.groupby(['A', 'B'])['C'].mean()
# 밑으로 합치기
df_c = df_a.append(pd.DataFrame(data = df_b), ignore_index=True)

# 결측치 처리
df2 = df["v1"].dropna()
# 행 중에서 결측치가 하나라도 있으면 제거
df3 = df.dropna(how="any")
# 행 모든열 결측시 해당  제거
df4 = df.dropna(how="all")
# # 결측치를 0으로 대체
df5 = df.fillna(0)
# 결측치 index보다 한 단계 이전의 값으로 대체
df6 = df.fillna(method="pad")
# 결측치를 결측치가 있는 index보다 한 단계 후의 값으로 대체
df7 = df.fillna(method="bfill")
# 결측치를 결측치를 제외한 평균으로 대체
df8 = df.fillna(df.mean())

# 1: 열삭제
df.drop('new', axis=1, inplace=True)
# 0, NA: 열삭제
df.drop('E'); df.drop('E', axis=0) 

# reshape
x = np.arange(12).reshape(3, 4)
x.reshape(-1, 2)
x.reshape(3, -1)


## 결측치 판별
df["v1"].isnull()
df["v1"].isnull().value_counts()


df[(df['cdsStart'] > 10000) & (df['cdsEnd'] < 20000)]
df[df['E'].isin(['two', 'four'])]
'Helloworld!'.startswith('Hello world!')