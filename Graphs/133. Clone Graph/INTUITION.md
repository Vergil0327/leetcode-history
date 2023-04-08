# Intuition
use DFS + memorization.

each time we traverse a new node, we clone it and memorize it in hashmap.

since node.val is unique, we can safely use node.val as key.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Code
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone = {}
        def dfs(node):
            if not node: return None
            if node.val in clone: return clone[node.val]

            clone[node.val] = Node(node.val)
            for nei in node.neighbors:
                clone[node.val].neighbors.append(dfs(nei))
            return clone[node.val]
        return dfs(node)
```