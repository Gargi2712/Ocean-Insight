import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for temperature and salinity
np.random.seed(42)  # for reproducibility
years = np.arange(1871, 2011)
temperature = 15 + 0.1 * (years - 1871) + np.random.normal(0, 1, len(years))
salinity = 35 - 0.02 * (years - 1871) + np.random.normal(0, 0.5, len(years))

# Plot the T/S diagram
plt.figure(figsize=(10, 6))
plt.scatter(salinity, temperature, c=years, cmap='viridis', marker='o', edgecolors='k', alpha=0.7)
plt.colorbar(label='Year')
plt.title('Temperature-Salinity (T/S) Diagram (1871-2010)')
plt.xlabel('Salinity')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
