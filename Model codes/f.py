import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for Sea Surface Temperature (SST) and Sea Surface Salinity (SSS)
np.random.seed(42)  # for reproducibility
years = np.arange(1871, 2011)
sst = 15 + 0.1 * (years - 1871) + np.random.normal(0, 1, len(years))
sss = 35 - 0.02 * (years - 1871) + np.random.normal(0, 0.5, len(years))

# Plot the interannual variation in SST and SSS
plt.figure(figsize=(12, 6))

# SST plot
plt.subplot(2, 1, 1)
plt.plot(years, sst, marker='o', color='blue', label='SST')
plt.title('Interannual Variation in Sea Surface Temperature (SST)')
plt.xlabel('Year')
plt.ylabel('SST (°C)')
plt.grid(True)
plt.legend()

# SSS plot
plt.subplot(2, 1, 2)
plt.plot(years, sss, marker='o', color='red', label='SSS')
plt.title('Interannual Variation in Sea Surface Salinity (SSS)')
plt.xlabel('Year')
plt.ylabel('SSS')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
