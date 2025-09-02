# Intuition

比較直覺的想法是透過Trie去找no common bits
但仍然TLE

```py

class TrieNode:
    def __init__(self):
            self.next = [None, None]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def dfs(node, i, x):
            if node is None: return -1
            if i >= 31: return 0

            b = (x>>(30-i))&1
            if b == 1:
                ans = dfs(node.next[0], i+1, x)
                if ans != -1:
                    return ans
                else:
                    return -1
            else:
                ans1 = dfs(node.next[1], i+1, x)
                if ans1 != -1:
                    return (1<<(30-i)) + ans1
                ans2 = dfs(node.next[0], i+1, x)
                if ans2 != -1:
                    return (0<<(30-i)) + ans2
                return -1

        root = TrieNode()
        res = 0
        for num in nums:
            node = root

            t = dfs(node, 0, num)
            if t != -1:
                 res = max(res, num * t)

            for i in range(31):
                b = ((num>>(30-i))&1)
                if node.next[b] is None:
                    node.next[b] = TrieNode()
                node = node.next[b]
                
        return res
```

dp[m]: the maximum element you can find from the array such that the element is a submask of m

那這樣遍歷nums[i]就能更新: res = max(res, nums[i] * dp[complementary(nums[i])])
因為complementary(nums[i])本身就跟nums[i]沒有common bits, 所以他的任何submask也不會有common bits, 而dp[complementary(nums[i])]為這些no-common bits裡的最大值
所以跟nums[i]相乘後, 可更新`res`