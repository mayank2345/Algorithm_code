def subarraysWithSumK(a: [int], k: int) -> [[int]]:
    # Write your code here
    s = []
    res = []
    su = 0
    subseq(0, s, su, res, a, k)
    return res


def subseq(i, s, su, res, a, k):
    if i == len(a):
        if su == k and s[:] not in res:
            res.append(s[:])
        return
    s.append(a[i])
    su += a[i]
    subseq(i + 1, s, su, res, a, k)
    su -= s.pop()
    subseq(i + 1, s, su, res, a, k)


arr = [1, 2, 1]
print(subarraysWithSumK(arr, 3))
