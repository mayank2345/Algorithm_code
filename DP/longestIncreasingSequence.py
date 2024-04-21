from bisect import bisect_left


# O(NlogN) method.
# def lis(arr):
#     n = len(arr)
#     tail = [arr[0]]
#     for i in range(1, n):
#         if arr[i] > tail[-1]:
#             tail.append(arr[i])
#         else:
#             c = bisect_left(tail, arr[i])
#             tail[c] = arr[i]
#     return len(tail)

def lIS(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return lis


arr = [1, 11, 2, 10, 4, 5, 2, 1]
print(lIS(arr))
