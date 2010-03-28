#!/usr/bin/python2.6

palindromes = []

def is_palindromic(n):
    n
    nreverse = list(n)
    nreverse.reverse()
    nreverse = ''.join(nreverse)
    if n == nreverse:
        return True
    return False
    
for i in range(1,1000001):
    if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]):
        palindromes.append(i)
        
print len(palindromes)
print sum(palindromes)

#print bin(10)

