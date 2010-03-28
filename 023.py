import sys
import math
abundants = []
abundantsums = []

def find_proper_factors(i):
    factors = [1]
    sq = int(math.sqrt(i))
    if sq != math.sqrt(i):
        rangemax = sq+1
    else:
        rangemax = sq
    for j in range(2, rangemax):
        if i % j == 0:
            factors.append(j)
            factors.append(i/j)
    if sq == rangemax:
        factors.append(sq)
    return factors

for i in xrange(4,28123+1):
    factors = find_proper_factors(i)
    if sum(factors) > i:
        abundants.append(i)
    
    if i % 5000 == 0:
        print 'abundant iter',i

print 'num abundants', len(abundants)
print 'some first abundants', abundants[:10]

for i in range(len(abundants)):
    for j in range(i, len(abundants) - i):
        abundantsums.append(abundants[i]+abundants[j])
    
    if i % 1000 == 0:
        print 'sum iter', i

print 'num sums', len(abundantsums)
uniqabundantsums = list(set(abundantsums))

trimmedsums = filter(lambda i: i <= 28123, uniqabundantsums)
print 'trimmed sums', len(trimmedsums) # 26667

allnums = range(1, 28124)

for i in trimmedsums:
    try:
        allnums.remove(i)
    except ValueError:
        pass

print len(abundants) # 6965
print len(allnums) # 1456
print sum(allnums) # 4179871