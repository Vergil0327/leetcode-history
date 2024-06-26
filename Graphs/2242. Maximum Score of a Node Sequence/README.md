[2242. Maximum Score of a Node Sequence](https://leetcode.com/problems/maximum-score-of-a-node-sequence/)

`Hard`

There is an undirected graph with n nodes, numbered from 0 to n - 1.

You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A node sequence is valid if it meets the following conditions:

There is an edge connecting every pair of adjacent nodes in the sequence.
No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.

Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.

```
Example 1:
Input: scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 24
Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3].
The score of the node sequence is 5 + 2 + 9 + 8 = 24.
It can be shown that no other node sequence has a score of more than 24.
Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

Example 2:
Input: scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]
Output: -1
Explanation: The figure above shows the graph.
There are no valid node sequences of length 4, so we return -1.
``` 

Constraints:

- n == scores.length
- 4 <= n <= 5 * 10^4
- 1 <= scores[i] <= 10^8
- 0 <= edges.length <= 5 * 10^4
- edges[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
- There are no duplicate edges.

Acceptance Rate
37.9%

<details>
<summary>Hint 1</summary>

For every node sequence of length 4, there are 3 relevant edges. How can we consider valid triplets of edges?

</details>
<details>
<summary>Hint 2</summary>

Fix the middle 2 nodes connected by an edge in the node sequence. Can you determine the other 2 nodes that will give the highest possible score?

</details>
<details>
<summary>Hint 3</summary>

The other 2 nodes must each be connected to one of the middle nodes. If we only consider nodes with the highest scores, how many should we store to ensure we don’t choose duplicate nodes?

</details>
<details>
<summary>Hint 4</summary>

For each node, we should store the 3 adjacent nodes with the highest scores to ensure we can find a sequence with no duplicate nodes via the method above.

</details>