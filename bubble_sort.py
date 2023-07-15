# Bubble sort
def bubble_sort(arr, n):
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if swapped == False:
                break
    return arr
    
arr = [7,5,8,32,75,35,21]
print(bubble_sort(arr, len(arr)))
