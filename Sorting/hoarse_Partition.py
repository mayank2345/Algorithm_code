def hoarsePartition(arr, n):
    pivot = arr[0]
    l = 0
    h = n - 1
    i = l - 1
    j = h + 1
    while True:
        i += 1
        if arr[i] < pivot:
            i += 1
        j -= 1
        if arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


arr = [70, 1, 2, 80, 90]
print(hoarsePartition(arr, len(arr)))
