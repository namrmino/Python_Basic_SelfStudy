import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn
import numpy as np
import seaborn as sns

np.random.seed(42)
x = np.random.randint(1, 7, 10000)
plt.hist(x, bins = 6, width = 0.6)


# 소득 카테고리 개수를 제한하기 위해 1.5로 나눕니다.
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
# 5 이상은 5로 레이블합니다.
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
housing["income_cat"].value_counts()
housing["income_cat"].hist()


# 코드 1-8. 변수를 막대 그래프로 시각화하기
skip_cols = ['ncodpers', 'renta']
for col in trn.columns:
    # 출력에 너무 시간이 많이 걸리는 두 변수는 skip
    if col in skip_cols:
        continue        
    # 보기 편하게 영역 구분 및 변수명 출력
    print('='*50)
    print('col : ', col)    
    # 그래프 크기 (figsize) 설정
    f, ax = plt.subplots(figsize=(20, 15))
    # seaborn을 사용한 막대그래프 생성
    sns.countplot(x=col, data=trn, alpha=0.5)
    # show() 함수를 통해 시각화
    plt.show()

#
sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))
plt.plot(x, y, 'b')
ax.tick_params(labelsize=14)
plt.xlim([-1,1000])
plt.ylim([0,3.0])
_ = ax.set_xlabel('x', fontsize=14)
_ = ax.set_ylabel('log10(x)', fontsize=14)


#
plt.plot(X, y, "b.")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([0, 2, 0, 15])
save_fig("generated_data_plot")
plt.show()