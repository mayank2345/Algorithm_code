from longestIncreasingSequence import lIS
def bridge(arr):
    arr.sort(key=lambda x: (x[0], x[1]))
    s = []
    for i,j in arr:
        s.append(j)
    lis = lIS(s)
    return max(lis)



arr = [[6, 3], [4, 3], [2, 6], [1, 5], [6,2]]
print(bridge(arr))
