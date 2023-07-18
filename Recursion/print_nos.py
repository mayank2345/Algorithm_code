from typing import List


def printNos(x: int) -> List[int]:
    if x == 1:
        return [1]
    else:
        number = printNos(x - 1)
        number.append(x)
        return number


# Driver code

arr = printNos(5)  # By default recursion set limit is 1000
print(arr)
