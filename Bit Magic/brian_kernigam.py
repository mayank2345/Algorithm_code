# Traverse only through set bit

def countSetBit(n):
    res = 0
    while n:
        n = n & (n-1)
        res += 1
    return res


print(countSetBit(5))