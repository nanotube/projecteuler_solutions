nums = [2]
for i in range(1,34):
    nums = nums + [1, 2*i, 1]
print len(nums)
print nums

fracnum = 0
fracdenom = 1

for i in range(len(nums)-1, 0-1, -1):
    fracdenom = fracdenom
    fracnum = nums[i]*fracdenom + fracnum
    (fracnum, fracdenom) = (fracdenom, fracnum)

print fracnum
print fracdenom

print 'e approximation', float(fracdenom)/float(fracnum)

print sum([int(c) for c in str(fracdenom)])