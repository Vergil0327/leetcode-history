[1782. Count Pairs Of Nodes](https://leetcode.com/problems/count-pairs-of-nodes/)

`Hard`

You are given an undirected graph defined by an integer n, the number of nodes, and a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

Let incident(a, b) be defined as the number of edges that are connected to either node a or b.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy both of the following conditions:

a < b
incident(a, b) > queries[j]
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

Note that there can be multiple edges between the same two nodes.

```
Example 1:
Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The calculations for incident(a, b) are shown in the table above.
The answers for each of the queries are as follows:
- answers[0] = 6. All the pairs have an incident(a, b) value greater than 2.
- answers[1] = 5. All the pairs except (3, 4) have an incident(a, b) value greater than 3.

Example 2:
Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
Output: [10,10,9,8,6]
``` 

Constraints:

- 2 <= n <= 2 * 10^4
- 1 <= edges.length <= 10^5
- 1 <= ui, vi <= n
- ui != vi
- 1 <= queries.length <= 20
- 0 <= queries[j] < edges.length

Accepted
6.6K
Submissions
16.5K
Acceptance Rate
39.8%

<details>
<summary>Hint 1</summary>

We want to count pairs (x,y) such that degree[x] + degree[y] - occurrences(x,y) > k

</details>
<details>
<summary>Hint 2</summary>

Think about iterating on x, and counting the number of valid y to pair with x.

</details>
<details>
<summary>Hint 3</summary>

You can consider at first that the (- occurrences(x,y)) isn't there, or it is 0 at first for all y. Count the valid y this way.

</details>
<details>
<summary>Hint 4</summary>

Then you can iterate on the neighbors of x, let that neighbor be y, and update occurrences(x,y).

</details>
<details>
<summary>Hint 5</summary>

When you update occurrences(x,y), the left-hand side decreases. Once it reaches k, then y is not valid for x anymore, so you should decrease the answer by 1.

</details>