#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Read the Tecplot format file
print("Reading Tecplot-format history.dat...")
with open('history.dat', 'r') as f:
    lines = f.readlines()

# Find where data starts (after "ZONE T=" line)
data_start = 0
for i, line in enumerate(lines):
    if 'ZONE T=' in line:
        data_start = i + 1
        break

print(f"Data starts at line {data_start + 1}")

# Parse the data
data = []
for line in lines[data_start:]:
    line = line.strip()
    if line and not line.startswith('#'):
        # Remove leading/trailing commas if present
        if line.startswith(','):
            line = line[1:]
        if line.endswith(','):
            line = line[:-1]
        
        # Split by commas
        values = line.split(',')
        if len(values) >= 20:  # Expecting 20-21 columns
            try:
                row = [float(v.strip()) for v in values]
                data.append(row)
            except ValueError:
                continue

data = np.array(data)
print(f"Read {len(data)} iterations")
print(f"Data shape: {data.shape}")

# Column indices based on Tecplot header (from your output):
# Column 0: Iteration
# Column 1: Time(s)
# Column 2: Res_Flow[0] (Continuity)
# Column 3: Res_Flow[1] (x-momentum) 
# Column 4: Res_Flow[2] (y-momentum)
# Column 5: Res_Flow[3] (energy)
# Column 6: Res_Flow[4]
# Column 7: Linear_Solver_Iterations
# Column 8: CFL_Number
# Column 9: CLift(Total)
# Column 10: CDrag(Total)
# Columns 11-20: Other coefficients

print("\nColumn mapping:")
columns = [
    "Iteration", "Time(s)", "Res_Flow[0]", "Res_Flow[1]", "Res_Flow[2]",
    "Res_Flow[3]", "Res_Flow[4]", "Linear_Solver_Iterations", "CFL_Number",
    "CLift(Total)", "CDrag(Total)", "CMz(Total)", "CFx(Total)", "CFy(Total)",
    "CLift(Pressure)", "CDrag(Pressure)", "CMz(Pressure)", "CFx(Pressure)", 
    "CFy(Pressure)", "CL/CD", "Time(min)"
]

for i, col in enumerate(columns[:min(21, data.shape[1])]):
    print(f"  Column {i}: {col}")

# Create comprehensive plots
plt.figure(figsize=(16, 12))

# Plot 1: Main residual convergence
plt.subplot(3, 3, 1)
plt.semilogy(data[:, 0], data[:, 2], 'b-', linewidth=2, label='Res_Flow[0]')
if data.shape[1] > 3:
    plt.semilogy(data[:, 0], data[:, 3], 'r-', linewidth=1, alpha=0.7, label='Res_Flow[1]')
if data.shape[1] > 4:
    plt.semilogy(data[:, 0], data[:, 4], 'g-', linewidth=1, alpha=0.7, label='Res_Flow[2]')
plt.xlabel('Iteration')
plt.ylabel('Residual (log scale)')
plt.title('Residual Convergence')
plt.legend(fontsize=8)
plt.grid(True, alpha=0.3)

# Plot 2: Force coefficients evolution
plt.subplot(3, 3, 2)
plt.plot(data[:, 0], data[:, 9], 'r-', linewidth=2, label='Lift (CL)')
plt.plot(data[:, 0], data[:, 10], 'g-', linewidth=2, label='Drag (CD)')
plt.xlabel('Iteration')
plt.ylabel('Coefficient')
plt.title('Force Coefficients Evolution')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: Lift-to-Drag ratio
plt.subplot(3, 3, 3)
if data.shape[1] > 19:
    plt.plot(data[:, 0], data[:, 19], 'purple', linewidth=2)
    plt.ylabel('CL/CD')
else:
    # Calculate L/D if not in data
    ld_ratio = data[:, 9] / data[:, 10]
    plt.plot(data[:, 0], ld_ratio, 'purple', linewidth=2)
    plt.ylabel('CL/CD (calculated)')
plt.xlabel('Iteration')
plt.title('Lift-to-Drag Ratio')
plt.grid(True, alpha=0.3)

