from longestIncreasingSequence import lIS
from longestDecreasingSequence import lds


def bioTonicSeq(arr):
    n = len(arr)
    lis_dp = lIS(arr)
    lds_dp = lds(arr)
    res = 0
    for i in range(n):
        res = max(res, lds_dp[i] + lis_dp[i] - 1)
    return res


arr = [1, 11, 2, 10, 4, 5, 2, 1]
print(bioTonicSeq(arr))
