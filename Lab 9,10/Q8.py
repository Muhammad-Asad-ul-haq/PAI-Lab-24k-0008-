import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

try:
    df = pd.read_csv('house_prices.csv')
except:
    np.random.seed(0)
    n=300
    df = pd.DataFrame({
        'OverallQual':np.random.randint(1,10,n),
        'GrLivArea':np.random.normal(1500,500,n).clip(300,5000),
        'GarageCars':np.random.randint(0,4,n),
        'YearBuilt':np.random.randint(1900,2020,n)
    })
    df['SalePrice'] = 20000*df['OverallQual'] + 30*df['GrLivArea'] + 8000*df['GarageCars'] + 50*(df['YearBuilt']-1900) + np.random.normal(0,20000,n)

X = df[['OverallQual','GrLivArea','GarageCars','YearBuilt']]
y = df['SalePrice']

model = LinearRegression().fit(X,y)
print(model.intercept_, model.coef_)

y_pred = model.predict(X)
print(r2_score(y,y_pred))
print(mean_squared_error(y,y_pred, squared=False))

print(pd.Series(model.coef_, index=X.columns).abs().sort_values(ascending=False))
