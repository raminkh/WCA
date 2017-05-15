# WCA
Simulation of WCA particles in 2d
$ lammps < in.wca
$ vmd final.lammps 
$ remove_lines.py N
$ python wca_analysis.py boxL

in.wca:
   - Runs the simulation of N WCA particles in a box of length boxL
   - Outputs final.lammps and traj.xyz 
   
remove_lines.py:
   - Reads traj.xyz and outputs a "cleaner" version of it, which is later read for postprocessing 

wca_analysis.py:
   - Takes the "cleaned up" traj.xyz and computes adjacency matrix, etc




