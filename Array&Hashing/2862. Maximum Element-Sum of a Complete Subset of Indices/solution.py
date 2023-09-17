class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        for i, num in enumerate(nums, start=1):
            for p in range(2, int(sqrt(i))+1):
                square = p*p
                while i%square == 0:
                    i //= square
            count[i] += num
            res = max(res, count[i])
            
        return res
        