def numberRev(n):
    res = 0
    temp = n
    while temp > 0:
        res = res*10 + temp%10
        temp = temp//10

    return res

print(numberRev(1234))