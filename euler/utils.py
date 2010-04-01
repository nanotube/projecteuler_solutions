def is_pandigital(n):
    panset = set([str(d) for d in range(1,len(str(n))+1)])
    if len(set(str(n))) == len(str(n)) and set(str(n)) == panset:
        return True
    else:
        return False
