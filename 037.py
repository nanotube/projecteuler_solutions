from euler.prime import PrimenessChecker
pc = PrimenessChecker('primes.txt')

truncatables = []

for i in range(len(pc.primes)):
    p = pc.primes[i]
    if p < 10:
        continue
    allprime = 1
    pstr = str(p)
    for i in [-1,1]:
        for s in range(1, len(pstr)):
            if i == -1:
                pstrtrunk = pstr[:s*i]
            if i == 1:
                pstrtrunk = pstr[s*i:]
            anint = int(pstrtrunk)
            if not pc.is_prime(anint):
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