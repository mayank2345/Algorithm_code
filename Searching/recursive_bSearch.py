def recursiveBs(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        return recursiveBs(arr, x, mid + 1, high)
    if arr[mid] > x:
        return recursiveBs(arr, x, low, mid - 1)


# Driver code
arr = [2, 5, 7, 9, 13, 15, 17]
low = 0
high = len(arr) - 1
print(recursiveBs(arr, 12, low, high))
