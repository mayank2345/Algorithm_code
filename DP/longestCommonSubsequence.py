M, N = 1000, 1000
memo = [[-1] * N for _ in range(M)]


# def lcs(s1, s2, m, n):
#     if memo[m][n] != -1:
#         return memo[m][n]
#     if n == 0 or m == 0:
#         memo[m][n] = 0
#     else:
#         if s1[m - 1] == s2[n - 1]:
#             memo[n][m] = 1 + lcs(s1, s2, m - 1, n - 1)
#         else:
#             memo[m][n] = max(lcs(s1, s2, n, m - 1), lcs(s1, s2, n - 1, m))
#
#     return memo[m][n]


def lcs(s1, s2, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = ''
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res += s1[i-1]
            i -= 1
            j -= 1
        elif dp[i-1] > dp[j-1]:
            i -= 1
        else:
            j -= 1
    return res

s1= 'AGGTAB'
s2= 'GXTXAYB'
print(lcs(s1 ,s2 , len(s1), len(s2)))
