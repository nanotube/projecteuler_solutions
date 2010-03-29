import math

def make_triangle(n):
    return n * (n+1) / 2

def is_pentagonal(n):
    s1 = (1. + math.sqrt(1. + 4.*3.*2.*n)) / 6.
    s2 = (1. - math.sqrt(1. + 4.*3.*2.*n)) / 6.
    
    if s1 == int(s1) and s1 > 0 or s2 == int(s2) and s2 > 0:
        return True
    else:
        return False

def is_hexagonal(n):
    s1 = (1. + math.sqrt(1. + 4.*2.*n)) / 4.
    s2 = (1. - math.sqrt(1. + 4.*2.*n)) / 4.
    
    if s1 == int(s1) and s1 > 0 or s2 == int(s2) and s2 > 0:
        return True
    else:
        return False


for i in range(286, 1000000):
    tr = make_triangle(i)
    if is_pentagonal(tr) and is_hexagonal(tr):
        print tr
        break
