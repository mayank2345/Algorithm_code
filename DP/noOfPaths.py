def NumberOfPaths(a, b):
    # code here
    dp = [[0] * (a + 1) for _ in range(b + 1)]
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[a][b]

print(NumberOfPaths(3,3))
