class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = 0
        count = Counter()

        for r in range(4, n-2):
            q = r-2
            for p in range(q-1):
                GCD = gcd(nums[p], nums[q])
                ratio = (nums[p]//GCD, nums[q]//GCD)
                count[ratio] += 1
            
            for s in range(r+2, n):
                GCD = gcd(nums[s], nums[r])
                ratio = (nums[s]//GCD, nums[r]//GCD)
                res += count[ratio]
        return res