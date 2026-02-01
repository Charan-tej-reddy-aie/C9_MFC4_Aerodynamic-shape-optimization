#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

print("Reading history.dat...")
# Skip the header line (starts with TITLE)
data = np.loadtxt('history.dat', skiprows=1)
print(f"Read {len(data)} iterations")

# Create figure
plt.figure(figsize=(12, 8))

# Plot 1: Residual convergence
plt.subplot(2, 2, 1)
plt.semilogy(data[:, 0], data[:, 1], 'b-', linewidth=2)
plt.xlabel('Iteration')
plt.ylabel('Residual [Rho]')
plt.title('Residual Convergence')
plt.grid(True, alpha=0.3)

# Plot 2: Force coefficients
plt.subplot(2, 2, 2)
plt.plot(data[:, 0], data[:, 3], 'r-', label='Lift (CL)', linewidth=2)
plt.plot(data[:, 0], data[:, 4], 'g-', label='Drag (CD)', linewidth=2)
plt.xlabel('Iteration')
plt.ylabel('Coefficient')
plt.title('Force Coefficients')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: Lift-to-Drag ratio
plt.subplot(2, 2, 3)
if len(data[0]) > 5:  # Check if we have enough columns
    plt.plot(data[:, 0], data[:, 5], 'm-', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('L/D Ratio')
    plt.title('Lift-to-Drag Ratio')
else:
    # Calculate L/D if not in data
    l_over_d = data[:, 3] / data[:, 4]
    plt.plot(data[:, 0], l_over_d, 'm-', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('L/D Ratio')
    plt.title('Lift-to-Drag Ratio (Calculated)')
plt.grid(True, alpha=0.3)

# Plot 4: Final values summary
plt.subplot(2, 2, 4)
plt.axis('off')  # Turn off axis for text display

# Get final values
final_iter = data[-1, 0]
final_residual = data[-1, 1]
final_cl = data[-1, 3]
final_cd = data[-1, 4]
final_ld = final_cl / final_cd if final_cd != 0 else 0

summary_text = f"""
SU2 Simulation Results
NACA0012 Airfoil (Inviscid)

Final Iteration: {int(final_iter)}
Final Residual: {final_residual:.2e}

Aerodynamic Coefficients:
• Lift (CL): {final_cl:.6f}
• Drag (CD): {final_cd:.6f}
• L/D Ratio: {final_ld:.6f}
• CL/CD: {final_ld:.2f}

Convergence:
Initial Residual: {data[0, 1]:.2e}
Final Residual:  {data[-1, 1]:.2e}
Reduction:       {data[0, 1]/data[-1, 1]:.2e}x
"""

plt.text(0.1, 0.5, summary_text, fontsize=10, 
         verticalalignment='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('SU2 CFD Simulation: NACA0012 Airfoil', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('convergence_results.png', dpi=150, bbox_inches='tight')
print("✅ Plot saved as 'convergence_results.png'")
plt.show()
