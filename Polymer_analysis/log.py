import numpy as np

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

# Save the results to a text file
np.savetxt("log_data.txt", np.column_stack((log_time, log_msd)), header="Log(time) Log(MSD)", fmt="%.6f")

# Print a confirmation message
print("Logarithmic transformation saved to log_data.txt")

