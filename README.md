
# Aerodynamic Optimization Project using SU2

## Overview
This project performs aerodynamic simulations and shape optimization using the **SU2 Computational Fluid Dynamics (CFD) solver**.

The goal of this project is to analyze and optimize aerodynamic performance for:

- NACA0012 airfoil
- ONERA M6 wing
- NREL wind turbine blade
- Winglet configuration

The project includes CFD simulations, mesh deformation, adjoint sensitivity analysis, and optimization.

---

## Software Requirements

To run this project you need:

- SU2 CFD Solver
- Python 3
- Python libraries:
  - numpy
  - pandas
  - matplotlib

Optional:
- ParaView (for viewing CFD results)

---

## Project Folder Structure

### Root Directory
Contains scripts used to run simulations and optimizations.

Important files:

- run_su2_simulations.bat – runs SU2 simulations
- run_all_optimizations.bat – runs all optimization cases
- run_su2_simple.bat – runs a simple test case
- test.cfg – example SU2 configuration

---

## configs/
Contains SU2 configuration files used for CFD simulations.

Each `.cfg` file defines:
- Flow conditions
- Solver settings
- Mesh input
- Optimization parameters

Examples:
- naca0012.cfg → NACA airfoil simulation
- onera_m6.cfg → ONERA wing simulation
- nrel.cfg → NREL turbine simulation
- winglet.cfg → winglet simulation

---

## meshes/
Contains mesh files used by the CFD solver.

Mesh format: `.su2`

Subfolders include:
- naca0012 – mesh for NACA airfoil simulations
- onera_m6 – mesh for ONERA M6 wing simulations
- nrel – mesh for NREL wind turbine simulations
- winglet – mesh for winglet simulations

---

## optimization/
Contains scripts used for aerodynamic shape optimization.

Optimization algorithm used:
**SLSQP (Sequential Least Squares Programming)**

Main scripts:
- run_slsqp_optimization.py
- run_slsqp_clean.py

These scripts perform:
1. CFD simulation
2. Sensitivity calculation
3. Geometry deformation
4. Optimization iteration

---

## optimization/ffd_boxes/
Contains Free Form Deformation (FFD) box definitions.

Examples:
- naca0012_ffd.txt
- onera_m6_ffd.txt

FFD boxes define the control points used to deform the geometry.

---

## results/
Stores simulation and optimization results.

### figures
Contains generated plots such as:
- drag convergence plots
- pressure coefficient plots
- Mach contour plots

### data
Contains CSV files storing optimization history.

Example:
`optimization_history.csv`

---

## results/vtu_files/
Contains CFD result files in `.vtu` format.

These files can be opened using ParaView.

They contain:
- pressure fields
- velocity fields
- Mach contours

---

## scripts/
Contains helper scripts for:
- checking results
- visualizing simulation outputs
- plotting aerodynamic data

---

## Running Simulations

1. Open the project folder.
2. Run the following file:

run_su2_simulations.bat

This runs the SU2 solver for all test cases.

---

## Running Optimization

To run optimization manually:

python optimization/run_slsqp_optimization.py

This script will:
1. Run CFD simulation
2. compute sensitivities
3. deform the geometry
4. update design variables
5. repeat until convergence

---

## Generating Results

To generate plots and figures:

python results/generate_all_figures.py

This creates:
- drag convergence plots
- pressure distribution plots
- optimization history graphs

---

## Visualization

Open `.vtu` files in ParaView from:

results/vtu_files/

These files allow visualization of:
- pressure distribution
- velocity fields
- Mach contours

---
##Computational Time Analysis

All the models were executed in MATLAB, taking approximately 50–60 seconds, whereas the simulations in SU2 and the visualization in ParaView required about 20–25 minutes.
---
## Summary

This project demonstrates a complete aerodynamic optimization workflow:

1. Geometry generation
2. Mesh creation
3. CFD simulation using SU2
4. Shape optimization
5. Result visualization

Test cases included:
- NACA0012 airfoil
- ONERA M6 wing
- NREL wind turbine
- Winglet configuration
