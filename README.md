# Ramanujan Mini Machine
A small Python program that searches for continued fractions
matching mathematical constants like π, inspired by the
Ramanujan Machine project.

## How it works
1. Generates continued fractions from a range of integer coefficients
2. Evaluates each one numerically
3. Flags any that match a target constant to 10 decimal places

## How to run
python mini_machine.py

## Results so far
- Searched all 14,641 combinations of four coefficients (each from −5 to 5),
  evaluating each fraction 200 levels deep
- Without being given the answers, rediscovered the known continued
  fractions for **e** and **1 + √2**
- Rediscovered the Ramanujan Machine's published formula for **e/(e−2)**
  (included as a target)
- Also found continued fractions for **1 + √3**, **1 + √5** and **1 + √6**
  once they were added as targets
- A stability check re-evaluates every match at double depth: [X] candidates
  found, [Y] confirmed, [Z] rejected as unstable

## Limitations
- Only checks numerically, so matches are conjectures, not proofs
- Only searches straight-line rules, which is why it can't find π
  (its known continued fractions need squared terms)
- Standard Python floats hold only about 15 significant digits
- Brute force, so it slows down quickly as the search space grows

## Background
Built alongside my EPQ on Ramanujan's formulas for π.

## Next steps
- Two-stage verification (fast filter, then high-precision check)
- Rewrite in NumPy for speed
