l = [i*j for i in range(100,1000) for j in range(100,1000)]
l.sort(reverse=True)
for i in l:
    if str(i) == str(i)[::-1]:
        break
print i