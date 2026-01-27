#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

print("Reading and parsing history.dat...")

# Read the file
with open('history.dat', 'r') as f:
    content = f.read()

# Find the data section
lines = content.split('\n')
data_lines = []
in_data = False

for line in lines:
    line = line.strip()
    if 'ZONE T=' in line:
        in_data = True
        continue
    if in_data and line and line[0].isdigit() or (line.startswith(',') and line[1:2].isdigit()):
        # Clean the line
        if line.startswith(','):
            line = line[1:]
        # Split by comma
        parts = line.split(',')
        # Convert to floats
        try:
            row = [float(p.strip()) for p in parts]
            if len(row) >= 10:  # Need minimum columns
                data_lines.append(row)
        except:
            continue

data = np.array(data_lines)
print(f"Read {len(data)} iterations")
print(f"Data shape: {data.shape}")

# Based on your actual output, let's identify correct columns
# From your sample: iteration 249 has values that might be CL/CD
# Let's find which columns match your known results

print("\n=== Identifying correct columns ===")
print("From forces_breakdown.dat we know:")
print("  Final CL = 0.326933")
print("  Final CD = 0.021350")
print("  Final CL/CD = 15.313230")
print()

# Search for matching values in last row
last_row = data[-1]
for i, val in enumerate(last_row):
    if abs(val - 0.326933) < 0.01:
        print(f"Column {i} might be CL: {val:.6f}")
    if abs(val - 0.021350) < 0.01:
        print(f"Column {i} might be CD: {val:.6f}")
    if abs(val - 15.313230) < 0.1:
        print(f"Column {i} might be CL/CD: {val:.6f}")

# Let me check the actual pattern from iteration 249 in your data
print("\n=== Last iteration (249) values ===")
for i, val in enumerate(last_row[:20]):  # First 20 columns
    print(f"Column {i:2}: {val:12.6f}")

# Based on common SU2 Tecplot output, the columns are usually:
# 0: Iteration
# 1: Time
# 2-6: Residuals
# 7: Linear solver iterations
# 8: CFL number
# 9: CL
# 10: CD
# 11: CMz
# 12: CFx
# 13: CFy
# ... etc

print("\n=== Creating plot with common column mapping ===")

# Create plot
plt.figure(figsize=(14, 10))

# Plot 1: Residuals (assuming columns 2-4 are residuals)
plt.subplot(2, 3, 1)
if data.shape[1] > 4:
    plt.semilogy(data[:, 0], np.abs(data[:, 2]), 'b-', label='Res[0]', linewidth=2)
    if data.shape[1] > 3:
        plt.semilogy(data[:, 0], np.abs(data[:, 3]), 'r-', alpha=0.7, label='Res[1]', linewidth=1)
    if data.shape[1] > 4:
        plt.semilogy(data[:, 0], np.abs(data[:, 4]), 'g-', alpha=0.7, label='Res[2]', linewidth=1)
plt.xlabel('Iteration')
plt.ylabel('Residual (log scale)')
plt.title('Residual Convergence')
plt.legend(fontsize=8)
plt.grid(True, alpha=0.3)

