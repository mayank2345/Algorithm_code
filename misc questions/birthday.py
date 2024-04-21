"""Your birthday is coming soon and one of your friends, Alex, is thinking about a gift for you. He knows that you
really like integer arrays with interesting properties.

He selected two numbers, N and K and decided to write down on paper all integer arrays of length K (in form a[1],
a[2], …, a[K]), where every number a[i] is in range from 1 to N, and, moreover, a[i+1] is divisible by a[i] (where 1
< i <= K), and give you this paper as a birthday present.

Alex is very patient, so he managed to do this. Now you’re wondering, how many different arrays are written down on
this paper?

Since the answer can be really large, print it modulo 10000.

Input:

The first line contains an integer, n, denoting the maximum possible value in the arrays.
The next line contains an integer, k, denoting the length of the arrays.
"""


def count_arrays(N, K):
    # Initialize a 2D array to store the count of valid arrays
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # Initialize base case: there is one way to create an array of length 1 for each value in the range
    for i in range(1, N + 1):
        dp[1][i] = 1

    # Use dynamic programming to calculate the count of valid arrays
    for k in range(2, K + 1):
        for n in range(1, N + 1):
            for i in range(n, N + 1, n):
                dp[k][i] = (dp[k][i] + dp[k - 1][n]) % 10000

    # Sum up the counts for all possible ending values in the last array
    result = sum(dp[K]) % 10000

    return result


print(count_arrays(5,5))