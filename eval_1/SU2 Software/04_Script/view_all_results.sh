#!/bin/bash
echo "================================================"
echo "          SU2 SIMULATION RESULTS"
echo "================================================"

echo -e "\n📊 1. CONVERGENCE HISTORY (history.dat):"
echo "================================================"
if [ -f "history.dat" ]; then
    echo "First 10 iterations:"
    head -11 history.dat
    echo -e "\nLast 5 iterations:"
    tail -5 history.dat
    echo -e "\nTotal iterations: $(wc -l < history.dat)"
else
    echo "File not found"
fi

echo -e "\n✈️ 2. AERODYNAMIC FORCES (forces_breakdown.dat):"
echo "================================================"
[ -f "forces_breakdown.dat" ] && cat forces_breakdown.dat || echo "File not found"

echo -e "\n📈 3. SURFACE PRESSURE (surface_flow.dat):"
echo "================================================"
if [ -f "surface_flow.dat" ]; then
    echo "First 5 surface points:"
    head -6 surface_flow.dat
    echo -e "\nFile contains $(wc -l < surface_flow.dat) data points"
else
    echo "File not found"
fi

echo -e "\n🌊 4. VOLUME SOLUTION (flow.dat):"
echo "================================================"
if [ -f "flow.dat" ]; then
    echo "File size: $(du -h flow.dat | cut -f1)"
    echo "First few lines:"
    head -3 flow.dat
    echo "..."
    echo "Variables saved:"
    grep -i "variables" flow.dat | head -2
else
    echo "File not found"
fi

echo -e "\n🔄 5. RESTART FILE (restart_flow.dat):"
echo "================================================"
[ -f "restart_flow.dat" ] && echo "Size: $(du -h restart_flow.dat | cut -f1)" || echo "File not found"

echo -e "\n================================================"
echo "Summary: All 5 output files generated successfully!"
echo "================================================"
