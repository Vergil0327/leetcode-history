# Path Sum

## Intuition

this is just like [leetcode 124. Binary Tree Maximum Path Sum](../124.%20Binary%20Tree%20Maximum%20Path%20Sum/)

core concept is the same, we can see below:
```
class Leetcode124:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0, -inf

            left, left_max_path_sum = dfs(root.left)
            right, right_max_path_sum = dfs(root.right)
            curr_max_path_sum = root.val + max(0, left) + max(0, right)
            maxSum = max(left_max_path_sum, right_max_path_sum, curr_max_path_sum)

            return root.val + max(left, right, 0), maxSum

        _, maxSum = dfs(root)
        return maxSum
```

we need to maintain each child's longest path sum.

then, while we do DFS, we can compute path sum when current node is turning point of path combined with first two largest child path sum.

```
pathLens.sort(reverse=True)
longest = max(longest, sum(pathLens[:2])+1) # choose first two largest to build longest path
```

also consider these condition:
1. since tree can have multiple children, we need to iterate through. thus, we need a `children` array and it can get by `parent` array

```
n = len(parent)
children = [[] for _ in range(n)]
for i in range(n):
    if parent[i] != -1:
        children[parent[i]].append(i)
```

2. adjacent node can't have the same character, we only can choose those nodes who differ with character as possible longest path

```
pathLens = []
for child in children[node]:
    pathLen = dfs(child)
    if s[child] != s[node]:
        pathLens.append(pathLen)
```

3. base case, if node without children, length equals 1 (itself)

```
def dfs():
    if not children[node]: return 1
```

## Complexity

- time complexity

$$O(V+E)$$ = $$O(n+nlogn)$$

we can reduce to $$O(n)$$ by keeping first 2 maximum path

see down below


- space complexity

$$O(n)$$

## Summary

Just like [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) but allow more than 2 child nodes.

two things to do:
1. do DFS to find longest **valid** no-split path from root to leaf nodes.
        - `valid` means **NO** pair of adjacent nodes has the same character
2. find longest subpath if we try to split at each node

## O(n) Optimized Solution

```python
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if not parent: return 0

        child = [[] for _ in range(len(parent))]
        for node, p in enumerate(parent):
            if p == -1: continue
            child[p].append(node)
    
        res = 1
        def dfs(node, prev):
            nonlocal res

            # path = []
            maxChild1, maxChild2 = 0, 0
            for ch in child[node]:
                if ch == prev: continue
                childPath = dfs(ch, node)
                if s[ch] != s[node]:
                    if childPath > maxChild1:
                        maxChild1, maxChild2 = childPath, maxChild1
                    elif childPath > maxChild2:
                        maxChild2 = childPath
                    # path.append(childPath)
            
            # path.sort(reverse=True)
            curMax = 1 + maxChild1
            subPath = 1 + maxChild1 + maxChild2
            res = max(res, curMax, subPath)
            return curMax
            # if not path:
            #     return 1
            # elif len(path) == 1:
            #     curMax = 1 + path[0]
            #     res = max(res, curMax)
            #     return curMax
            # else:
            #     curMax = 1 + maxChild1
            #     subPath = 1 + path[0] + path[1]
            #     res = max(res, curMax, subPath)
            #     return curMax
            
        dfs(0, 0)
        return res
```
