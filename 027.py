from euler.prime import PrimenessChecker
pc = PrimenessChecker('primes.txt')

result = [-1000, -1000, 0]

def quadratic(a, b, n):
    return n**2 + a*n + b

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        count = 0
        while pc.is_prime(quadratic(a, b, n)):
            count += 1
            n += 1
        if count > result[2]:
            result = [a, b, count]
    if a % 100 == 0:
        print a # progress report
print result
print result[0] * result[1]