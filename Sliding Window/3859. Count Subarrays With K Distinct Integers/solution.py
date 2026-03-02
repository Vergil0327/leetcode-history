from collections import defaultdict
class Solution:
    """
    The core realization is that for a fixed right endpoint, the valid left endpoints form a contiguous range $[l1, l2)$.
    
    - Lower Bound ($l1$): Standard sliding window to find the leftmost index such that the window [l1, current] has at most $k$ distinct elements.
    - Upper Bound ($l2$): A second pointer that moves forward as long as the window [l2, current] contains at least $k$ elements that each appear $\ge m$ times.
    
    - The Magic Gap:
        - If satisfy == k, then every subarray starting from $l1$ up to $l2-1$ is guaranteed to have exactly $k$ distinct elements (because $l1$ keeps it $\le k$ and $l2$ ensures there are at least $k$ "satisfied" ones).
        - Furthermore, because $l2$ only stops when we drop below $k$ satisfied elements, every $left$ in the range $[l1, l2)$ satisfies the "each distinct element appears $\ge m$ times" condition.
        
    - Count: The number of valid subarrays ending at current is simply the width of that gap: l2 - l1.
    
    Why this is more efficient
    Instead of checking "at most $k$" vs "at most $k-1$", this approach directly bounds the validity of the $m$ condition against the distinct element constraint. It works because the "satisfied" count (elements with count $\ge m$) effectively acts as a proxy for both the distinct count and the frequency requirement simultaneously.
    """

    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        res = 0
        l1 = l2 = satisfy = 0
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        
        for curr in nums:
            count1[curr] += 1
            while len(count1) > k:
                count1[nums[l1]] -= 1
                if count1[nums[l1]] == 0:
                    del count1[nums[l1]]
                l1 += 1
                
            count2[curr] += 1
            if count2[curr] == m:
                satisfy += 1
            while satisfy >= k:
                if count2[nums[l2]] == m:
                    satisfy -= 1
                count2[nums[l2]] -= 1
                l2 += 1
                
            if l2 > l1:
                res += (l2 - l1)
        return res