class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count = Counter([0])

        res = presum = 0
        for i in range(n):
            presum = (presum+nums[i])%k
            res += count[presum]
            count[presum] += 1
        
        # dedup
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            
            L = j-i
            for length in range(1, L):
                if (length * nums[i]) % k == 0:
                    res -= L - length # the number of subarray with size = `length`

            i = j

        return res
