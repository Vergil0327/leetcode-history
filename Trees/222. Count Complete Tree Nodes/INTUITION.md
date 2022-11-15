## Binary Search

if we label every nodes from index `1` to `n`, just like `Example 1`,
we can use binary search to guess `how many nodes in this complete tree` since this binary tree is complete tree

- how to guess K if K is total number of nodes?
  1. if our label starts from 1 to n, we can see that:

        - left-child's index = root's index * 2
        - right-child's index = root's index * 2 + 1
        - then we can build a path from root to K by
      ```python
      k //= 2 -> k //= 2 -> ... -> root

      # left-child is 2*root.val
      # right-child is 2*root.val+1
      pathToK = []
      while k > 0:
          pathToK.append(k)
          k //= 2
      ```
  2. check if there is a path from root to K based on path of K-to-root
     
     - pathToK[-1] should be root if root not None
     - so we can iterate pathToK reversely to check if K exists or not

        ```python
        # starts from root (pathToK[-1])
        for i in range(len(pathToK), -1, -1):
          if not root: return False # tree's last index < K
          if i == 0: return True # found K

          if pathToK[i-1] == 2 * pathTOK[i]: # goes from root from current to left node
            root = root.left
          else: # goes from current to right node
            root = root.right
        ```

then we can use our guess function to do binary search.

search space should start from `left-most index at level of max height` to `right-most index at level of max height`

since max height of complete tree can easily be found by:
```python
h = 0
curr = root
while curr:
    h += 1
    curr = curr.left
```

so our search space should be `[2**(h-1), 2**h-1]`
and we can start our binary search

## Recursion, Divide & Conquer

for complete binary tree, we can keep finding if left subtree is a complete tree or not

- if right subtree's height == left subtree's height, left subtree must be a complete tree

therefore,
hLeft = left subtree's max height
hRight = right subtree's maxheight
- if `hLeft == hRight`, left subtree is complete and keep finding right subtree
  - `count += 2**hLeft - 1`
- if `hLeft != hRight`, right subtree is complete and keep finding left subtree
  - `count += 2**hRight - 1`

```
 1
2 3

hLeft = 1
hRight = 1
count = 1(root) + 1 + dfs(root.right) = 1 + 1 + 1
```

```
  1
 2 
hLeft = 1
hRight = 0
count = 1(root) + 2**0-1 + dfs(root.left)
      = 1 + 0 + (1 + 0 + 0)
      = 2
```