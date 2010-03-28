import math
primes = []
i = 2
for i in range(2, 2000001):
    prime = 1
    for j in primes:
        if j > math.sqrt(i)+1:
            break
        if i % j == 0:
            prime = 0
            break
    if prime:
        primes.append(i)
    if i % 100000 == 0:
        print i #progress report
print sum(primes)
primestr = [str(i) for i in primes]
open('primes.txt', 'w').write('\n'.join(primestr))