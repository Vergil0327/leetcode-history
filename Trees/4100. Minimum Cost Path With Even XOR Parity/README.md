[4100. Minimum Cost Path With Even XOR Parity](https://leetcode.com/problems/minimum-cost-path-with-even-xor-parity/)

`Hard`

You are given a tree with n nodes numbered from 0 to n - 1, represented by a 2D integer array edges. Each edges[i] = [ui, vi, ci] represents an edge between nodes ui and vi with cost ci.

You are also given an integer array values of length n, where values[i] is the value of node i.

A path between two distinct nodes is Balanced-XOR if the bitwise XOR of the values of all nodes on the path, including both endpoints, has an even number of set bits.

The cost of a path is the sum of its edge costs.

Return the minimum cost of a Balanced-XOR path. If no such path exists, return -1.

The number 0 has zero set bits.

Example 1:
Input: edges = [[0,1,4],[0,2,6],[0,3,3],[3,4,5]], values = [3,1,7,1,3]

Output: 7

Explanation:

Balanced-XOR Path	XOR Value	Total Cost
1 - 0 - 2	1 XOR 3 XOR 7 = 5	4 + 6 = 10
1 - 0 - 3	1 XOR 3 XOR 1 = 3	4 + 3 = 7
1 - 0 - 3 - 4	1 XOR 3 XOR 1 XOR 3 = 0	4 + 3 + 5 = 12
2 - 0 - 3	7 XOR 3 XOR 1 = 5	6 + 3 = 9
2 - 0 - 3 - 4	7 XOR 3 XOR 1 XOR 3 = 6	6 + 3 + 5 = 14
The minimum cost is 7, achieved by the path 1 - 0 - 3. Thus, the answer is 7.

Example 2:
Input: edges = [[0,1,5],[1,2,10]], values = [1,7,3]

Output: 5

Explanation:

Balanced-XOR Path	XOR Value	Total Cost
0 - 1	1 XOR 7 = 6	5
0 - 1 - 2	1 XOR 7 XOR 3 = 5	5 + 10 = 15
The minimum cost is 5, achieved by the path 0 - 1. Thus, the answer is 5.

Example 3:
Input: edges = [[0,1,5],[0,2,7],[0,3,9]], values = [1,3,5,9]

Output: -1

Explanation:

Every path between two distinct nodes has an XOR value with an odd number of set bits.
Therefore, no Balanced-XOR path exists, so the answer is -1.
 

Constraints:

- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i] = [ui, vi, ci​​​​​​​]
- 0 <= ui, vi <= n - 1
- 1 <= ci <= 10^9
- values.length == n
- 1 <= values[i] <= 10^9
- edges represents a valid tree.

Accepted
2,484/4.6K
Acceptance Rate
54.1%

<details>
<summary>Hint 1</summary>

1a (Tree DP): Replace each node value with the parity of its set-bit count. The original condition becomes requiring the XOR of these parities along the path to be zero.
</details>
<details>
<summary>Hint 2</summary>

1b (Tree DP): For each node, maintain the minimum cost of a downward path starting there for each possible parity, including the starting node. Initialize its single-node path with cost zero.
</details>
<details>
<summary>Hint 3</summary>

1c (Tree DP): Process children one at a time. Matching parities between an already processed path from the current node and a downward path from a child give a balanced path after adding the connecting edge. Combine before updating the current node's states to avoid reusing a child.
</details>
<details>
<summary>Hint 4</summary>

2a (Local Paths): Replace each value with its set-bit parity. An edge alone is balanced exactly when its endpoint parities agree.
</details>
<details>
<summary>Hint 5</summary>

2b (Local Paths): If a balanced path has no such edge, its parities alternate and it contains a three-node subpath with parities 1, 0, 1. Since edge costs are positive, an optimal path needs at most two edges.
</details>
<details>
<summary>Hint 6</summary>

2c (Local Paths): Check all balanced edges. For each node of parity zero, also consider the sum of its two cheapest incident edges leading to distinct neighbors of parity one.
</details>