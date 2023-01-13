# Intuition

we can use **Topological Sort* to know the relation of prerequisite.

use `Hashset` to store each node's prerequisite, and union them while topological sorting

answer with each node's `Hashset`

# Complexity

- time complexity
$$O(V + E*N)$$ because of union

- space complexity
$$O(n^2)$$ for isPrerequisite

# Other Solution - Floyd-Warshall Algorithm

[Floyd–Warshall Algorithm](https://leetcode.com/problems/course-schedule-iv/solutions/660509/java-python-floyd-warshall-algorithm-clean-code-o-n-3/)

## Code

```python
connected = [[False] * numCourses for _ in range(numCourses)]

for u, v in prerequisites:
    connected[u][v] = True

for k in range(n):
    for u in range(n):
        for v in range(n):
            connected[u][v] = connected[u][v] or (connected[u][k] and connected[k][v])
return [connected[u][v] for u, v in queries]
```