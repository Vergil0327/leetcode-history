class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mid = nums.index(k)

        # valid subarray must contains median k
        # just like two-sum
        # search left side first including mid (start from mid)
        # records how many count of currrent balance.
        balance = 0
        counter = defaultdict(int)
        for i in range(mid, -1, -1):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            counter[balance] += 1
        
        # search right side, calculate how many subarray if we can add left-side subarray to make balance 1 or 0
        total = 0
        balance = 0
        for i in range(mid, n):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            total += counter[-balance] + counter[1-balance]
            
        return total
