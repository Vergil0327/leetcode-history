# Intuition

這題很明顯是用recursion來建構樹
首先很自然地想到用row, col跟mid逐漸遞歸出四個子樹，直到一格為止的遞歸方式

我們可以用 preorder
```py
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
        root.topLeft = build(row0, (row1+row0)//2, col0, (col1+col0)//2)
        root.topRight = build(row0, (row0+row1)//2, (col0+col1)//2, col1)
        root.bottomLeft = build((row0+row1)//2,row1, col0, (col0+col1)//2)
        root.bottomRight = build((row0+row1)//2,row1,  (col0+col1)//2, col1)
        return root
    
return build(0, m, 0, n)
```

或是利用 postorder
```py
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
        topLeft = build(row0, (row1+row0)//2, col0, (col1+col0)//2)
        topRight = build(row0, (row0+row1)//2, (col0+col1)//2, col1)
        bottomLeft = build((row0+row1)//2,row1, col0, (col0+col1)//2)
        bottomRight = build((row0+row1)//2,row1,  (col0+col1)//2, col1)
        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
    
return build(0, m, 0, n)
```

注意:
row0 跟 row1的mid是: `(row1+row0)//2` 而不只是 `row1//2`

# Complexity
- time complexity:

$$O(N^2)$$
All the cells in the matrix will be iterated only once

- space complexity:

$$O(log⁡N)$$

the recursion call stack


# Other Solution (Golang)

Based on description, we can define a dfs called `build` as:

`build(r0, r1, c0, c1): return root node of Quad Tree which ranges from row=r0 to row=r1 and column=c0 to column=c1`

and we start our recursion from top to bottom: `build(0, n-1, 0, n-1)`

1. first, we can easily define our base case: we should top when our recursion reach single cell
    ```go
    if r0==r1 and c0==c1 {
        // val is true if grid[r0][c0] == 1 else false
        return &Node{Val: val, IsLeaf: true}
    }
    ```
2. check if we can merge all four section `bottomLeft`, `bottomRight`, `topLeft`, `topRight` into one single leaf node or just return a node with these four section
    - we can merge these four section and return `&Node{Val: bottomRight.Val, IsLeaf: true}` only if we meet this condition:
        ```
        topLeft.IsLeaf && bottomLeft.IsLeaf &&
        topRight.IsLeaf && bottomRight.IsLeaf &&
        topLeft.Val == bottomLeft.Val &&
        bottomLeft.Val == topRight.Val &&
        topRight.Val == bottomRight.Val
        ```
    - or we just return:
        ```
        &Node{Val: false, IsLeaf: false, TopLeft: topLeft, TopRight: topRight, BottomLeft: bottomLeft, BottomRight: bottomRight}
        ```

# Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(logn)$$

# Code
```go
/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func construct(grid [][]int) *Node {
    n := len(grid)

    var build func(r0, r1, c0, c1 int) *Node
    build = func(r0, r1, c0, c1 int) *Node {
        if r1 == r0 && c1 == c0 {
            var val bool
            if grid[r0][c0] == 1 {
                val = true
            }
            return &Node{Val: val, IsLeaf: true}
        }

        midR := r0 + (r1-r0)/2
        midC := c0 + (c1-c0)/2
        topLeft := build(r0, midR, c0, midC)
        bottomLeft := build(midR+1, r1, c0, midC)
        topRight := build(r0, midR, midC+1, c1)
        bottomRight := build(midR+1, r1, midC+1, c1)
        if topLeft.IsLeaf && bottomLeft.IsLeaf && topRight.IsLeaf && bottomRight.IsLeaf && topLeft.Val == bottomLeft.Val && bottomLeft.Val == topRight.Val && topRight.Val == bottomRight.Val {
            return &Node{Val: bottomRight.Val, IsLeaf: true}
        }

        return &Node{Val: false, IsLeaf: false, TopLeft: topLeft, TopRight: topRight, BottomLeft: bottomLeft, BottomRight: bottomRight}
    }
    return build(0, n-1, 0, n-1)
}
```
