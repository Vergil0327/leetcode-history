# Intuition

we can use post-order DFS to calculate difference of every left and right path cost.

the minimum operations we need are `abs(left-right)` because we want to increment lower path sum until left path equals right path.

then, the left and right path should be equal to each other, i.e. ` max(left, right)`, and current path becomes `cost[node] + max(left, right)`

**base case**

define the depth of leaf node is `h`, we can know that `h = floor(log2(n))` by math.

once we reach leaf node, we return its cost directly.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(log2(n))$$

<details>
<summary>Hint 1</summary>

The path from the root to a leaf that has the maximum cost should not be modified.

</details>

<details>
<summary>Hint 2</summary>

The optimal way is to increase all other paths to make their costs equal to the path with maximum cost.

</details>

# Other Solution

we can focus on `cost` array and use `2*i+1` and `2*i+2` to find left & right child node's cost

```py
class Solution:
    def minIncrements(self, n, cost):
        self.res = 0
        def dfs(node):
            if node >= len(cost): return 0
            a, b = dfs(2 * node + 1), dfs(2 * node + 2)
            self.res += abs(a - b)
            return cost[node] + max(a, b)
        dfs(0)
        return self.res
```