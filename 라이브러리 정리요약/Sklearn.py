import sklearn
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

dic = {'city': ['서울', '부산', '대전', '대구', '광주'],
       'year': [2017, 2017, 2018, 2018, 2018],
       'temp': [18, 20, 19, 21, 20]}
data= pd.DataFrame(dic)
data.index = ['a', 'b', 'c', 'd', 'e']


housing = fetch_california_housing()
print(housing.data.shape, housing.target.shape)

X_train, X_test, y_train, y_test = train_test_split(housing.data[:, 0:1], 
                                                    housing.target, random_state=42)
print(X_train.shape, X_test.shape, \
      y_train.shape, y_test.shape)

lr = LinearRegression()
lr.fit(X_train, y_train)
lr.score(X_test, y_test)

print(lr.coef_, lr.intercept_)

plt.scatter(X_train, y_train)
plt.plot([0, 10], [lr.intercept_, 10 * lr.coef_ + lr.intercept_], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

                                            


num_attribs = df.select_dtypes(include=[np.number])
cat_attribs = df.select_dtypes(include=[np.object])

from sklearn.compose import ColumnTransformer
full_pipeline = ColumnTransformer([
        ("num_pipeline", num_pipeline, num_attribs),
        ("cat_encoder", OneHotEncoder(categories='auto'), cat_attribs),
    ])
