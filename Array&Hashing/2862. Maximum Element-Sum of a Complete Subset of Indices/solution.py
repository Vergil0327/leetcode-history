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
        
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        subset = defaultdict(int) # complete_subset_key: sum

        # 先把完全平方項去掉
        for i, num in enumerate(nums, start=1): # 1-indexed
            perfect_square = 2
            while i >= perfect_square**2:
                while i % (perfect_square**2) == 0:
                    i //= perfect_square**2
                perfect_square += 1
            subset[i] += num
        return max(subset.values())
