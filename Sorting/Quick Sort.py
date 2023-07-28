def quickSort(arr, low, high):
    # code here
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p)
        quickSort(arr, p + 1, high)


def partition(arr, low, high):
    # code here
    i = low - 1
    j = high + 1
    pivot = arr[low]
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


arr = [10, 80, 30, 90, 40, 50, 60]
quickSort(arr, 0, len(arr)-1)
print(arr)