import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Initialize empty lists to store time and MSD data
time = []
msd = []

# Open the file and read data, skipping the title line
with open('msd.xvg', 'r') as f:
    lines = f.readlines()[1:]  # Skip the first line (title line)
    for line in lines:
        columns = line.split()
        if len(columns) == 2:  # Check if the line has two columns
            try:
                time.append(float(columns[0]))
                msd.append(float(columns[1]))
            except ValueError:
                pass  # Skip lines that cannot be parsed as floats

# Convert lists to numpy arrays
time = np.array(time)
msd = np.array(msd)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(time, msd)

# Calculate diffusion coefficient (D = slope / 6)
diffusion_coefficient = slope / 6

# Plot MSD data and fitted line
plt.plot(time, msd, label='MSD')
plt.plot(time, slope * time + intercept, label='Fitted line')
plt.xlabel('Time (ps)')
plt.ylabel('MSD (nm^2)')
plt.legend()
plt.title(f'Diffusion Coefficient: {diffusion_coefficient:.4f} nm^2/ps')
plt.show()

print(f'Diffusion Coefficient: {diffusion_coefficient:.4f} nm^2/ps')
print(f'Standard Error: {std_err:.4f}')

