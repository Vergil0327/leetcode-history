# Intuition

看了一下example1, 最佳選擇肯定是`x`節點的某個鄰接節點

由於不可跨越不同顏色節點, 所以只要有任一子樹個數大於另兩個子樹和, 那就代表存在一個節點`y`能勝過`x`

感覺首先建構出整個graph後, 我們就從`x`節點出發, 出發有三個方向:
1. 父節點子樹: 假設該子樹大小為A
2. 左子樹: 假設該子樹大小為B
3. 右子樹: 假設該子樹大小為C

那麼只要任意(A or B or C)**大於**另兩個子樹和+1(x節點自身), 那麼必定存在一節點能贏過`x`

# Approach

先用DFS建構出DFS, 然後再往`x`的鄰接方向進行BFS求出各方向子樹和即可

# Complexity

time: O(n)
space: O(n)

# Intuition - DFS

另外也能純粹用DFS即可, 無需BFS:

- leftX: left subtree size of `x`
- rightX: right subtree size of `x`
- upperX: parent subtree size of `x`

```py
leftX = rightX = 0
def dfs(node):
    nonlocal leftX, rightX

    if not node: return 0

    l = dfs(node.left)
    r = dfs(node.right)
    if node.val == x:
        leftX, rightX = l, r

    return l + r + 1

total = dfs(root)

upperX = (total-leftX-rightX-1)
res = max(leftX, rightX, upperX)
return  res > total-res
```

# Optimized

另又個很精妙的dfs能一次遍歷求出`x`節點的三個方向子樹大小

```py
def dfs(node):
    if not node:
        return 0, 0, 0
    if node.val == x:
        l, _, _ = dfs(node.left)
        r, _, _ = dfs(node.right)
        return 0, l, r
    c1, l1, r1 = dfs(node.left)
    c2, l2, r2 = dfs(node.right)
    return 1 + c1 + c2, l1 + l2, r1 + r2

res = max(dfs(root))
return res > n - res
```