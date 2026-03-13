# NACA Airfoil Aerodynamic Shape Optimization

## Overview

This project presents aerodynamic analysis of the **NACA0012 airfoil** using Computational Fluid Dynamics (CFD) and MATLAB simulations.  

The study is part of an **Aerodynamic Shape Optimization (ASO)** framework using the **Discrete Adjoint method and Radial Basis Function (RBF) mesh deformation** implemented in SU2.

The goal is to analyze airflow around the airfoil and evaluate aerodynamic performance using lift and drag coefficients.


## Team Members

| Name                          | Roll Number |
| ----------------------------- | ----------- |
| Amrutha Tammurothu            | CB.SC.U4AIE24255       |
| Bala Prasanna Kumar Telapolu | CB.SC.U4AIE24256       |
| Charan Tej Reddy Yammunuru    | CB.SC.U4AIE24259       |
| Poojitha Devineni             |CB.SC.U4AIE 24263       |
___
## Problem Statement

Aircraft performance depends strongly on aerodynamic efficiency.
Traditional airfoil designs may not achieve optimal drag‑to‑lift ratios
under different flight conditions. This project applies CFD‑based
optimization to improve airfoil performance.

Traditional design methods require many CFD simulations and are computationally expensive.  

Adjoint-based optimization allows efficient improvement of aerodynamic performance.


## Objectives

-   Analyze aerodynamic behavior of a NACA airfoil
-   Perform CFD simulation of airflow
-   Calculate lift and drag coefficients
-   Optimize airfoil shape to reduce drag
-   Maintain aerodynamic stability

## Methodology

### 1 Airfoil Geometry Generation
The NACA0012 airfoil coordinates are generated mathematically.

### 2 Mesh Generation
A computational mesh is generated around the airfoil with:

- structured boundary layer mesh
- unstructured outer domain mesh

### 3 CFD Simulation
The airflow is simulated using CFD solvers that solve the **Navier–Stokes equations**.

### 4 Aerodynamic Analysis
Key aerodynamic parameters are computed:

- Lift coefficient (CL)
- Drag coefficient (CD)
- Pressure coefficient (Cp)

---
## Tools & Technologies

-   SU2 (CFD Solver)
-    MATLAB
-   Free Form Deformation (FFD)
-   Radial Basis Function (RBF)
-   CFD Mesh Generation Tools


## Simulation Conditions

| Parameter | Value |
|----------|------|
| Mach Number | 0.76 |
| Angle of Attack | 2° |
| Reynolds Number | 6.04 × 10⁶ |
| Temperature | 215.38 K |

---


## Key Parameters

-   Lift Coefficient (CL)
-   Drag Coefficient (CD)
-   Pressure Distribution (Cp)
-   Mach Number
-   Reynolds Number

## Results

The optimization improves aerodynamic performance by reducing drag and
improving pressure distribution around the airfoil.

## Future Work

-   Extend optimization to 3D wings
-   Multi‑objective optimization
-   Wind turbine blade optimization
-   Machine learning based aerodynamic prediction

## Applications

-   Aircraft wing design
-   UAV and drone aerodynamics
-   Wind turbine blade optimization
-   Automotive aerodynamics

## Conclusion

This project demonstrates the use of CFD and adjoint‑based optimization
techniques to improve aerodynamic performance of NACA airfoils.
