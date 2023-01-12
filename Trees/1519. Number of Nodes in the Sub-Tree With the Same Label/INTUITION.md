# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use post-order DFS from bottom to top to gather each subtree's information

we can use a `visited` hashset or keep tracking `parent` which is previous node to do DFS

# Complexity
- Time complexity:
$$O(V+26E)$$ = $$O(n)$$

- Space complexity:
$$O(n)$$

# Code
```
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        res = [0] * n
        def dfs(node, parent):
            curr = [0] * 26
            curr[ord(labels[node])-ord("a")] = 1

            for nei in G[node]:
                if nei == parent: continue
                counter = dfs(nei, node)
                for i in range(26):
                    curr[i] += counter[i]

            res[node] = curr[ord(labels[node])-ord("a")]
            return curr

        dfs(0, -1)
        return res
```