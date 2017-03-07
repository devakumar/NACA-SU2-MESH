#!/bin/bash

# ARG1 - NACA airfoil series (Only numbers , without naca prefix)
# ARG2 - no of NACA points
# ARG3 - SU2 file name to be written

mkdir "naca$1"

# Generate NACA profile
echo "Generating naca$1.txt file using naca.py"
python naca.py -p $1 -n $2 -s > "naca$1/naca$1.txt"

# Generate Gmsh geo file and create airfoil & farfiled
echo "Generating naca$1.geo file using txttogeo.py"
python txttogeo.py -i "naca$1/naca$1.txt" -n 2 -f 10 -N 20 > "naca$1/naca$1.geo"

# Create Gmsh output file
echo "Meshing ....Generating naca$1.su2 file using gmsh"
gmsh "naca$1/naca$1.geo" -2 -o "naca$1/naca$1.su2" -format su2 -saveall > gmshout
