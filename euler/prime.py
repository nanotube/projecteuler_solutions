import math

class PrimenessChecker:
    def __init__(self, primesfile):
        primes = open(primesfile).readlines()
        self.primes = [int(line) for line in primes]

    def is_prime(self, n):
        is_prime = 1
        if n < 2:
            return 0
        if n in [2, 3]:
            return 1
        for p in self.primes:
            if n % p == 0:
                is_prime = 0
                break
            if p > math.sqrt(n):
                break
        return is_prime