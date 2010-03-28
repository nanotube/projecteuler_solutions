from operator import mul
import sys
numbers = []

powers = [n**5 for n in range(10)]
powdict = dict(zip([str(i) for i in range(10)], powers))

for i in xrange(2, 999999):
    sumpows = sum([powdict[d] for d in str(i)])
    if sumpows == i:
        numbers.append(i)
    if i % 100000 == 0:
        print i
        
print sum(numbers)
print max(numbers) # this is 194979