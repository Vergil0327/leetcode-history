### 2 DFS + Suffix Sum Calculation

1. inorder traversal to get all the values in order
2. calculate suffix sum
3. assign computed value back to node

### One Pass DFS Solution

- inorder traversal from left subtree to right subtree
  - get values in increasing order

- inorder traversal from right subtree to left subtree
  - get values in decreasing order

according to BST's inorder feature and our solution above,
we can use inorder DFS traversal from right subtree to left subtree to calculate and accumulate node's value