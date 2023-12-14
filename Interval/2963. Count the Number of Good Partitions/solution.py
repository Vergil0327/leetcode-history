class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        interval = defaultdict(lambda: [n, -1]) # interval[nums[i]] = [l, r], each element's leftmost and rightmost index
        for i in range(n):
            interval[nums[i]][0] = min(interval[nums[i]][0], i)
            interval[nums[i]][1] = max(interval[nums[i]][1], i)
            
        intervals = sorted(interval.values())
        
        nonoverlap = []
        for l, r in intervals:
            if not nonoverlap or l > nonoverlap[-1][1]:
                nonoverlap.append([l, r])
            else:
                nonoverlap[-1][1] = max(nonoverlap[-1][1], r)
        
        return pow(2, len(nonoverlap)-1, 10**9 +7)
