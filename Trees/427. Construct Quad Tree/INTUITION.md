# Intuition

這題很明顯是用recursion來建構樹
首先很自然地想到用row, col跟mid逐漸遞歸出四個子樹，直到一格為止的遞歸方式

```py
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
```

但由於我們每次都用$O(n^2)$時間判斷當前是不是leaf node(每一格值都相同)，這樣複雜度為 $O(n^2logn)$
但實際上我們不需要判斷，我們只要用post-order DFS從底部向上構建回來即可

把原本TLE的建構稍微移動一下位置，把check fn擺回來，一但不是leaf node，便繼續遞歸建構，一但為leaf node，變依據題意返回`Node(grid[row0][col0], True)`即可

注意:

row0 跟 row1的mid是: `(row1+row0)//2` 而不只是 `row1//2`

# Complexity
- time complexity:

$$O(N^2)$$
All the cells in the matrix will be iterated only once

- space complexity:

$$O(log⁡N)$$

the recursion call stack