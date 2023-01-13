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

see:
```java
class Solution {
    private int longestPath = 1;

    public int dfs(int currentNode, Map<Integer, List<Integer>> children, String s) {
        // If the node is the only child, return 1 for the currentNode itself.
        if (!children.containsKey(currentNode)) {
            return 1;
        }

        // Longest and second longest path starting from currentNode (does not count the
        // currentNode itself).
        int longestChain = 0, secondLongestChain = 0;
        for (int child : children.get(currentNode)) {
            // Get the number of nodes in the longest chain starting from the child,
            // including the child.
            int longestChainStartingFromChild = dfs(child, children, s);
            // We won't move to the child if it has the same character as the currentNode.
            if (s.charAt(currentNode) == s.charAt(child)) {
                continue;
            }
            // Modify the longestChain and secondLongestChain if longestChainStartingFromChild
            // is bigger.
            if (longestChainStartingFromChild > longestChain) {
                secondLongestChain = longestChain;
                longestChain = longestChainStartingFromChild;
            } else if (longestChainStartingFromChild > secondLongestChain) {
                secondLongestChain = longestChainStartingFromChild;
            }
        }

        // Add "1" for the node itself.
        longestPath = Math.max(longestPath, longestChain + secondLongestChain + 1);
        return longestChain + 1;
    }

    public int longestPath(int[] parent, String s) {
        int n = parent.length;
        Map<Integer, List<Integer>> children = new HashMap<>();
        // Start from node 1, since root node 0 does not have a parent.
        for (int i = 1; i < n; i++) {
            children.computeIfAbsent(parent[i], value -> new ArrayList<Integer>()).add(i);
        }

        dfs(0, children, s);

        return longestPath;
    }
}
```

- space complexity

$$O(n)$$

## Summary

Just like [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) but allow more than 2 child nodes.

two things to do:
1. do DFS to find longest **valid** no-split path from root to leaf nodes.
        - `valid` means **NO** pair of adjacent nodes has the same character
2. find longest subpath if we try to split at each node
