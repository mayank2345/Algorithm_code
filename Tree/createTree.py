from typing import List


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def createTree(arr: List[int]) -> Node:
    # Write your code here.
    return createBinaryTree(arr, 0)


def createBinaryTree(arr, s):
    if s >= len(arr):
        return None
    root = Node(arr[s])
    root.left = createBinaryTree(arr, 2 * s + 1)
    root.right = createBinaryTree(arr, 2 * s + 2)
    return root


arr = [1, 2, 3, 4, 5, 6, 7]
print(createTree(arr))