# Intuition
first, since we need `n-1` edges at least to connect `n` node, if `len(connections) < n-1`, we can return -1 directly.

then we just need to find how many connected components exists.
if there are `m` connected components, we need `m-1` operations.

# Complexity
- Time complexity:
$$O(n)$$ approximately

- Space complexity:
$$O(n)$$
