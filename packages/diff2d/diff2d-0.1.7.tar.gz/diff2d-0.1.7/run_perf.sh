#! bin/bash
cd "$(dirname "$0")"
perf stat -e cycles,instructions,cpu-clock,page-faults,cache-references,cache-misses,context-switches,branch-misses python diff2d/diffusion.py input.png 0.7 0.1 100