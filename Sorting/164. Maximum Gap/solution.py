class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # and we got n-1 gaps.
        # turn these gaps into bucket to sort nums with bucket size equals (max-min)//gaps
        n, lo, hi = len(nums), min(nums), max(nums)
        if n <= 2 or lo == hi: return hi-lo

        buckets = [[inf, -inf] for _ in range(n-1)]
        bucketSize = ceil((hi-lo) / (n-1))
        for num in nums:
            if num == hi:
                buckets[-1][0] = min(buckets[-1][0], num)
                buckets[-1][1] = max(buckets[-1][1], num)
            else:
                idx = (num-lo) // bucketSize
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        buckets = [bucket for bucket in buckets if bucket[0] != inf]
        diff = 0
        for prev, nxt in zip(buckets, buckets[1:]):
            diff = max(diff, nxt[0]-prev[1])
        
        return diff
