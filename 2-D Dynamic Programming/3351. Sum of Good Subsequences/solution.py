class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        count = defaultdict(int)
        total = defaultdict(int)
        
        for i in range(len(nums)):
            count[nums[i]] += count[nums[i]-1] + count[nums[i]+1] + 1
            count[nums[i]] %= mod

            # total[nums[i]] += (total[nums[i]-1] + nums[i] * count[nums[i]-1] + 
            #                    total[nums[i]+1] + nums[i] * count[nums[i]+1] + 
            #                    nums[i])

            total[nums[i]] += total[nums[i]-1] + total[nums[i]+1] + nums[i] * (count[nums[i]-1] + count[nums[i]+1] + 1)
            total[nums[i]] %= mod
        return sum(total.values()) % mod