import string
import sys
import re

data = open('059 - cipher1.txt').read().split(',')
data = [int(i) for i in data]
print len(data)
#sys.exit()
for a in string.lowercase:
    for b in string.lowercase:
        for c in string.lowercase:
            password = [a,b,c]*400 + [a]
            decryptlist = [(ord(password[i]) ^ data[i]) for i in range(len(data))]
            decryptstring = "".join([chr(num) for num in decryptlist])
            if re.search(r'(?i) the ', decryptstring):
                print decryptstring
                print sum(decryptlist)
                print a, b, c # this is g, o, d
                sys.exit()
