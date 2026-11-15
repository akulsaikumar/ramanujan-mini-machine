import os
os.system("cls")
import math

def evaluate(c, d, p, q, depth):
    value = c * depth + d
    for level in range(depth, 0, -1):
        bottom = c * (level - 1) + d
        top = p * level + q
        if value == 0:
            return None
        value = bottom + top / value
    return value

targets = {
    "e": math.e,
    "pi": math.pi, 
    "root2": math.sqrt(2),
    "1 + root2": 1 + math.sqrt(2),
    "e/(e-2)": math.e/(math.e-2),
    "1 + root3": 1 + math.sqrt(3),
   "1 + root5": 1 + math.sqrt(5),
   "1 + root6": 1 + math.sqrt(6),
}
combinations_checked = 0
candidates = 0
broken = 0
confirmed = 0
rejected = 0 
for c in range (-5, 6):
    for d in range(-5, 6):
        for p in range(-5, 6):
            for q in range(-5, 6):
                value = evaluate(c, d, p, q, 200)
                combinations_checked = combinations_checked + 1
                if value is None:
                    broken = broken + 1
                    continue
                for name, target in targets.items():
                    if abs(value - target) < 1e-2:
                        candidates = candidates + 1
                        checkvalue = evaluate(c, d, p, q, 400)
                        if checkvalue is not None and abs(checkvalue - target) < 1e-10:
                            confirmed = confirmed + 1
                            print("Found", name, value, "[", c, d, p, q, "]")
                        else:
                            rejected = rejected + 1
print("Searched", combinations_checked, "continued fractions.")
print(candidates, "candidates found.")
print("Confirmed", confirmed, "values.")
print("Found", broken, "broken continued fractions.")
print("Rejected", rejected, "continued fractions.")
