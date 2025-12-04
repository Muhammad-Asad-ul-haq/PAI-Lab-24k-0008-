import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

h = np.array([150,155,160,165,170,175,180]).reshape(-1,1)
w = np.array([50,55,60,63,68,72,75])

model1 = LinearRegression().fit(h,w)
b0_1, b1_1 = model1.intercept_, model1.coef_[0]
r2_1 = r2_score(w, model1.predict(h))

h2 = np.vstack([h, np.array([[190]])])
w2 = np.hstack([w, np.array([60])])
model2 = LinearRegression().fit(h2,w2)

b0_2, b1_2 = model2.intercept_, model2.coef_[0]
r2_2 = r2_score(w2, model2.predict(h2))

print(b0_1, b1_1, r2_1)
print(b0_2, b1_2, r2_2)
