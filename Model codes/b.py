import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for temperature and salinity
years = np.arange(1883, 2023)  # Assuming data spans 140 years
data_points = 12 * (years.shape[0] // 12)  # Ensure divisibility by 12
years = years[:data_points]  # Trim years to match data_points
temperature = 10 + 0.1 * (years - 1883) + np.random.normal(0, 1, data_points)
salinity = 35 - 0.02 * (years - 1883) + np.random.normal(0, 0.5, data_points)

# Reshape the data into 2D arrays for monthly climatology
temperature_2d = temperature.reshape(-1, 12)
salinity_2d = salinity.reshape(-1, 12)

# Calculate region-averaged climatological monthly values
region_averaged_temperature_monthly = np.mean(temperature_2d, axis=0)
region_averaged_salinity_monthly = np.mean(salinity_2d, axis=0)

# Create a bar plot for monthly climatology of temperature
months = np.arange(1, 13)
plt.figure(figsize=(10, 6))
plt.bar(months, region_averaged_temperature_monthly, color='blue')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Region-Averaged Climatological Monthly Temperature Variations')
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Create a bar plot for monthly climatology of salinity
plt.figure(figsize=(10, 6))
plt.bar(months, region_averaged_salinity_monthly, color='red')
plt.xlabel('Month')
plt.ylabel('Salinity')
plt.title('Region-Averaged Climatological Monthly Salinity Variations')
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Show the plots
plt.show()
