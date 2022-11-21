Follow-up of [Leetcode 105. Construct Binary Tree from Preorder and Inorder](../105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/)

### recursion by values

we can observe that

1. by post-order traversal, we can see that root node is the last element. more than that, the second last node is right-subtree's root node
2. when we find root node, we can use inorder array to find nodes of left-subtree and nodes of right-subtree
3. therefore, we can recursively construct tree like leetcode 105. by these two information

### recursion by index

optimized steps:

1. we can reduce time time complexity to use a `hashmap` to store mapping of root node to its index

2. also, we can use `l` and `r` pointer to represent our valid range of `inorder` array rather than copy `inorder` array in every recursion stack

3. we can construct right-subtree first, then left-subtree because the order from last element in `postorder` to first element is the order of root node from right-subtree to left-subtree