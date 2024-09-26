Molecular Dynamics (MD) Simulation and Analysis 

This repository contains scripts and resources for MD simulations and polymer analysis using GROMACS and related tools.

Step 1: GROMACS Setup  
  This folder contains all necessary input files and scripts for setting up and running MD simulations using GROMACS. 
It includes:
  - md_Setup.sh: A script that automates MD setup with periodic boundary conditions (PBC), radius of gyration (Rg), and RMSD analysis.
  - Input parameter files (`.mdp`), topology files (`.top`), and structure files (`.gro`) are required for running the simulation.
  - Example commands and workflows for different simulation setups.
  - Post-simulation analysis like calculating Rg and RMSD

Step 2: Polymer Analysis
  This folder includes scripts and utilities for analyzing polymer systems, particularly focusing on:
  - Tools for analyzing the structural and dynamic properties of polymers.
  - Post-simulation analysis like calculating MSD and diffusion coefficients.
  - Scripts for visualizing polymer behaviour over time.
