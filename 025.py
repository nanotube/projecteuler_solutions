(i,j) = (1,1)
limit = 10**999
counter = 2
while int(j / limit) < 1:
    (i,j) = (j, i+j)
    counter += 1
print counter