import math
import sys

solutions = dict(zip(range(1,1001), [0]*1000))

for a in range(1,500):
    for b in range(1, 500):
        csq = a**2 + b**2
        c = math.sqrt(csq)
        if c == int(c):
            if a+b+c <= 1000:
                solutions[a+b+c] += 1

vals = solutions.keys()
vals.sort(key=solutions.__getitem__)
print vals[len(vals)-1]