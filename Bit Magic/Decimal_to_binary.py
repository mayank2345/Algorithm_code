def decToBin(n):
    res = ''
    while n > 0:
        b = n & 1
        res = str(b) + res
        n = n >> 1
    return res


print(decToBin(25))
