#!/bin/bash
echo "=============================================="
echo "          SU2 OUTPUT FILES VIEWER"
echo "=============================================="

# List all files
echo "Files in directory:"
ls -la

echo -e "\n=============================================="
echo "1. FORCES BREAKDOWN (if exists):"
echo "=============================================="
[ -f "forces_breakdown.dat" ] && cat forces_breakdown.dat || echo "Not found"

echo -e "\n=============================================="
echo "2. CONVERGENCE HISTORY (if exists):"
echo "=============================================="
if [ -f "history.csv" ]; then
    echo "First 10 iterations:"
    head -11 history.csv | column -t -s,
elif [ -f "history.dat" ]; then
    head -20 history.dat
else
    echo "No history file found"
    # Check for other convergence files
    find . -name "*conv*" -type f 2>/dev/null | while read f; do
        echo "Found: $f"
        head -5 "$f"
    done
fi

echo -e "\n=============================================="
echo "3. SURFACE DATA (if exists):"
echo "=============================================="
if [ -f "surface_flow.csv" ]; then
    echo "Surface flow data (first 5 points):"
    head -6 surface_flow.csv | column -t -s,
else
    ls *surface* *wall* 2>/dev/null || echo "No surface files found"
fi

echo -e "\n=============================================="
echo "4. VISUALIZATION FILES:"
echo "=============================================="
echo "VTK/PLT files for ParaView/Tecplot:"
ls *.vtk *.plt 2>/dev/null || echo "No visualization files found"

echo -e "\n=============================================="
echo "5. RESTART FILES:"
echo "=============================================="
ls *restart* 2>/dev/null || echo "No restart files found"

echo -e "\n=============================================="
echo "File sizes:"
echo "=============================================="
find . -maxdepth 1 -type f ! -name "*.cfg" -exec du -h {} \; 2>/dev/null
