import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7]).reshape(-1,1)
y = np.array([39.0,46.0,47.0,52.0,56.0,64.0,65.0,67.0,68.0,70.0])

x_mean = x.mean()
y_mean = y.mean()
num = ((x - x_mean)*(y - y_mean)).sum()
den = ((x - x_mean)**2).sum()
b1 = (num/den).item()
b0 = (y_mean - b1*x_mean).item()
print(b0, b1)

xr = np.array([[4.5]])
print(float(b0 + b1*xr))

model = LinearRegression().fit(x,y)
print(model.intercept_, model.coef_[0])
print(model.predict(xr)[0])

ss_tot = ((y - y_mean)**2).sum()
ss_res = ((y - (b0 + b1*x.flatten()))**2).sum()
r2 = 1 - ss_res/ss_tot
print(r2)
