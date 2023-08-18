# Intuition

see Example 3, all the cities do not have to be connected.
```
0-1-2-3
    |
    4
7
|
5-6
```
(city-2,city-5) pair has 5 network rank which means 5 edges connected to it

thus, we can calculate indegrees of each node and iterate two distinct node to see their sum of indegrees. also, use adjacency list to check if they share the same edge, then:

`rank = indegrees[a] + indegrees[b] - (1 if a and b are connected else 0)`

# Complexity
- Time complexity:

    $$O(n^2)$$

- Space complexity:

    $$O(n^2)$$
