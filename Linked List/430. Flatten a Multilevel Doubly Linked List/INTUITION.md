# Intuition

use DFS to flatten.

想成一棵樹, 我們進行preorder dfs traversal把所有node依順序連接再一起即可

這邊我們用`stack`進行iterative way of DFS

首先用一個`dummy` node作為result node, 然後依序將linked list node一個個接在後面
最終答案即為:

```py
# dfs

res = dummy.next
if res:
    res.prev = None 
return res
```