# from mathQ.combination import ncr
# def pascalTriangle(n):
#     triangle = [[0]*n for _ in range(n)]
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             element = ncr(i-1,j-1)
#             triangle[i-1][j-1] = element
#     return triangle

def generateRow(n):
    res = [1]
    cur = 1
    for i in range(1, n):
        cur = cur * (n-i)
        cur = cur // i
        res.append(cur)
    return res

def generatePasacalTriangle(n):
    res = []
    for i in range(1, n+1):
        res.append(generateRow(i))
    return res



print(generatePasacalTriangle(4))
