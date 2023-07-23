# Intuition

建構題, 看起來必須透過backtracking來建構每一種可能

這題的突破口是要想如何分配這n個node到左子樹或右子數

我們用DFS來遞歸建構一棵樹的話:
如果當前有`n`個node我們可以有以下組合:
1個作為root node
可以分配numLeft = 1~n-1個node到左子樹, n-1-numLeft到右子樹
然後遞歸建構所有可能
```py
for numLeft in range(n):
    numRight = n-numLeft-1 # 1 for root node

    leftSubtree = backtracking(numLeft)
    rightSubtree = backtracking(numRight)
```

那要遞歸到什麼時候停止?

**base case**

- if n == 0, return []
- if n == 1, return [TreeNode]

那這樣我們就有左子樹跟右子樹的root node
再來就來組合左右子樹, 然後再返回當前所有可能root node

```py
res = []

[rootL1, rootL2, ...] = backtracking(numLeft)
[rootR1, rootR2, ...] = backtracking(numRight)
for left in [rootL1, rootL2, ...]:
    for right in [rootR1, rootR2, ...]:
        root = TreeNode(0, left, right)
        res.append(root)
return res
```

最後記得配合memorization