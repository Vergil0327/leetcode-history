# Intuition

calculate total length and substract LCA to root

two cases:

`u` is max(queries[i]) and `v` is min(queries[i])

1. `v` is LCA of `u`
2. `v` is **NOT** LCA of `u`

# Approach

- first case: (length from v to u) + 1 addional edge
- second case: (length from v to root) + (length from u to LCA) - (length from their LCA to root) + 1 addional edge

and we choose largest index as starting node `v`.

# Complexity

- time complexity
$$O(len(queries) * (log(u) + log(v)))$$

- space complexity
$$O(len(queries) * (log(u) + log(v)))$$ for hashset `path`

# Optimzed Concise Solution

just find node `u` and `v`'s way back until they reach LCA(lowest common ancestor).