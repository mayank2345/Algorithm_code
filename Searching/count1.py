def countOnes(arr, n):
    # Your code here
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        if (mid == high or arr[mid + 1] == 0) and (arr[mid] == 1):
            return mid + 1
        elif arr[mid] == 1:
            low = mid + 1
        else:
            high = mid - 1
    return 0


arr = [1, 1, 1, 0, 0]
print(countOnes(arr, len(arr)))