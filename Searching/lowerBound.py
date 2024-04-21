def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    l = 0
    r = n - 1
    if x > max(arr):
        return n
    mid = n
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= x:
            ans = m
            r = m - 1
        elif arr[m] < x:
            l = m + 1
    return m


arr = [1, 2, 2, 3, 3, 5]
x = 2
print(lowerBound(arr, len(arr), x))
