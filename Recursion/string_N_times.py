from typing import *


def printNtimes(n: int) -> None:
    if n == 0:
        return None
    else:
        print("Mayank", end=" ")
    return printNtimes(n - 1)

# Driver Code

printNtimes(5)