import math
primes = open('primes.txt').readlines()
primes = [int(p.strip()) for p in primes]

f = open('primes.txt', 'a')

i = primes[len(primes)-1] # latest available prime
print 'starting prime', i

newprimes = []

try:
    while True:
        i+=1
        prime = 1
        for j in primes:
            if j > math.sqrt(i)+1:
                break
            if i % j == 0:
                prime = 0
                break
        if prime:
            primes.append(i)
            newprimes.append(i)
        if i % 100000 == 0:
            f.write('\n'.join([str(j) for j in newprimes]) + '\n')
            newprimes = []
            print i #progress report
except KeyboardInterrupt:
    if len(newprimes):
        f.write('\n'.join([str(j) for j in newprimes]) + '\n')