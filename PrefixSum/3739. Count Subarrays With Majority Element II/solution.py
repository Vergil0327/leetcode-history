from collections import Counter
from itertools import accumulate
from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Map to +1 if equals target, else -1
        arr = [1 if x == target else -1 for x in nums]
        
        # Prefix sums, with pref[0] = 0
        presum = list(accumulate(arr, initial=0))

        # Coordinate compression
        vals = sorted(set(presum))
        idx = {v: i for i, v in enumerate(vals, start=1)}  # 1-based

        # Fenwick Tree
        size = len(vals)
        bit = [0] * (size + 2)

        def update(i: int, delta: int) -> None:
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(i: int) -> int:
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        # Count pairs with pref[j] > pref[i]
        res = 0
        for cnt in presum:
            pos = idx[cnt]
            res += query(pos - 1)
            update(pos, 1)

        return res
    
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        A subarray has target as majority
        if its balance increase is positive,
        meaning target appears more than half.

        count[x] stores how many prefixes have balance x.
        acc[x] is the prefix sum of count.

        Each step adds acc[pre - 1] to
        count all earlier prefixes with smaller balance
        these correspond to valid subarrays where target dominates.

        acc[i] means the number of times the prefix sum <= i has occurred.
        There is an offset of n+1 used in the algorithm to map index with prefix sum, which works fine even if the prefix sum goes negative.
        """
        n = len(nums)
        arr = [1 if x == target else -1 for x in nums]

        count = Counter()
        count[0] = 1

        acc = [1] + [0] * (n + n + 2)
        res = presum = 0
        for num in arr:
            presum += num
            count[presum] += 1
            acc[presum] = acc[presum - 1] + count[presum]
            res += acc[presum - 1]
        return res
