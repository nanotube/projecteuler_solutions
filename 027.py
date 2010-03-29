import sys
import math

primes = open('primes.txt').readlines()
primes = [int(p) for p in primes]

def is_prime(n):
    prime = 1
    if n < 2:
        return 0
    if n in [2, 3]:
        return 1
    for p in primes:
        if n % p == 0:
            prime = 0
            break
        if p > math.sqrt(n):
            break
    return prime

result = [-1000, -1000, 0]

def quadratic(a, b, n):
    return n**2 + a*n + b

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        count = 0
        while is_prime(quadratic(a, b, n)):
            count += 1
            n += 1
        if count > result[2]:
            result = [a, b, count]
    if a % 100 == 0:
        print a # progress report
print result
print result[0] * result[1]