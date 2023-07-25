def binarySearch(arr, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2  # mid = 3

        if arr[mid] == x:  # arr[3] != 15
            return mid
        elif arr[mid] < x:  # arr[3] < 15
            low = mid + 1  # change low position
        else:
            high = mid - 1

    return -1


# Driver code

arr = [2, 5, 7, 9, 13, 15, 17]
print(binarySearch(arr, len(arr), 15))
