# Intuition

perfect binary tree的條件是底下左右子樹也都是perfect binary tree
可觀察到perfect binary tree的左右子樹個數都是對稱的, 所以我們可以用post-order traversal dfs來搜索

1. 一但左右子樹相等, 代表從當前根節點開始為perfect binary tree, 我們將個數加入到k-size minimum priority queue
2. 一但不相等, 代表不可能為perfect binary tree, 我們返回不可能相等的數值即可, `inf`或`-inf`

```py
l = dfs(node.left)
r = dfs(node.right)

if l < inf and r < inf and l == r:
    heapq.heappush(pq, l+r+1)
    if len(pq) > k:
        heapq.heappop(pq)
    return l + r + 1
else:
    return inf
```

```py
l = dfs(node.left)
r = dfs(node.right)

if l == r and (size := l+r+1) > 0:
    heapq.heappush(pq, size)
    if len(pq) > k:
        heapq.heappop(pq)
    return size
else:
    return -inf
```

全部結束後, 如果pq.size有足夠k個, 那麼pq[0]即為k-th largest size
不然則為-1


time: O(nlogk)
space: O(k)