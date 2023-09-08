class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        count = defaultdict(int)
        
        for i in range(n):
            for j in range(n):
                count[nums[i]&nums[j]] += 1

        res = 0
        for num in nums:
            for pair, cnt in count.items():
                if num&pair == 0:
                    res += cnt
        return res