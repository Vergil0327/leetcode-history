# time: O(n)
# space: O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        res = [-1] * 2
        for num in range(1, n+1):
            if counter[num] == 0:
                res[1] = num
            if counter[num] == 2:
                res[0] = num
        return res

# time: O(n)
# space: O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = -1
        # use value as index, mapping [1..n]value to [0..n-1]index
        # [1,2,2,4]
        # [-1,2,2,4]
        # [-1,-2,2,4]
        # [-1,-2,2,4] found dup = abs(-2) because duplicate value means we'll visit index twice
        # [-1,-2,-2,4] missing number means we'll never visit that index
        for i in range(n):
            idx = abs(nums[i])-1
            if nums[idx] < 0:
                dup = abs(nums[i])
            else:
                nums[idx] *= -1
        
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i+1 # mapping index to element
        return [dup, missing]
