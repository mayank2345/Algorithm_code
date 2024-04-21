def findMax(arr):
    res = -float('inf')
    for i in range(len(arr)):
        if arr[i] > res:
            res = arr[i]
    return res

def findMin(arr):
    res = float('inf')
    for i in range(len(arr)):
        if arr[i] < res:
            res = arr[i]
    return res

def findSecMax(arr):
    maxV = -float('inf')
    secMax = -float('inf')
    for i in range(len(arr)):
        if arr[i] > maxV:
            secMax = maxV
            maxV = arr[i]
        if arr[i] != maxV and arr[i] > secMax:
            secMax = arr[i]
    return secMax

def findSecMin(arr):
    minV = float('inf')
    secMin = float('inf')
    for i in range(len(arr)):
        if arr[i] < minV:
            secMin = minV
            minV = arr[i]
        if arr[i] != minV and arr[i] > secMin:
            secMin = arr[i]
    return secMin


arr = [23,45, 12, 46, 75, 93, 34,5]
print(f"Max Value:{findMax(arr)}")
print(f"Min Value:{findMin(arr)}")
print(f"SecMax Value:{findSecMax(arr)}")
print(f"SecMin Value:{findSecMin(arr)}")
