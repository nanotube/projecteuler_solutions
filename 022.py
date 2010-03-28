data = open('022 - names.txt').read()
data = data.replace('"','').split(',')
data.sort()
scores = 0
for (i,name) in enumerate(data):
    namescore = sum([ord(c) - 64 for c in name])
    namescore = (i+1) * namescore
    scores += namescore
print scores