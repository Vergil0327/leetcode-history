# Intuition
I think the longer the path is, the greather the path sum is.
find all the leaf nodes and use DFS to calculate path sum.

since lots of path sum will be calculated multiple times, we can cache it to reduce time complexity

# Complexity
- Time complexity:
$$O(n)$$
each node only calculate one time and it'll be cached

- Space complexity:
$$O(n)$$

# Code
```
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        leaves = [node for node, deg in enumerate(indegree) if deg == 1]

        
        cache = {}
        def dfs(node, prev):
            if (node, prev) in cache:
                return cache[(node, prev)]

            pathsum = 0
            for nei in graph[node]:
                if nei == prev: continue
                pathsum = max(pathsum, dfs(nei, node))

            cache[(node, prev)] = pathsum + price[node]
            return cache[(node, prev)]
        
        res = 0
        for node in leaves:
            res = max(res, dfs(node, node) - price[node])
        return res
```

# Other Solution - Re-root

[original post](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/solutions/3052596/re-rooting/)

這題也能利用re-root來解

首先最小的path sum 就是根節點本身
因此要求的maximum difference path sum就是子樹的path sum

首先我們先從任意節點，例如`0`，求得所有子節點的path sum
再來對於當前節點的子節點來說，他的maximum difference path sum就可能來自兩個地方：

1. 子節點的最大path sum是他的父節點那條，前一個遞歸的計算結果(parentContribution)
2. 所有子節點裡最大的path sum

所以最大的`maxDiff = max(maxDiff, max(max(child_path_sum), parentContribution))`

然後我們再繼續reroot到其他子節點
1. 如果移到的下個子節點是我們剛剛算出來的最大子節點，那麼reroot後的parentContribution就是從原本父節點的path sum 與其餘子節點中次大的path sum中挑最大的，`max(parentContribution, secondContribution)`，也就是reroot後的反方向maximum path sum
2. 如果reroot的下個節點不是最長path sum的子節點，那麼reroot後的父節點貢獻的最長path sum就是`max(parentContribution, maxContribution)`，原本父節點貢獻的path sum跟最大子節點path sum取最大

