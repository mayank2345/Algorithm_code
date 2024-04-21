# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         minI = i
#         for j in range(i+1, n):
#             if arr[j] < arr[minI]:
#                 minI = j
#         arr[i], arr[minI] = arr[minI], arr[i]
#
# def insertionSort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i-1
#         while j >=0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -=1
#         arr[j+1] = key
#
#
# def dutchFlag(arr):
#     n = len(arr)
#     l,m = 0,0
#     r = len(arr)-1
#     while m<=r:
#
#         if arr[m] == 0:
#             arr[l],arr[m] = arr[m],arr[l]
#             m += 1
#             l += 1
#
#         elif arr[m] == 1:
#             m += 1
#
#         else:
#             arr[m], arr[r] = arr[r], arr[m]
#             r -= 1
#
# def revList(arr):
#     l = 0
#     r = len(arr)-1
#     while l<=r:
#         arr[l], arr[r] = arr[r], arr[l]
#         r -= 1
#         l += 1
#
#
# def kadane(arr):
#
#     cursum = arr[0]
#     res = arr[0]
#     n = len(arr)
#     for i in range(1, n):
#         cursum = max(arr[i], arr[i]+cursum)
#         res = max(cursum, res)
#
#     return res
#
# def evenOddSubArray(arr):
#
#     res = 1
#     cur = 1
#     n = len(arr)
#     for i in range(1,n):
#         if (arr[i]%2 == 0 and arr[i-1]%2 != 0) or (arr[i]%2 !=0 and arr[i-1]%2 == 0):
#             cur += 1
#             res = max(res, cur)
#         else:
#             cur = 1
#     return res
#
# def mergeSort(arr, l, r):
#     if l < r:
#         m = (l+r)//2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         merge(arr, l, m, r)
#
# def merge(arr, l, m, r):
#
#     left = arr[l:m+1]
#     right = arr[m+1:r+1]
#     i, j, k = 0, 0, l
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#             k += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#             k += 1
#
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1
#
#     return arr
#
# def quickSort(arr, l, h):
#     if l < h:
#         p = lomuto(arr, l , h)
#         quickSort(arr, l, p-1)
#         quickSort(arr, p+1, h)
#
# def lomuto(arr, l, h):
#     pivot = arr[h]
#     i = l-1
#     for j in range(l, h):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[h], arr[i+1] = arr[i+1],arr[h]
#     return i+1
#
#

def quickSort(arr, l , r):
    if l < r:
        p = lomuto(arr, l, r)
        quickSort(arr, l, p-1)
        quickSort(arr, p+1, r)

def lomuto(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1


arr = [87,45,67,23,9]
# arr = [1,1,1,2,2,0,0]
# dutchFlag(arr)
# k = evenOddSubArray(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)