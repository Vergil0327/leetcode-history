# Intuition

首先BST的中序遍歷為由小到的排列

再來對於一個BST，最小的數肯定是從根節點一路往左節點找

那我們會發現我們要的順序正好反過來，因此我們可以用`stack`來儲存

而對於每個節點來說下個次大的節點要麻就是:
1. 他的父節點
2. 不然就是先往右節點走後，再一路往左節點找

這時我們可以發現規律:
每當呼叫`next`將當前節點從`stack`取出來時，我們可以將他的右節點作為根節點一路往左找，找出下個次大的節點
同時一路上的節點都存進`stack`裡

# Further Reading

**Iterative Inorder Traversal**

```python
inorder = []
stack = []
while stack or root:
    if root:
        stack.append(root)
        root = root.left
    else:
        last = stack.pop()
        inorder.append(last.val)
        root = last.right
```
