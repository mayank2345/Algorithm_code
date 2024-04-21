def longestSubsequence(a, n):
    dp = [0] * (n)
    dp[0] = 1
    for i in range(1, n):

        if a[i] > a[i-1]:
            dp[i] = 1 + dp[i-1]
        elif a[i] < a[:i-1]:
            dp[i] = 1
    return dp


a = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(longestSubsequence(a, len(a)))