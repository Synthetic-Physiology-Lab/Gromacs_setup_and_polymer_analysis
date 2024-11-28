# Mean Squared Displacement (MSD) Analysis Scripts
## Overview
This repository contains scripts and tools for performing Mean Squared Displacement (MSD) analysis on particle trajectory data. MSD analysis is commonly used in the study of particle diffusion and dynamics.
## File structure
- `msd.py`: Computes Mean Squared Displacement (MSD) from trajectory data.
- `log.py`: Performs logarithmic transformation on MSD data.
- `logvalue.py`: Calculates logarithmic values for MSD data points.
- `slope.py`: Computes slope values from MSD data points.
- `graphwithslope.py`: Plots MSD data with slope calculations.
## Features
- Calculation of MSD for single particles or particle ensembles
- Plotting tools for visualizing MSD data
- Integration with common trajectory file formats (e.g., xvg, xvg)
## Installation
1. Clone the repository:
git clone https://github.com/drsaranya/Polymer-analysis.git
## Run gromacs MSD calculation
gmx_mpi msd -f md.xtc -s md.tpr -o msd_results.xvg -tu ns -n index.ndx 
## Usage
### msd.py
1. Calculate MSD:
python3 msd.py --input trajectory.xvg --output msd_results.xvg
- Replace `trajectory.xvg` with your input trajectory file.
- Outputs MSD results to `msd_results.xvg`.
### log.py
2. Perform logarithmic transformation:
python3 log.py --input msd_results.xvg --output transformed_msd.xvg
- Replace `msd_results.xvg` with your MSD results file.
- Outputs a transformed MSD file `transformed_msd.xvg`.
### logvalue.py
3. Calculate logarithmic values:
python3 logvalue.py --input transformed_msd.xvg --output log_values.xvg
- Use `transformed_msd.xvg` from `log.py` as input.
- Outputs logarithmic values to `log_values.xvg`.
### slope.py
4. Compute slope values:
python3 slope.py --input log_values.xvg --output slope_values.xvg
- Calculates slopes from `msd_results.xvg`.
- Outputs slope values to `slope_values.xvg`.
### graphwithslope.py
5. Plot MSD with slope:
python3 graphwithslope.py --input log_values.xvg --slope slope_values.xvg --output msd_plot_with_slope.png
- Generates a plot of MSD data with slope annotations.
- Uses `log_values.xvg` for MSD data and `slope_values.xvg` for slope calculations.
- Outputs the plot `msd_plot_with_slope.png`.
