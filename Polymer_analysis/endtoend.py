#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 calculate_end_to_end.py topology_file gro_file mdp_file output_dir")
        sys.exit(1)

    topology_file = sys.argv[1]
    gro_file = sys.argv[2]
    mdp_file = sys.argv[3]
    output_dir = sys.argv[4]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Set GROMACS environment variables directly
    os.environ['LD_LIBRARY_PATH'] = '/usr/local/gromacs/lib'
    os.environ['PATH'] = '/usr/local/gromacs/bin:' + os.environ['PATH']

    # Step 1: Prepare the system
    grompp_command = f'gmx_mpi grompp -f {mdp_file} -c {gro_file} -p {topology_file} -n index.ndx -o {output_dir}/md.tpr -maxwarn 10'
    subprocess.run(['/bin/bash', '-c', grompp_command], check=True, shell=False)

    # Step 2: Run the simulation
    mdrun_command = f'gmx_mpi mdrun -s {output_dir}/md.tpr -o {output_dir}/md.trr -x {output_dir}/md.xtc -c {output_dir}/md.gro -e {output_dir}/md.edr -v'
    subprocess.run(['/bin/bash', '-c', mdrun_command], check=True, shell=False)

    # Step 3: Analyze the trajectory to calculate end-to-end distance
    analyze_script = f"""
    #!/bin/bash
    source /usr/local/gromacs/bin/GMXRC
    echo "0 0" | gmx_mpi trjconv -s {output_dir}/md.tpr -f {output_dir}/md.xtc -o {output_dir}/md_noPBC.xtc -pbc nojump -center -n index.ndx
    echo "0 0" | gmx_mpi trjconv -s {output_dir}/md.tpr -f {output_dir}/md_noPBC.xtc -o {output_dir}/md_fit.xtc -fit rot+trans -n index.ndx
    echo "1 1" | gmx_mpi distance -s {output_dir}/md.tpr -f {output_dir}/md_fit.xtc -select 'com of group "Protein" plus com of group "Protein" plus 1' -oall {output_dir}/end_to_end.xvg -n index.ndx
    """

    with open(f"{output_dir}/analyze.sh", 'w') as f:
        f.write(analyze_script)

    analyze_command = f"bash {output_dir}/analyze.sh"
    subprocess.run(analyze_command, check=True, shell=True)

    print("End-to-end distance calculation completed.")

if __name__ == "__main__":
    main()

