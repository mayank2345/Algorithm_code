def ncr(n,r):
    res = 1
    for i in range(r):
        res = res*(n-i)
        res = res//(i+1)
    return res

def pascalElement(r,c):
    return ncr(r-1,c-1)


print(pascalElement(7,4))