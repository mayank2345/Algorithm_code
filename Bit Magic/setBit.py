"""
Set the rightmost unset bit
"""


def setBit(n) -> int:
    temp = n & (n + 1)
    if temp == 0:
        return n
    return n | (n + 1)


print(setBit(7))
