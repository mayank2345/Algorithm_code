def binToDec(n):
    res = 0
    i = 0
    while n > 0:
        d = n & 1
        res += d * (2 ** i)
        i += 1
        n = n // 10
    return res


print(binToDec(10010))
