# Naive approach
def patSearch(s,pat):
    n = len(s)
    m = len(pat)
    i = 0
    while i <= (n-m ):
        j = 0
        while j < m:
            if s[i + j] != pat[j]:
                break
            j+=1
        if j == m:
            print(i, end= " ")
        if j == 0:
            i += 1
        else:
            i += j







s = "abaabaab"
print(ord('z'))
