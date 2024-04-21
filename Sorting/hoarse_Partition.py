def hoarsePartition(arr, n):
    pivot = arr[0]
    l = 0
    h = n - 1
    i = l - 1
    j = h + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return arr, j
        arr[i], arr[j] = arr[j], arr[i]


arr = [2, 5, 1, 7, 9, 11, 12]
print(hoarsePartition(arr, len(arr)))
