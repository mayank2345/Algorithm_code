def printAllSubsequences(arr):
    n = len(arr)
    seq, res = [], []
    subsequences(0, arr, seq, res, n)
    return res


def subsequences(i, arr, seq, res, n):
    if i >= n:
        res.append(seq[:])
        return
    seq.append(arr[i])
    subsequences(i + 1, arr, seq, res, n)
    seq.pop()
    subsequences(i + 1, arr, seq, res, n)


arr = [3, 1, 2]
print(printAllSubsequences(arr))
