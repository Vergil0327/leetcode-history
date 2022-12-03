### Intuition - 3 DFS

first, the most important thing we need to know is that
the shortest path is `startValue -> LCA -> destValue`

if we can observe and know this, the problem is just 3 steps:

1. find LCA
2. find LCA to startValue
	-  find how many levels should we go up from startValue to LCA.
3. find LCA to destValue
	- post-order DFS traversal to find `destValue -> LCA`.
	- reverse path to get `LCA -> destValue`
	- if destValue itself is LCA, we can skip step 3.


### Intuition of Solution 2 - DFS backtracking

we can use DFS traverse and backtracking to find path to `startValue` and `destValue`,

after that, we need to remove their common ancestor path

lastly, we replace `path to startValue` with `"U"` and plus `path to destValue`

and the result is answer