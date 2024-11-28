#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Load GROMACS module (adjust this based on your HPC environment)
module load gromacs
source /usr/local/gromacs/bin/GMXRC

# Define file names and paths
INPUT_GRO=input.gro
TOPOL=topol.top
INDEX=index.ndx
MDP_MIN=minim.mdp
MDP_EQ=nvt.mdp
MDP_PROD=md.mdp
OUTPUT_DIR=output

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Step 1: Energy Minimization
echo Running energy minimization...
gmx_mpi grompp -f $MDP_MIN -c $INPUT_GRO -p $TOPOL -o $OUTPUT_DIR/em.tpr
gmx_mpi mdrun -v -deffnm $OUTPUT_DIR/em

# Step 2: NVT Equilibration
echo Running NVT equilibration...
gmx_mpi grompp -f $MDP_EQ -c $OUTPUT_DIR/em.gro -p $TOPOL -o $OUTPUT_DIR/nvt.tpr
gmx_mpi mdrun -deffnm $OUTPUT_DIR/nvt

# Step 3: NPT Equilibration (if applicable)
echo Running NPT equilibration...
gmx_mpi grompp -f $MDP_EQ -c $OUTPUT_DIR/nvt.gro -p $TOPOL -o $OUTPUT_DIR/npt.tpr
gmx_mpi mdrun -deffnm $OUTPUT_DIR/npt

# Step 4: Production MD
echo Running production MD...
gmx_mpi grompp -f $MDP_PROD -c $OUTPUT_DIR/npt.gro -p $TOPOL -o $OUTPUT_DIR/md.tpr
gmx_mpi mdrun -deffnm $OUTPUT_DIR/md

# Step 5: Post-processing
echo Post-processing and analysis...
gmx_mpi trjconv -s $OUTPUT_DIR/md.tpr -f $OUTPUT_DIR/md.xtc -o $OUTPUT_DIR/md_noPBC.xtc -pbc mol -center
gmx_mpi rms -s $OUTPUT_DIR/md.tpr -f $OUTPUT_DIR/md_noPBC.xtc -o $OUTPUT_DIR/rmsd.xvg -tu ns
gmx_mpi gyrate -s $OUTPUT_DIR/md.tpr -f $OUTPUT_DIR/md_noPBC.xtc -o $OUTPUT_DIR/gyrate.xvg

echo MD simulation completed successfully.

