import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

try:
    df = pd.read_csv('fifa19.csv')
except:
    np.random.seed(0)
    n=500
    df = pd.DataFrame({
        'Overall':np.random.randint(50,95,n),
        'Potential':np.random.randint(50,95,n),
        'Age':np.random.randint(17,40,n),
        'InternationalReputation':np.random.randint(1,6,n)
    })
    df['Value'] = 1e5*df['Overall'] + 8e4*df['Potential'] - 2e3*df['Age'] + 5e4*df['InternationalReputation'] + np.random.normal(0,1e6,n)

X = df[['Overall','Potential','Age','InternationalReputation']]
y = df['Value']

model = LinearRegression().fit(X,y)
print(model.coef_)

model_no_pot = LinearRegression().fit(X.drop(columns=['Potential']), y)
print(model_no_pot.coef_)

print(r2_score(y, model.predict(X)))
print(r2_score(y, model_no_pot.predict(X.drop(columns=['Potential']))))
