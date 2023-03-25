# Intuition
first, if we have `n` nodes, we'll have $n(n-1)/2$ pairs

then, we find how many connected components exist.

the unreach pairs are `total expected pairs - sum(pairs exist in each connected component)`

As for connected components, we can use **Union-Find** to union each edge by rank/size.

# Complexity
- Time complexity:
$$O(n)$$ approximately

- Space complexity:
$$O(n)$$
