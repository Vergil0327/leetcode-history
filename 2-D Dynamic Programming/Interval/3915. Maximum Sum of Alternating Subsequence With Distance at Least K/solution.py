"""
This problem is a classic Dynamic Programming + Segment Tree optimization challenge.
The $10^5$ constraints on both $n$ and the values in $nums$ mean an $O(n^2)$ DP will TLE, so we need a data structure to speed up the transitions.

1. The DP StateWe want to pick numbers at least $k$ distance apart that alternate.Let:

- dp[i][0] = Max score of a subsequence ending at index $i$, where the next number must be smaller (the current number is a "peak").
- dp[i][1] = Max score of a subsequence ending at index $i$, where the next number must be larger (the current number is a "valley").

2. The Transitions

For any index $i$, we look for a valid previous index $j$ such that $j \le i - k$:

- To make $i$ a peak: $nums[i] > nums[j]$. We transition from a state where $j$ was a valley:
    
    $$dp[i][0] = \max(nums[i], \max_{j \le i-k, nums[j] < nums[i]} \{dp[j][1]\} + nums[i])$$

- To make $i$ a valley: $nums[i] < nums[j]$. We transition from a state where $j$ was a peak:
    
    $$dp[i][1] = \max(nums[i], \max_{j \le i-k, nums[j] > nums[i]} \{dp[j][0]\} + nums[i])$$

3. Optimization with Segment Trees

The $j \le i - k$ constraint is a "sliding window" of valid indices. As we iterate $i$ from $0$ to $n-1$, we can maintain a Segment Tree that stores the DP values based on the value of $nums[j]$.

1. When we are at index $i$, the "available" indices are those $\le i - k$.
2. We add the DP results of index $i - k$ into two Segment Trees:

    - Tree 0: Stores dp[j][0] at position nums[j].
    - Tree 1: Stores dp[j][1] at position nums[j].
    
3 To calculate $dp[i][0]$, we query Tree 1 for the range $[1, nums[i]-1]$ to find the max $dp[j][1]$.
4. To calculate $dp[i][1]$, we query Tree 0 for the range $[nums[i]+1, \max(nums)]$ to find the max $dp[j][0]$.
"""        

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [-float('inf')] * (2 * self.n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = max(self.tree[i], val)
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        res = -float('inf')
        if l > r: return res
        l += self.n
        r += self.n
        while l <= r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0: return 0
        
        max_val = max(nums)
        # Tree 0 stores max scores ending in a PEAK (next should be smaller)
        tree0 = SegmentTree(max_val + 1)
        # Tree 1 stores max scores ending in a VALLEY (next should be larger)
        tree1 = SegmentTree(max_val + 1)
        
        dp = [[0, 0] for _ in range(n)]
        ans = 0
        
        for i in range(n):
            # Add the index that just became valid (i - k) into the trees
            if i >= k:
                prev_idx = i - k
                tree0.update(nums[prev_idx], dp[prev_idx][0])
                tree1.update(nums[prev_idx], dp[prev_idx][1])
            
            # Current nums[i] as a PEAK: needs a previous VALLEY smaller than nums[i]
            prev_valley_max = tree1.query(1, nums[i] - 1)
            dp[i][0] = max(nums[i], prev_valley_max + nums[i])
            
            # Current nums[i] as a VALLEY: needs a previous PEAK larger than nums[i]
            prev_peak_max = tree0.query(nums[i] + 1, max_val)
            dp[i][1] = max(nums[i], prev_peak_max + nums[i])
            
            ans = max(ans, dp[i][0], dp[i][1])
            
        return ans