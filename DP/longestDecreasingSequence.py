def lds(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n - 1, 0, -1):
        for j in range(n-1,i-1,-1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


arr = [1, 11, 2, 10, 4, 5, 2, 1]
print(lds(arr))
