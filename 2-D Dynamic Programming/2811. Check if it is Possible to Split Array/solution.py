class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n == 1: return True

        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)

        @cache
        def dfs(l, r):
            if l >= r: return 0
            if r-l+1 == 2: return 1
            res = 0
            for i in range(l, r):
                sumA = presum[i+1]-presum[l]
                sumB = presum[r+1]-presum[i+1]
                if ((sumA >= m or i-l+1 == 1) and (sumB >= m or r-i == 1)):
                    res = max(res, dfs(l, i) + dfs(i+1, r)+1)
            
            return res
        
        return dfs(0, n-1) >= n-1
