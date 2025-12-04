import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

h = np.array([150,155,160,165,170,175,180]).reshape(-1,1)
w = np.array([50,55,60,63,68,72,75])

model = LinearRegression().fit(h,w)
print(model.intercept_, model.coef_[0])

print(float(model.predict(np.array([[172]]))))

plt.scatter(h,w)
xs = np.linspace(145,185,100).reshape(-1,1)
plt.plot(xs, model.predict(xs))
plt.savefig('plot_q3.png')

res = w - model.predict(h).flatten()
print(res.mean(), res.std())

plt.figure()
plt.hist(res)
plt.savefig('residuals_q3.png')
