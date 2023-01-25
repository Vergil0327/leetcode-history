# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
first, find every node `i` which can be reached by node1 and node2
then, we compare distance from node1 to `i` and node2 to `i`

1. use DFS to explore how far **node1** and **node2** can reach and store distance to every node `i` in **dist1[i]** and **dist2[i]** array

2. iterate from `0` to `n-1` to find intersection `i` which both node1 and node2 can reach and the  distance from node1 to `i` and node2 to `i` is MinMax

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

