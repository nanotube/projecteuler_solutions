import math
n = 600851475143
largestprime = 0
for i in range(2, int(math.sqrt(600851475143)) + 1):
    if n % i == 0:
        prime = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            prime = 1
        if prime == 1 and i > largestprime:
            largestprime = i
print largestprime