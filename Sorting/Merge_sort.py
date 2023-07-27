def mergeSort(arr, L, R):
    if L<R:
        mid = (L+R)// 2
        mergeSort(arr, L, mid)
        mergeSort(arr, mid + 1, R)
        merge(arr, L, mid, R)


def merge(arr, L, mid, R):
    left = arr[L: mid + 1]
    right = arr[mid + 1: R + 1]
    i, j = 0, 0
    k = L
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


arr = [5, 2, 7, 1, 8, 10, 3, 25, 12]
mergeSort(arr,0, len(arr)-1)
print(arr)
