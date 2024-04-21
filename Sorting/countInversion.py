def invCount(arr, n):
    count = 0
    if n > 1:
        m = n // 2
        l = arr[:m]
        r = arr[m:]
        count += invCount(l, len(l))
        count += invCount(r, len(r))
        i, j, k = 0, 0, 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[i]
                count += len(l)-i
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return count


arr = [2, 4, 1, 3, 5]
print(invCount(arr, len(arr)))