# Plot 4: Moment coefficient
plt.subplot(3, 3, 4)
if data.shape[1] > 11:
    plt.plot(data[:, 0], data[:, 11], 'orange', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('CMz')
    plt.title('Pitching Moment Coefficient')
plt.grid(True, alpha=0.3)

# Plot 5: Force coefficients in x and y
plt.subplot(3, 3, 5)
if data.shape[1] > 12:
    plt.plot(data[:, 0], data[:, 12], 'b-', linewidth=2, label='CFx')
if data.shape[1] > 13:
    plt.plot(data[:, 0], data[:, 13], 'm-', linewidth=2, label='CFy')
plt.xlabel('Iteration')
plt.ylabel('Force Coefficient')
plt.title('Force in x and y directions')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 6: CFL Number evolution
plt.subplot(3, 3, 6)
if data.shape[1] > 8:
    plt.plot(data[:, 0], data[:, 8], 'c-', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('CFL Number')
    plt.title('CFL Number Evolution')
plt.grid(True, alpha=0.3)

# Plot 7: Linear solver iterations
plt.subplot(3, 3, 7)
if data.shape[1] > 7:
    plt.plot(data[:, 0], data[:, 7], 'brown', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('Linear Solver Iterations')
    plt.title('Linear Solver Performance')
plt.grid(True, alpha=0.3)

# Plot 8: Computational time
plt.subplot(3, 3, 8)
plt.plot(data[:, 0], data[:, 1], 'gray', linewidth=2)
plt.xlabel('Iteration')
plt.ylabel('Time (s)')
plt.title('Cumulative Computational Time')
plt.grid(True, alpha=0.3)

# Plot 9: Final results summary
plt.subplot(3, 3, 9)
plt.axis('off')

# Calculate final values
final_iter = int(data[-1, 0])
final_cl = data[-1, 9]
final_cd = data[-1, 10]
final_cmz = data[-1, 11] if data.shape[1] > 11 else 0
final_time = data[-1, 1]
initial_res = data[0, 2]
final_res = data[-1, 2]

summary = f"""
SU2 Simulation Results
NACA0012 Airfoil
=====================

Iterations: {final_iter}
Time: {final_time:.2f} s

FINAL COEFFICIENTS:
• Lift (CL):     {final_cl:.6f}
• Drag (CD):     {final_cd:.6f}
• L/D Ratio:     {final_cl/final_cd:.2f}
• Moment (CMz):  {final_cmz:.6f}

CONVERGENCE:
• Initial Res:   {initial_res:.2e}
• Final Res:     {final_res:.2e}
• Reduction:     {initial_res/final_res:.1e}x

CFL History:
• Min CFL:       {data[:,8].min():.2f}
• Max CFL:       {data[:,8].max():.2f}
• Final CFL:     {data[-1,8]:.2f}
"""

plt.text(0.1, 0.5, summary, fontsize=9, 
         verticalalignment='center',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

plt.suptitle('SU2 Tecplot History Analysis: NACA0012 Inviscid Flow', 
             fontsize=16, fontweight='bold')
plt.tight_layout()

# Save figure
plt.savefig('tecplot_history_analysis.png', dpi=150, bbox_inches='tight')
print("\n✅ Plot saved as 'tecplot_history_analysis.png'")

# Also save a CSV for further analysis
np.savetxt('history_clean.csv', data, delimiter=',', 
           header=','.join(columns[:data.shape[1]]))
print("✅ Clean data saved as 'history_clean.csv'")

# Show final values table
print("\n" + "="*80)
print("FINAL SIMULATION RESULTS")
print("="*80)
print(f"{'Iteration':>10} {'CLift':>12} {'CDrag':>12} {'CL/CD':>12} {'Residual':>15}")
print("-"*80)
for i in [0, 50, 100, 150, 200, final_iter]:
    if i < len(data):
        idx = i if i < len(data) else -1
        cl = data[idx, 9]
        cd = data[idx, 10]
        res = data[idx, 2]
        print(f"{int(data[idx,0]):10d} {cl:12.6f} {cd:12.6f} {cl/cd:12.2f} {res:15.2e}")
print("="*80)

# Show the plot
plt.show()
