import numpy as np
import matplotlib.pyplot as plt

# Load MSD and time data from msd.xvg file
data = np.loadtxt("msd.xvg", comments=["@", "#"])

# Extract time and MSD columns from the data
time_data = data[:, 0]
msd_data = data[:, 1]

# Filter out zero values
nonzero_indices = np.nonzero(msd_data)
time_data = time_data[nonzero_indices]
msd_data = msd_data[nonzero_indices]

# Calculate logarithm (base 10) of MSD and time
log_msd = np.log10(msd_data)
log_time = np.log10(time_data)

# Plot Log(MSD) vs. Log(time)
plt.plot(log_time, log_msd, marker='o', linestyle='-')
plt.xlabel('Log(time)')
plt.ylabel('Log(MSD)')
plt.title('Log-Log Plot of MSD vs Time')
plt.grid(True)
plt.show()

