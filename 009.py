import math
import sys

for a in range(1,500):
    for b in range(1, 500):
        csq = a**2 + b**2
        c = math.sqrt(csq)
        if c == int(c):
            if a+b+c == 1000:
                print 'a,b,c:', a, b, c
                print 'a*b*c:', a*b*c
                sys.exit()