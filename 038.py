largestpandigital = 0
panset = set('123456789')
for i in range(1, 9999):
    products = []
    for j in range(1, 10):
        totalproducts = ''.join(products)
        if set(totalproducts) == panset and len(totalproducts) == 9:
            if int(totalproducts) > largestpandigital:
                largestpandigital = int(totalproducts)
                break
        if len(totalproducts) > 9:
            break
        aproduct = str(i*j)
        if len(aproduct) != len(set(aproduct)):
            break
        else:
            products.append(aproduct)
        
print largestpandigital