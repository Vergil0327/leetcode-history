# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
## DFS
travel from leaf node to node0, we can calcualte how many people in each traversal at post-order DFS position

each time we travel to next city, we needs `ceil(passengers/seats)` fuel, we accumulate it to the answer.

## BFS
actually, this is topological sort.
we can simulate the scenario from leaf node to capital.
at each city excluding capital(node=0), we can calculate the fuel we need and accumulate passengers to next city

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
