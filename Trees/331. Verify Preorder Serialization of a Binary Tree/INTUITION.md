# Intuition

since it guarentee every node has 2 child node including NULL (represented by #), we can keep tracking of total number of child node. check if it is valid or not while we iterate through

# Approach

1. first pop out root node
2. if root node is not `#`, it means we need two child node for it.
   - if root node is `#` (NULL) and `preorder` is not empty, it's **invalid**
3. while iterating through rest of `preorder`, each time we pop out one node from `preorder`, decrement total number by 1 but don't forget to check:
   - if new node popped out from `preorder` is not `#`, we need to increment number of child node we need by 2
   - whenever child node we need reach 0, we need to check if there exists more node in `preorder`. if `preorder` is not empty, it means `preorder` is **invalid**
4. after iterating all over the `preorder`, return **True** if number of child node we need reaches 0

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$