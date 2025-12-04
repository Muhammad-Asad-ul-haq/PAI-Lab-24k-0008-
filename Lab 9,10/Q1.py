import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ==========================================
# 1. DATA PREPARATION
# ==========================================
# Input data
X = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7]) # YearsExperience
y = np.array([39.0, 46.0, 47.0, 52.0, 56.0, 64.0, 65.0, 67.0, 68.0, 70.0]) # Salary

# Value to predict
x_new = 4.5

print("========== DATASET ==========")
print("Experience (X):", X)
print("Salary (y):", y)
print("")


# ==========================================
# 2. METHOD A: FROM SCRATCH (The Math)
# ==========================================
print("========== METHOD A: FROM SCRATCH ==========")

# Step 1: Calculate Means
x_mean = np.mean(X)
y_mean = np.mean(y)

# Step 2: Calculate Slope (m)
# Formula: m = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean)^2)
numerator = np.sum((X - x_mean) * (y - y_mean))
denominator = np.sum((X - x_mean) ** 2)
m_scratch = numerator / denominator

# Step 3: Calculate Intercept (b)
# Formula: b = y_mean - (m * x_mean)
b_scratch = y_mean - (m_scratch * x_mean)

# Step 4: Make Prediction
y_pred_scratch = m_scratch * x_new + b_scratch

# Step 5: Calculate R-squared
# Formula: R² = 1 - (SS_res / SS_tot)
# SS_res: Sum of Squares Residuals (variance of error)
# SS_tot: Total Sum of Squares (variance of data)
y_fitted = m_scratch * X + b_scratch
ss_res = np.sum((y - y_fitted) ** 2)
ss_tot = np.sum((y - y_mean) ** 2)
r2_scratch = 1 - (ss_res / ss_tot)

print("Slope (m):", round(m_scratch, 4))
print("Intercept (b):", round(b_scratch, 4))
print("Prediction for " + str(x_new) + " years:", round(y_pred_scratch, 4), "k")
print("R2 Score:", round(r2_scratch, 4))
print("")


# ==========================================
# 3. METHOD B: SCIKIT-LEARN (The Standard Way)
# ==========================================
print("========== METHOD B: SCIKIT-LEARN ==========")

# Reshape X to 2D array (required by sklearn) -> [[1.1], [1.3], ...]
X_reshaped = X.reshape(-1, 1)

# Initialize and Fit
model = LinearRegression()
model.fit(X_reshaped, y)

# Get parameters
m_sklearn = model.coef_[0]
b_sklearn = model.intercept_

# Predict
y_pred_sklearn = model.predict([[x_new]])[0]

# Calculate R²
# Note: standard approach is model.score(X, y) or r2_score(y_true, y_pred)
r2_sklearn = r2_score(y, model.predict(X_reshaped))

print("Slope (m):", round(m_sklearn, 4))
print("Intercept (b):", round(b_sklearn, 4))
print("Prediction for " + str(x_new) + " years:", round(y_pred_sklearn, 4), "k")
print("R2 Score:", round(r2_sklearn, 4))
