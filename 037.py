import math
import sys

primes = open('primes.txt').readlines()
primes = [int(line.strip()) for line in primes]
print len(primes) # just to see. this should contain all primes <= 2mill
truncatables = []

def is_prime(n):
    prime = 1
    if n == 1:
        #print 'number, primeness:', n, 0
        return 0
    if n in [2, 3]:
        #print 'number, primeness:', n, 1
        return 1
    for p in primes:
        if n % p == 0:
            prime = 0
            break
        if p > math.sqrt(n):
            break
    #print 'number, primeness:', n, prime
    return prime

for i in range(len(primes)):
    p = primes[i]
    if p < 10:
        continue
    allprime = 1
    pstr = str(p)
    #print 'main number', pstr
    for i in [-1,1]:
        #print 'i', i
        for s in range(1, len(pstr)):
            if i == -1:
                pstrtrunk = pstr[:s*i]
            if i == 1:
                pstrtrunk = pstr[s*i:]
            anint = int(pstrtrunk)
            if not is_prime(anint):
                allprime = 0
                break
        
        if allprime == 0:
            break
    
    if i %10000 == 0:
        print i
    
    if allprime == 1:
        truncatables.append(p)

print len(truncatables)
print sum(truncatables)