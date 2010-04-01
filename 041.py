from euler.prime import PrimenessChecker
from euler import utils
pc = PrimenessChecker('primes.txt')

largestpandigitalprime = 0

for i in range(len(pc.primes)): #let's hope we have enough primes...
    p = pc.primes[i]
    if utils.is_pandigital(p):
        largestpandigitalprime = p

print largestpandigitalprime # 7652413 (yay, we do have enough)