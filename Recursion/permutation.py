def permutation(arr):
    res = []
    # ds = []
    # freq = [False]*len(arr)
    # seq(ds, freq, arr, res)
    seq2(0, arr, res)
    
    return res


def seq(ds, freq, arr, res):
    if len(arr) == len(ds):
        res.append(ds.copy())
        return

    for i in range(len(arr)):
        if not freq[i]:
            ds.append(arr[i])
            freq[i] = True
            seq(ds, freq, arr, res)
            ds.pop()
            freq[i] = False


def seq2(ind, arr, res):
    if ind == len(arr):
        res.append(arr[:])
        return

    for i in range(ind,len(arr)):
        arr[ind], arr[i] = arr[i], arr[ind]
        seq2(ind + 1, arr, res)
        arr[ind], arr[i] = arr[i], arr[ind]


arr = [1, 2, 3]
print(permutation(arr))
