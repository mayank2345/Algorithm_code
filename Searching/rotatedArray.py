def firstAndLastPosition(arr, n, k):
    # Write your code here
    l, r = 0, n - 1

    while l <= r:

        m = (l + r) // 2
        if arr[m] == k:
            return m
        elif arr[l] <= arr[m]:

            if arr[l] <= k <= arr[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if arr[r] >= k >= arr[m]:

                l = m + 1
            else:
                r = m - 1
    return -1


arr=[1,0,1,1,1]
print(firstAndLastPosition(arr,len(arr),0))