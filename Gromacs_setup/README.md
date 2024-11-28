This repository provides a single script, md_setup.sh, that automates the process of running the molecular dynamics (MD) simulations using GROMACS. The primary focus is on applying periodic boundary conditions (PBC) and calculating global properties such as the Radius of Gyration (Rg) and Root Mean Square Deviation (RMSD).

The script will perform the following actions:
  Energy minimization: To prepare the system.
  Application of PBC: Setting up PBC.
  MD simulation: Running the MD simulation.
  Analysis: Automatically calculating the Rg and RMSD.

Running the MD simulation 

Step 1: Make the script executable
Before running the script, make sure it is executable by running 

  chmod +x md_setup.sh

Step 2: Run the script
Run the whole simulation and analysis

  ./md_setup.sh

Step 3: Visualization
Once the script completes, you will have output files (rmsd.xvg, rg.xvg) ready for visualization. You can use a tool like xmgrace to plot the results: 

xmgrace rmsd.xvg rg.xvg
