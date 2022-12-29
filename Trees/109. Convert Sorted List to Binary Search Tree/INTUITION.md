# Intuition

1. 題目給的Linked List是有序的
2. BST 的inorder也是有序的

因此我們可以透過inorder DFS反過來建構BST

首先先遍歷Linked List拿到中序遍歷的數值

而中序遍歷的特點是root node會是整個array的中央，因此我們可以每次遞歸把`mid`建立成node
然後再個別對剩下的左半邊及右半邊array繼續遞歸建立

**base case**

- l > r，不合法，返回None
- l == r，返回TreeNode(nums[l])

# Complexity

- time complexity
$$O(n)$$

- space complexity

$$O(n)$$

# Space-Optimized O(1)

那既然我們知道建構好的樹的中序遍歷結果會是Linked List

那我們也可以直接透過中序遍歷的位置反過來建構這個BST

1. 首先遍歷Linked List得知整個TreeNode的總數
2. 再來跟space O(n)解法一樣概念去建構，只是我們是在中序位置上建構，這樣建構的順序剛好就會是Linked List的順序. (因為中序遍歷的結果就會是Linked List)

```
def build(l, r):ad
    if l > r: return None

    mid = l + (r-l)//2
    left = build(l, mid-1)

    # inorder position
    # construct TreeNode
    # move LinkedList head pointer

    root.right = build(mid+1, r)
    return root
```