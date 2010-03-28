maxseq = 0
maxnum = 0

def treat(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

for i in range(13, 1000000):
    seq = 1
    n = i
    while n != 1:
        n = treat(n)
        seq += 1
    if seq > maxseq:
        maxseq = seq
        maxnum = i
    if i%100000 == 0:
        print i

print maxnum
print maxseq