def threeSum(arr, t):
    for i in range(len(arr)):
        d = {}
        for j in range(i + 1, len(arr)):
            v = t - (arr[i] + arr[j])
            if v in d:
                return i, d[v], j
            d[arr[j]] = j

    return False


arr = [1,2,4,4]
print(threeSum(arr, 6))
