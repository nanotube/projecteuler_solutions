lychrelcount = 0
for i in range(10000):
    n = i
    for j in range(50):
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            break
    else:
        lychrelcount += 1
print 'lychrel count:', lychrelcount