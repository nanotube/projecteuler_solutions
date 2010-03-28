import math
primes = []
i = 2
while len(primes) < 10001:
    prime = 1
    for j in primes:
        if i % j == 0:
            prime = 0
            break
    if prime:
        primes.append(i)
    i += 1
print primes[-1]