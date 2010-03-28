import math

primes = open('primes.txt').readlines()
primes = [int(line.strip()) for line in primes]
print len(primes) # just to see. this should contain all primes <= 2mill
circularcount = 0

def is_prime(n):
    prime = 1
    for p in primes:
        if n % p == 0:
            prime = 0
            break
        if p > math.sqrt(n):
            break
    return prime

for i in range(len(primes)):
    p = primes[i]
    if p < 10:
        circularcount += 1
        continue
    if p > 1000000:
        break
    allprime = 0
    pstr = str(p)
    for s in range(len(pstr)):
        pstr = pstr[1:] + pstr[0]
        anint = int(pstr)
        if not is_prime(anint):
            break
    else:
        allprime = 1
    
    if i %10000 == 0:
        print i
    
    if allprime == 1:
        circularcount += 1

print circularcount