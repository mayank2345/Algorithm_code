
def selSort(arr,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr


# Driver
arr = [1,1,3,2,2,6,3,2,6,7]
print(selSort(arr, len(arr)))
