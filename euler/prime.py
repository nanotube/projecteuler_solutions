import math

class PrimenessChecker:
    def __init__(self, primesfile, lines=0, maxprime=0):
        '''initialize by reading the primes file. 
        
        if lines and/or maxprime arguments are given, 
        read only up to the lines/maxprime limit, whichever
        is lower.
        '''
        if lines == 0 and maxprime == 0:
            primes = open(primesfile).readlines()
            self.primes = [int(p) for p in primes]
        else:
            f = open(primesfile)
            primes = []
            for (i, line) in enumerate(f):
                p = int(line)
                primes.append(p)
                if lines != 0 and i > lines:
                    break
                if maxprime != 0 and p > maxprime:
                    break
            self.primes = primes

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