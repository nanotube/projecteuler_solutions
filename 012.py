import math
i = 0
num = 0
while True:
    i += 1
    num += i
    factors = 0
    sq = int(math.sqrt(num))
    for j in range(2, sq):
        if num%j == 0:
            factors += 1
    factors *= 2
    if sq == math.sqrt(num):
        factors += 1
    factors += 2
    if factors > 500:
        print num # 76576500
        print factors #576
        break
    if i % 1000 == 0:
        print 'iter',i