# Plot 2: Try to find CL and CD - let's plot several candidate columns
plt.subplot(2, 3, 2)
# Common CL columns: 9, 14, 19
candidate_cols = [9, 14, 19]
colors = ['r', 'b', 'g']
labels = ['Col9', 'Col14', 'Col19']
for col, color, label in zip(candidate_cols, colors, labels):
    if data.shape[1] > col:
        plt.plot(data[:, 0], np.abs(data[:, col]), color+'-', label=label, linewidth=2, alpha=0.7)
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Candidate CL/CD Columns')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: CFL number (usually column 8)
plt.subplot(2, 3, 3)
if data.shape[1] > 8:
    plt.plot(data[:, 0], data[:, 8], 'c-', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('CFL Number')
    plt.title('CFL Number Evolution')
    plt.grid(True, alpha=0.3)

# Plot 4: Time progression
plt.subplot(2, 3, 4)
if data.shape[1] > 1:
    plt.plot(data[:, 0], data[:, 1], 'gray', linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('Time (s)')
    plt.title('Cumulative Time')
    plt.grid(True, alpha=0.3)

# Plot 5: Text analysis - show actual values from forces_breakdown.dat
plt.subplot(2, 3, 5)
plt.axis('off')

# Read forces_breakdown.dat for correct values
correct_cl = 0.326933
correct_cd = 0.021350
correct_cmz = 0.033698
correct_cld = 15.313230

summary = f"""
CORRECT RESULTS from forces_breakdown.dat:
==========================================
Lift (CL):     {correct_cl:.6f}
Drag (CD):     {correct_cd:.6f}
CL/CD Ratio:   {correct_cld:.6f}
Moment (CMz):  {correct_cmz:.6f}

Last iteration values from history.dat:
=======================================
Column 9:  {last_row[9]:.6f}
Column 10: {last_row[10]:.6f}
Column 11: {last_row[11]:.6f}
Column 14: {last_row[14]:.6f}
Column 19: {last_row[19]:.6f}

Note: Some values might be negative
in history.dat but magnitudes matter.
"""

plt.text(0.05, 0.5, summary, fontsize=9, 
         verticalalignment='center', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot 6: Magnitude plot (absolute values)
plt.subplot(2, 3, 6)
plt.axis('off')

# Show which columns might contain our data by comparing magnitudes
matches = []
for i in range(min(25, data.shape[1])):
    val = abs(last_row[i])
    if abs(val - correct_cl) < 0.05:
        matches.append(f"Col {i}: {last_row[i]:.6f} (matches CL)")
    if abs(val - correct_cd) < 0.05:
        matches.append(f"Col {i}: {last_row[i]:.6f} (matches CD)")
    if abs(val - correct_cld) < 0.5:
        matches.append(f"Col {i}: {last_row[i]:.6f} (matches CL/CD)")

match_text = "Possible column matches:\n" + "\n".join(matches) if matches else "No close matches found"

plt.text(0.05, 0.5, match_text, fontsize=9,
         verticalalignment='center', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

plt.suptitle('SU2 History Data Analysis - Column Identification', fontsize=14, fontweight='bold')
plt.tight_layout()

# Save and show
plt.savefig('column_analysis.png', dpi=150, bbox_inches='tight')
print("\n✅ Analysis plot saved as 'column_analysis.png'")
print("   This will help identify which columns contain CL, CD, etc.")

# Also create a simple correct plot using known values
print("\n=== Creating simple correct plot ===")
plt.figure(figsize=(10, 4))

# Since we know the correct final values, let's plot something useful
# Plot residual convergence (this is definitely correct)
plt.subplot(1, 2, 1)
plt.semilogy(data[:, 0], np.abs(data[:, 2]), 'b-', linewidth=2)
plt.xlabel('Iteration')
plt.ylabel('|Residual| (log scale)')
plt.title('Residual Convergence')
plt.grid(True, alpha=0.3)

# Plot a candidate force coefficient (use column with reasonable magnitude)
plt.subplot(1, 2, 2)
# Try column 9 or 14 based on typical SU2 output
if data.shape[1] > 14:
    plt.plot(data[:, 0], np.abs(data[:, 9]), 'r-', label='|Col 9|', linewidth=2)
    plt.plot(data[:, 0], np.abs(data[:, 14]), 'g-', label='|Col 14|', linewidth=2, alpha=0.7)
    plt.xlabel('Iteration')
    plt.ylabel('|Coefficient|')
    plt.title('Candidate Force Coefficients (abs values)')
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('simple_analysis.png', dpi=150, bbox_inches='tight')
print("✅ Simple plot saved as 'simple_analysis.png'")

plt.show()
