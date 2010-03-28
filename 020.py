from operator import mul
p = reduce(mul, range(1,101))
print sum([int(c) for c in str(p)])