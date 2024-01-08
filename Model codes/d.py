import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for temperature and salinity
years = np.arange(1883, 2023)  # Assuming data spans 140 years
data_points = 12 * (years.shape[0] // 12)  # Ensure divisibility by 12
years = years[:data_points]  # Trim years to match data_points

# Generate synthetic data for temperature and salinity
temperature = 10 + 0.1 * (years - 1883) + np.random.normal(0, 1, data_points)
salinity = 35 - 0.02 * (years - 1883) + np.random.normal(0, 0.5, data_points)

# Reshape the data into 2D arrays for monthly climatology
temperature_2d = temperature.reshape(-1, 12)
salinity_2d = salinity.reshape(-1, 12)

# Define the seasons
seasons = ['Feb-Apr', 'Oct-Dec']

# Select data for the chosen seasons (Feb-Apr and Oct-Dec)
seasonal_temperature = [temperature_2d[:, 1:4], temperature_2d[:, 9:12]]
seasonal_salinity = [salinity_2d[:, 1:4], salinity_2d[:, 9:12]]

# Calculate the standard deviation profiles for temperature and salinity
std_dev_temperature = np.std(seasonal_temperature, axis=1, ddof=1)
std_dev_salinity = np.std(seasonal_salinity, axis=1, ddof=1)

# Create plots for standard deviation profiles
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
fig.suptitle('Standard Deviation Profile of Temperature and Salinity', fontsize=16)

# Plot Temperature for Feb-Apr and Oct-Dec
for i, season in enumerate(seasons):
    months = np.arange(1, 4) if i == 0 else np.arange(10, 13)
    axes[0].plot(months, std_dev_temperature[i], label=f'Temperature ({season})', marker='o', linestyle='-', linewidth=2)

axes[0].set_xlabel('Month')
axes[0].set_ylabel('Standard Deviation (°C)')
axes[0].set_title('Temperature Standard Deviation Profile')
axes[0].set_xticks(range(1, 4))
axes[0].legend()

# Plot Salinity for Feb-Apr and Oct-Dec
for i, season in enumerate(seasons):
    months = np.arange(1, 4) if i == 0 else np.arange(10, 13)
    axes[1].plot(months, std_dev_salinity[i], label=f'Salinity ({season})', marker='o', linestyle='-', linewidth=2)

axes[1].set_xlabel('Month')
axes[1].set_ylabel('Standard Deviation')
axes[1].set_title('Salinity Standard Deviation Profile')
axes[1].set_xticks(range(1, 4))
axes[1].legend()

# Show the plots
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
