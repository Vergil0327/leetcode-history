"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def build(grid, row0, row1, col0, col1) -> 'Node':
            for i in range(row0, row1):
                for j in range(col0, col1):
                    if grid[i][j] != grid[row0][col0]:
                        topLeft = build(grid, row0, (row1+row0)//2, col0, (col1+col0)//2)
                        topRight = build(grid, row0, (row0+row1)//2, (col0+col1)//2, col1)
                        bottomLeft = build(grid, (row0+row1)//2,row1, col0, (col0+col1)//2)
                        bottomRight = build(grid, (row0+row1)//2,row1,  (col0+col1)//2, col1)
                        root = Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
                        return root
            return Node(grid[row0][col0], True)

        return build(grid, 0, n, 0, n)

# TLE
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m, n = len(grid), len(grid[0])
        def check(row0, row1, col0, col1):
            target = grid[row0][col0]
            for x in range(row0, row1):
                for y in range(col0, col1):
                    if grid[x][y] != target: return False
            return True

        def build(row0, row1, col0, col1):
            if check(row0, row1, col0, col1):
                return Node(grid[row0][col0] == 1, True)
            else:
                root = Node(False, False)
                root.topLeft = build(row0, row1//2, col0, col1//2)
                root.topRight = build(row0, row1//2, col1//2, col1)
                root.bottomLeft = build(row1//2, row1, col0, col1//2)
                root.bottomRight = build(row1//2, row1, col1//2, col1)
                return root
            
        return build(0, m, 0, n)

# use length
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def build(row0, col0, length):
            if length == 1: return Node(grid[row0][col0] == 1, True)

            topLeft = build(row0, col0, length//2)
            topRight = build(row0, col0 + length//2, length//2)
            bottomLeft = build(row0+length//2, col0, length//2)
            bottomRight = build(row0 + length//2, col0 + length//2, length//2)

            if (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf):
                return Node(topLeft.val, True)
            
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
            
        return build(0, 0, n)