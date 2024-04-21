def twoSum(arr, t):

    d = {}
    for i in range(len(arr)):
        v = t - arr[i]
        if v in d:
            return d[v],i
        d[arr[i]] = i


arr = [2,4,5,3,1]
print(twoSum(arr, 4))

