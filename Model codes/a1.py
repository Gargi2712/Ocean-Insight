import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for temperature and salinity
years = np.arange(1883, 2023)  # Assuming data spans 140 years
temperature = 10 + 0.1 * (years - 1883) + np.random.normal(0, 1, len(years))
salinity = 35 - 0.02 * (years - 1883) + np.random.normal(0, 0.5, len(years))

# Calculate region-averaged values
region_averaged_temperature = np.mean(temperature)
region_averaged_salinity = np.mean(salinity)

# Create the time series plot
plt.figure(figsize=(10, 6))
plt.plot(years, temperature, label='Temperature', color='blue')
plt.plot(years, salinity, label='Salinity', color='red')

# Add region-averaged values to the plot
plt.axhline(region_averaged_temperature, color='blue', linestyle='--', label='Avg. Temperature')
plt.axhline(region_averaged_salinity, color='red', linestyle='--', label='Avg. Salinity')

# Customize the plot
plt.xlabel('Year')
plt.ylabel('Temperature (°C) / Salinity')
plt.title('Region-Averaged Temperature and Salinity Over 140 Years')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
