def printBoundary(mat):
    rows = len(mat)
    cols = len(mat[0])

    if rows == 1:
        # Only one row, print all elements
        print(*mat[0], end=' ')
    elif cols == 1:
        # Only one column, print all elements
        for i in range(rows):
            print(mat[i][0], end=' ')
    else:
        # Print top row
        for i in range(cols):
            print(mat[0][i], end=' ')

        # Print right column
        for i in range(1, rows):
            print(mat[i][cols-1], end=' ')

        # Print bottom row (in reverse order)
        for i in range(cols-2, -1, -1):
            print(mat[rows-1][i], end=' ')

        # Print left column (in reverse order)
        for i in range(rows-2, 0, -1):
            print(mat[i][0], end=' ')


mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
printBoundary(mat)


