import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

try:
    df = pd.read_csv('laptops.csv')
except:
    np.random.seed(0)
    n=300
    df = pd.DataFrame({
        'RAM':np.random.choice([4,8,16,32],n),
        'Weight':np.random.normal(2.0,0.5,n).clip(1.0,4.0),
        'CPU_GHz':np.random.normal(2.5,0.6,n).clip(1.0,5.0),
        'Storage':np.random.choice([128,256,512,1024],n)
    })
    df['Price'] = 50*df['RAM'] + 200*df['Storage']/128 + 150*df['CPU_GHz'] - 30*df['Weight'] + np.random.normal(0,100,n)

X = df[['RAM','Weight','CPU_GHz','Storage']]
y = df['Price']

model = LinearRegression().fit(X,y)
print(r2_score(y, model.predict(X)))

scaler = StandardScaler().fit(X)
Xs = scaler.transform(X)

model2 = LinearRegression().fit(Xs,y)
print(r2_score(y, model2.predict(Xs)))

print(model.coef_)
print(model2.coef_)
