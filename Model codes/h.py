import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Generate synthetic data for SST and SSS
np.random.seed(42)
years = np.arange(1871, 2011)
sst = 20 - 0.02 * (years - 1871) + np.random.normal(0, 1, len(years))
sss = 35 - 0.01 * (years - 1871) + np.random.normal(0, 0.5, len(years))

# Combine SST and SSS into a single array for modeling
data = np.vstack((sst, sss)).T

# Split the data into features (X) and target variables (y)
X = years.reshape(-1, 1)
y_sst = sst
y_sss = sss

# Split the data into training and testing sets
X_train, X_test, y_sst_train, y_sst_test, y_sss_train, y_sss_test = train_test_split(
    X, y_sst, y_sss, test_size=0.2, random_state=42
)

# Train Linear Regression model
linear_model_sst = LinearRegression()
linear_model_sst.fit(X_train, y_sst_train)

linear_model_sss = LinearRegression()
linear_model_sss.fit(X_train, y_sss_train)

# Train Decision Tree Regressor model
dt_model_sst = DecisionTreeRegressor(random_state=42)
dt_model_sst.fit(X_train, y_sst_train)

dt_model_sss = DecisionTreeRegressor(random_state=42)
dt_model_sss.fit(X_train, y_sss_train)

# Train Random Forest Regressor model
rf_model_sst = RandomForestRegressor(random_state=42)
rf_model_sst.fit(X_train, y_sst_train)

rf_model_sss = RandomForestRegressor(random_state=42)
rf_model_sss.fit(X_train, y_sss_train)

# Predict SST and SSS for the next 5 years
future_years = np.arange(2011, 2016).reshape(-1, 1)

linear_predictions_sst = linear_model_sst.predict(future_years)
linear_predictions_sss = linear_model_sss.predict(future_years)

dt_predictions_sst = dt_model_sst.predict(future_years)
dt_predictions_sss = dt_model_sss.predict(future_years)

rf_predictions_sst = rf_model_sst.predict(future_years)
rf_predictions_sss = rf_model_sss.predict(future_years)

# Plot the predictions
plt.figure(figsize=(12, 8))

# SST predictions
plt.subplot(2, 1, 1)
plt.scatter(X, y_sst, color='blue', label='Actual SST')
plt.plot(future_years, linear_predictions_sst, label='Linear Regression', linestyle='--', marker='o')
plt.plot(future_years, dt_predictions_sst, label='Decision Tree Regressor', linestyle='--', marker='o')
plt.plot(future_years, rf_predictions_sst, label='Random Forest Regressor', linestyle='--', marker='o')
plt.title('Sea Surface Temperature (SST) Prediction')
plt.xlabel('Year')
plt.ylabel('SST')
plt.legend()

# SSS predictions
plt.subplot(2, 1, 2)
plt.scatter(X, y_sss, color='red', label='Actual SSS')
plt.plot(future_years, linear_predictions_sss, label='Linear Regression', linestyle='--', marker='o')
plt.plot(future_years, dt_predictions_sss, label='Decision Tree Regressor', linestyle='--', marker='o')
plt.plot(future_years, rf_predictions_sss, label='Random Forest Regressor', linestyle='--', marker='o')
plt.title('Sea Surface Salinity (SSS) Prediction')
plt.xlabel('Year')
plt.ylabel('SSS')
plt.legend()

plt.tight_layout()
plt.show()
