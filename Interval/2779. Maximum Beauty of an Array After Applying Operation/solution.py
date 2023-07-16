class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        interval = []
        for num in nums:
            interval.append([num-k, num+k])
        interval.sort(key=lambda x:x[1])
        
        res = 1
        n = len(interval)
        j = 1
        for i in range(n):
            while j < n and interval[j][0] <= interval[i][1]:
                j += 1
                
            res = max(res, j-i)
        return res