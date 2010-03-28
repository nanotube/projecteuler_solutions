import math
(i,j) = (1,1)
count = 2
pandigits = set(range(1,10))
while True:
    (i,j) =  (j, i+j)
    count += 1
    if j < 1000000000:
        continue
    lastdigits = set([int(c) for c in str(j%1000000000)])
    if lastdigits == pandigits:
        #firstdigits = set([int(c) for c in str(j)[:9]])
        power = int(math.log10(j))
        firstdigits = set([int(c) for c in str(int(j / 10**(power - 8)))])
        if firstdigits == pandigits:
            print j
            print count # 329468
            break
    if count % 10000 == 0:
        print count
    