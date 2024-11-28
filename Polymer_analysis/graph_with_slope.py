import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to calculate slope from Log(MSD) and Log(time) data
def calculate_slope(log_time, log_msd):
    slope, _, _, _, _ = linregress(log_time, log_msd)
    return slope

# Function to plot graph with slope value
def plot_graph_with_slope(filename):
    # Load data from file
    data = np.loadtxt(filename)

    # Extract Log(time) and Log(MSD) columns
    log_time = data[:, 0]
    log_msd = data[:, 1]

    # Calculate slope
    slope = calculate_slope(log_time, log_msd)

    # Plot Log(MSD) vs. Log(time)
    plt.plot(log_time, log_msd, marker='o', linestyle='-', label=f"Slope: {slope:.2f}")
    plt.xlabel('Log(time)')
    plt.ylabel('Log(MSD)')
    plt.title('Log-Log Plot of MSD vs Time')
    plt.legend()
    plt.grid(True)

# Plot graph for each file with slope value
files = ["log_data.txt"]
for file in files:
    plot_graph_with_slope(file)

# Show the plot
plt.show()

