# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
1. use post-order DFS to mark path we don't need to continue. if this path doesn't contribute any apples, mark it `canSkip`.
2. measure time. increment time at pre-order and post-order position. skip every node marked with `canSkip`

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# One Pass Concise Solution

## Code

```py
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not any(hasApple): return 0
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, parent):
            time = 0
            for child in graph[node]:
                if child != parent:
                    time += dfs(child, node)
            
            # means there is no apple from child to current node (post-order)
            if not time and not hasApple[node]:
                return 0

            return time + 2 # pre-order + post-order
        
        return dfs(0, 0) - 2 # -2 for root node
```