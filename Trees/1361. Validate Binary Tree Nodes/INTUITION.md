# Intuition

一個合法的binary tree, 每個節點應該只會有一個parent node或本身就是root node

所以首先可以先找出有哪些可能的root node

```py
# find possible root
left = set(leftChild)
right = set(rightChild)

root = -1
for node in range(n):
    if node not in left and node not in right:
        if root != -1: return False # should only 1 root node
        root = node
```

再來就用dfs來看我們能不能遍歷到整棵樹, 遍歷的節點總數應為`n`