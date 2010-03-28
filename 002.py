fibsum = 2
(i,j) = (1,2)
while j < 4000000:
    (i,j) = (j, i+j)
    if j % 2 == 0:
        fibsum += j
print fibsum