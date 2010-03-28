import math
amicables = []

def find_proper_factors(i):
    factors = [1]
    sq = int(math.sqrt(i))
    for j in range(2, sq):
        if i%j == 0:
            factors.append(j)
            factors.append(i/j)
    if sq == math.sqrt(i):
        factors.append(sq)
    return factors

for i in range(4,10001):
    if i in amicables:
        continue
    factors_i = find_proper_factors(i)
    i2 = sum(factors_i)
    if i2 == i:
        continue
    factors_i2 = find_proper_factors(i2)
    if sum(factors_i2) == i:
        amicables.append(i)
        amicables.append(i2)
    
    if i % 1000 == 0:
        print 'iter',i
        
print sum(amicables)
print amicables