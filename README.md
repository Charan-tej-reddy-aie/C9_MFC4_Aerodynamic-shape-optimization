**Aerodynamic shape optimization based on discrete adjoint and RBF**
___

**Overview**
---
This project develops a robust aerodynamic shape optimization framework by combining Discrete Adjoint methods with RBF-based mesh deformation to reduce drag while preserving mesh quality and using SU2 Software
___
**Team Members**
---

| Name                          | Roll Number |
| ----------------------------- | ----------- |
| Amrutha Tammurothu            | CB.SC.U4AIE24255       |
| Bala Prasanna Kumar Telapolu | CB.SC.U4AIE24256       |
| Charan Tej Reddy Yammunuru    | CB.SC.U4AIE24259       |
| Poojitha Devineni             |CB.SC.U4AIE 24263       |
___

**Project Outline**
---
**Problem**

Traditional aerodynamic shape optimization methods suffer from poor robustness and high computational cost due to inefficient mesh deformation techniques such as Linear Elasticity Analogy (ELA).

**Objective**

 - Reduce aerodynamic drag using adjoint-based optimization

 - Ensure accurate sensitivity computation

 - Maintain mesh quality during shape deformation

**Methodology**

Geometry parameterization using Free-Form Deformation (FFD)

Baseline CFD simulation using SU2

Sensitivity computation using Discrete Adjoint method

Mesh deformation using RBF interpolation

Elimination of volume mesh sensitivity using double adjoint approach

Performance evaluation using aerodynamic coefficients

**Tools & Technologies**

- SU2 (CFD & Adjoint Solver)

- FFD (Geometry Parameterization)

- RBF (Mesh Deformation)

- Euler / Navier–Stokes Solver

Gradient-based Optimization
___
**Current Updates**
---

 - Literature review completed

 - NACA0012 airfoil geometry validated

 - Baseline CFD simulations completed

 - Residual and force convergence verified

 - Sensitivity formulation studied
___
**Challenges**
---
 - Maintaining mesh quality for large deformations

 - Efficient adjoint sensitivity computation

 - Balancing accuracy and computational cost
___
**Future Plans**
---
 - Apply optimization to 3D wings and winglets

 - Extend to turbulent flow simulations

 - Multi-objective optimization (drag, lift, moment)

 - Real-world aerospace and wind energy applications
___
**Conclusion**

A stable and converged CFD solution using SU2 has been obtained, validating the solver and mesh setup. This forms a strong baseline for implementing adjoint-based aerodynamic shape optimization using RBF mesh deformation.
