from operator import mul
import sys
numbers = []

def factorial(n):
    if n == 0:
        return 1
    return reduce(mul, range(1, n+1))

factorials = [factorial(n) for n in range(1, 10)]
factorials = [1] + factorials
factdict = dict(zip([str(i) for i in range(10)], factorials))

for i in xrange(3, 100000):
    sumfact = sum([factdict[d] for d in str(i)])
    #print sumfact
    if sumfact == i:
        numbers.append(i)
    if i % 1000000 == 0:
        print i
        
print sum(numbers)
print max(numbers) # this is 40585