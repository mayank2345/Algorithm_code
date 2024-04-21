def snake(mat):
    rows = len(mat)
    cols = len(mat[0])
    a = []
    for i in range(rows):
        for j in range(cols):
            if i % 2 == 0:
                a.append(mat[i][j])

            else:
                a.append(mat[i][-j-1])
    return a



mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(snake(mat))
