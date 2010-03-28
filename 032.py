panprods = []
panset = set('123456789')
for i in range(2, 1000):
    for j in range(i+1, 10000/i):
        if set(str(i)).intersection(set(str(j))) == set():
            if len(list(str(i) + str(j) + str(i*j))) == 9 and set(str(i) + str(j) + str(i*j)) == panset:
                panprods.append(i*j)

panprodset = set(panprods)
print len(panprodset)
print sum(panprodset) # 45228