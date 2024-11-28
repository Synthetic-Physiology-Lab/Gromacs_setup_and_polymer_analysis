#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def main():
    # Set default marker
    marker = '-'

    # Set font family
    plt.rcParams["font.family"] = "serif"
    rc('font', **{'family': 'serif', 'serif': ['Times New Roman', 'Times', 'DejaVu Serif', 'serif']})

    # Check if the correct number of arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python3 plot_rmsd.py <filename> [marker]")
        sys.exit(1)

    # Get filename from command line arguments
    fname = sys.argv[1]

    # Check if the provided file is in .xvg format
    if not fname.endswith(".xvg"):
        print("The provided file is not in .xvg format.")
        sys.exit(1)

    # Get marker type from command line arguments, default to '-' if not provided
    try:
        marker = sys.argv[2]
    except IndexError:
        marker = '-'

    # Read the file
    try:
        with open(fname, 'r') as fid:
            ll = fid.readlines()
    except FileNotFoundError:
        print(f"File {fname} not found.")
        sys.exit(1)

    # Initialize label list and data container
    labels = []
    data = []

    # Parse the file
    for line in ll:
        if line.startswith('@'):
            if 'label' in line:
                label = line.split('"')[1]
                labels.append(label)
        elif not line.startswith(('#', '@')):
            data.append([float(x) for x in line.split()])

    # Convert data to numpy array
    data = np.array(data)

    # Check the dimensions of the data array
    if data.shape[1] != 2:
        print(f"Error: Expected 2 columns of data, but found {data.shape[1]} columns.")
        sys.exit(1)

    # Plot the data
    plt.plot(data[:, 0], data[:, 1], marker, label=labels[1] if len(labels) > 1 else 'RMSD')
    plt.legend()
    plt.grid(visible=True, which='major', color='grey', linestyle='--')
    plt.xlabel('Time (ps)' if len(labels) == 0 else labels[0])
    plt.ylabel('RMSD (nm)' if len(labels) <= 1 else labels[1])
    plt.title(f'RMSD from \'{fname}\'')
    plt.show()

if __name__ == "__main__":
    main()

