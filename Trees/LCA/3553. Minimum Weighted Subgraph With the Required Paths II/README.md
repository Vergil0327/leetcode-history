[3553. Minimum Weighted Subgraph With the Required Paths II](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/)

`Hard`

You are given an undirected weighted tree with n nodes, numbered from 0 to n - 1. It is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an edge between nodes ui and vi with weight wi.​

Additionally, you are given a 2D integer array queries, where queries[j] = [src1j, src2j, destj].

Return an array answer of length equal to queries.length, where answer[j] is the minimum total weight of a subtree such that it is possible to reach destj from both src1j and src2j using edges in this subtree.

A subtree here is any connected subset of nodes and edges of the original tree forming a valid tree.

```
Example 1:
Input: edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]
Output: [12,11]
Explanation:

The blue edges represent one of the subtrees that yield the optimal answer.

answer[0]: The total weight of the selected subtree that ensures a path from src1 = 2 and src2 = 3 to dest = 4 is 3 + 5 + 4 = 12.

answer[1]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 2 to dest = 5 is 2 + 3 + 6 = 11.

Example 2:
Input: edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]
Output: [15]
Explanation:

answer[0]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 1 to dest = 2 is 8 + 7 = 15.
```

Constraints:

- 3 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 3
- 0 <= ui, vi < n
- 1 <= wi <= 10^4
- 1 <= queries.length <= 10^5
- queries[j].length == 3
- 0 <= src1j, src2j, destj < n
- src1j, src2j, and destj are pairwise distinct.
- The input is generated such that edges represents a valid tree.

Accepted
1.9K
Submissions
4.4K
Acceptance Rate
43.9%

<details>
<summary>Hint 1</summary>

Binary lifting

</details>
<details>
<summary>Hint 2</summary>

Find the lowest common ancestor (LCA) of any two nodes using binary lifting

</details>
<details>
<summary>Hint 3</summary>

For any node x, let f(x) be the distance from the root to x. Then for two nodes x and y:d(x, y) = f(x) + f(y) - 2 * f(LCA(x, y))

</details>
<details>
<summary>Hint 4</summary>

For three nodes a, b and c, the minimum total weight of the subtree connecting all three is:(d(a, b) + d(b, c) + d(c, a)) / 2, where d(x, y) is the distance between nodes x and y

</details>
