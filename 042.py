data = open('042 - words.txt').read().replace('"','').split(',')

tnums = [i * (i+1) / 2 for i in range(100)] #that should be enough

numtwords = 0

for word in data:
    values = [ord(c) - 64 for c in word]
    if sum(values) in tnums:
        numtwords += 1

print numtwords