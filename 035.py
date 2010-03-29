from euler.prime import PrimenessChecker
pc = PrimenessChecker('primes.txt', maxprime=1000000)

circularcount = 0

for i in range(len(pc.primes)):
    p = pc.primes[i]
    if p < 10:
        circularcount += 1
        continue
    allprime = 0
    pstr = str(p)
    for s in range(len(pstr)):
        pstr = pstr[1:] + pstr[0]
        anint = int(pstr)
        if not pc.is_prime(anint):
            break
    else:
        allprime = 1
    
    if i %10000 == 0:
        print i
    
    if allprime == 1:
        circularcount += 1

print circularcount