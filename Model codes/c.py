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

# Calculate seasonal averages for February to April and October to December
seasons = ['Feb-Apr', 'Oct-Dec']
seasonal_temperature = [temperature_2d[:, 1:4], temperature_2d[:, 9:12]]
seasonal_salinity = [salinity_2d[:, 1:4], salinity_2d[:, 9:12]]

# Create subplots for temperature and salinity in one graph only
fig, ax1 = plt.subplots(figsize=(12, 8))
fig.suptitle('Seasonal Variations of Temperature and Salinity (Surface)', fontsize=16)

# Plot Temperature for Feb-Apr
ax1.plot(years[:seasonal_temperature[0].shape[0]].flatten(), seasonal_temperature[0].mean(axis=1), label='Temperature (Feb-Apr)', color='blue')

# Plot Salinity for Feb-Apr
ax1.plot(years[:seasonal_salinity[0].shape[0]].flatten(), seasonal_salinity[0].mean(axis=1), label='Salinity (Feb-Apr)', color='red')

# Customize the plot
ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature (°C) / Salinity')
ax1.legend()
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Create a new plot for October to December
fig, ax2 = plt.subplots(figsize=(12, 8))
fig.suptitle('Seasonal Variations of Temperature and Salinity (Surface)', fontsize=16)

# Plot Temperature for Oct-Dec
ax2.plot(years[:seasonal_temperature[1].shape[0]].flatten(), seasonal_temperature[1].mean(axis=1), label='Temperature (Oct-Dec)', color='blue')

# Plot Salinity for Oct-Dec
ax2.plot(years[:seasonal_salinity[1].shape[0]].flatten(), seasonal_salinity[1].mean(axis=1), label='Salinity (Oct-Dec)', color='red')

# Customize the plot
ax2.set_xlabel('Year')
ax2.set_ylabel('Temperature (°C) / Salinity')
ax2.legend()
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plots
plt.show()
