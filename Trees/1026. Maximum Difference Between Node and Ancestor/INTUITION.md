# Intuition
during recursion, preorder DFS can keep tracks of `currMin` & `currMax`
since postorder comes after preorder, `currMin` & `currMax` must be valid ancestor in postorder DFS.

till the leaf nodes, we can use postorder to calculate each node with `currMin` & `currMax`


# Approach
- we need to keep tracks of `currMin` & `currMax`
- find `currMin` & `currMax` in preorder DFS
- compute `diff` in postorder DFS

our base case:
whenever leaf node is `None`, we return `currMax` since `currMax` is valid value.
I think returning `currMin` is fine

we can't return something like `0` or `inf`, we'll compute wrong `diff`

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(recursion)$$
