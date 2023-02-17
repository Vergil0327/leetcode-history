# Intuition

這題想法很簡單，就是DFS去找出最長的path
基本框架就是:

```py
longest = 0
def dfs(root):
    nonlocal longest
    if not root: return 0

    leftPath = dfs(root.left)
    rightPath = dfs(root.right)
    longest = max(longest, leftPath+rightPath+1)
    return max(leftPath, rightPath) + 1
```

我們遞歸找出單一條沒有分岔的最長路徑，也就是左右子節點挑最長的再加上自身，`max(leftPath, rightPath) + 1`

而對於每個節點來說，最長的path就是他的兩個子節點的最長路徑再加上節點本身, `leftPath+rightPath+1`

如此一來，我們就能得到最長路徑

只是這題還加上個限制，那就是只有節點跟子節點的數值相同時，才能算上是合法路徑

所以我們就判斷左右兩節點有沒有跟根節點有相同的數值，如果有相同，該子節點的最長路徑才是合法路徑

所以找出合法子節點路徑後，其餘的邏輯就跟一般求最長路徑一樣了


```py
def dfs(root):
    nonlocal longest
    if not root: return 0

    left = dfs(root.left)
    right = dfs(root.right)
    
    candidates = []
    if root.left and root.left.val == root.val:
        candidates.append(left)
    if root.right and root.right.val == root.val:
        candidates.append(right)
    candidates.sort(reverse=True)

    longest = max(longest, sum(candidates[:2]))
    return (candidates[0]+1) if candidates else 1
```