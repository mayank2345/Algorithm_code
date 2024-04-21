import copy
from typing import List


def nQueens(n: int):
    # Write your code here
    res = []
    board = [['0'] * n for _ in range(n)]
    solveNQueen(0, board, n, res)


    return res
    pass


def solveNQueen(col, board, n, res):
    if col == n:
        res.append(copy.deepcopy(board))
        return

    for row in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = '1'
            solveNQueen(col + 1, board, n, res)
            board[row][col] = '0'


def isSafe(row, col, board, n):
    dupRow = row
    dupCol = col

    while row >= 0 and col >= 0:
        if board[row][col] == '1':
            return False
        row -= 1
        col -= 1

    row = dupRow
    col = dupCol
    while col >= 0:
        if board[row][col] == '1':
            return False
        col -= 1

    row = dupRow
    col = dupCol
    while col >= 0 and row < n:
        if board[row][col] == '1':
            return False
        row += 1
        col -= 1
    return True

print(nQueens(4))