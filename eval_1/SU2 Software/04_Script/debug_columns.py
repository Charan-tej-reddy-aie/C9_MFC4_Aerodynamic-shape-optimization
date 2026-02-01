#!/usr/bin/env python3
import numpy as np

# Read and parse the data manually
with open('history.dat', 'r') as f:
    lines = f.readlines()

# Find data start
for i, line in enumerate(lines):
    if 'ZONE T=' in line:
        start = i + 1
        break

print("=== DEBUG: First 3 data rows ===")
for i in range(start, start + 3):
    line = lines[i].strip()
    values = [float(x.strip()) for x in line.split(',')]
    print(f"Row {i-start}: {len(values)} columns")
    for col_idx, val in enumerate(values[:15]):  # First 15 columns
        print(f"  Col {col_idx:2}: {val:12.6e}")
    print()

print("=== DEBUG: Last 3 data rows ===")
for i in range(len(lines)-3, len(lines)):
    line = lines[i].strip()
    if line and not line.startswith('#'):
        values = [float(x.strip()) for x in line.split(',')]
        print(f"Row ~{i-start}: {len(values)} columns")
        for col_idx, val in enumerate(values[:15]):
            print(f"  Col {col_idx:2}: {val:12.6e}")
        print()

# Now compare with forces_breakdown.dat
print("=== Comparing with forces_breakdown.dat ===")
with open('forces_breakdown.dat', 'r') as f:
    for line in f:
        if 'Total CL:' in line:
            print("From forces_breakdown.dat:")
            print(line.strip())
        if 'Total CD:' in line:
            print(line.strip())
