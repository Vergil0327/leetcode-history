class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        nums.sort()
        
        power2 = [1] * (n+1)
        for i in range(1, n+1):
            power2[i] = power2[i-1]*2%MOD


        cnt = 0
        r = n-1
        for l in range(n):
            while r >= l and nums[r] + nums[l] > target:
                r -= 1
            if r < l: break
            # MIN [X X X X X X X X X MAX]
            # l                       r   -> we can pick or not to pick nums[i] where i from l+1 to r
            #                             -> cnt += 2 ** (r-l)
            # cnt += pow(2, r-l, MOD)
            cnt += power2[r-l]
            cnt %= MOD
        return cnt