import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ==========================================
# 1. DATA PREPARATION
# ==========================================
# Height (X) in cm
X = np.array([150, 155, 160, 165, 170, 175, 180]).reshape(-1, 1)

# Weight (y) in kg
y = np.array([50, 55, 60, 63, 68, 72, 75])

# Height to predict
x_new = [[172]]

print("========== DATASET ==========")
print("Height (X):", X.flatten())
print("Weight (y):", y)
print("")

# ==========================================
# 2. MODEL FITTING
# ==========================================
model = LinearRegression()
model.fit(X, y)

m = model.coef_[0]
b = model.intercept_
r2 = r2_score(y, model.predict(X))

print("========== MODEL RESULTS ==========")
print("Slope (m):", round(m, 4))
print("Intercept (b):", round(b, 4))
print("R2 Score:", round(r2, 4))
print("Equation: Weight =", round(m, 4), "* Height +", round(b, 4))
print("")

# ==========================================
# 3. PREDICTION
# ==========================================
pred_weight = model.predict(x_new)[0]
print("========== PREDICTION ==========")
print("Predicted weight for 172 cm:", round(pred_weight, 2), "kg")
print("")

# ==========================================
# 4. RESIDUAL ANALYSIS
# ==========================================
# Calculate predictions for all data points
y_pred_all = model.predict(X)

# Calculate Residuals (Actual - Predicted)
residuals = y - y_pred_all

print("========== RESIDUAL ANALYSIS ==========")
print("Residuals (Errors):", np.round(residuals, 2))
print("Mean of Residuals:", round(np.mean(residuals), 4))
print("")
print("INTERPRETATION:")
print("1. If the model is good, residuals should be randomly scattered around 0.")
print("2. If you see a U-shape or curve pattern, a linear model might not be best.")
print("3. Here, look at the plot to verify.")

# ==========================================
# 5. PLOTTING
# ==========================================
plt.figure(figsize=(12, 5))

# Plot 1: Regression Line vs Data
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred_all, color='red', label='Regression Line')
plt.scatter(x_new, pred_weight, color='green', marker='X', s=100, label='Prediction (172cm)')
plt.title('Height vs Weight Linear Regression')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.grid(True)

# Plot 2: Residuals
plt.subplot(1, 2, 2)
plt.scatter(X, residuals, color='purple')
plt.axhline(y=0, color='black', linestyle='--')
plt.title('Residual Plot (Errors)')
plt.xlabel('Height (cm)')
plt.ylabel('Residuals (kg)')
plt.grid(True)

plt.tight_layout()
plt.show()
