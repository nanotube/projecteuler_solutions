from operator import mul
number = ''
i = 0
while len(number) < 1000000:
    i+=1
    number += str(i)

digits = [number[0], number[9], number[99], number[999], number[9999], number[99999], number[999999]]

print ','.join(digits)
print reduce(mul, [int(n) for n in digits])