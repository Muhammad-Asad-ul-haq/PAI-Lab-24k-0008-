import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

np.random.seed(0)
n=200
screen = np.random.uniform(0.5,8.0,size=n)
noise = np.random.normal(0,0.5,size=n)
battery = 15 - 1.2*screen + noise

df = pd.DataFrame({'ScreenOnHrs':screen,'BatteryHrs':battery})
X = df[['ScreenOnHrs']]
y = df['BatteryHrs']

model = LinearRegression().fit(X,y)
print(model.intercept_, model.coef_[0])

r,p = pearsonr(df['ScreenOnHrs'],df['BatteryHrs'])
print(r,p)
