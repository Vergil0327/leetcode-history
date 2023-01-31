# with sorting
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkArithmetic(nums):
            nums.sort()
            diff = nums[1] - nums[0]
            for i in range(2, len(nums)):
                if nums[i] - nums[i-1] != diff: return False
            return True

        res = [False]*len(l)
        for i in range(len(l)):
            left, right = l[i], r[i]
            res[i] = checkArithmetic(nums[left:right+1])

        return res

# without sorting, using hashset
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkArithmetic(nums):
            n = len(nums)
            MAX, MIN = max(nums), min(nums)
            SET = set(nums)
            diff = (MAX-MIN)//(n-1)
            if diff == 0:
                return MIN == MAX
            else:
                for num in range(MIN, MAX+1, diff):
                    if num not in SET: return False
                return True

        res = [False]*len(l)
        for i in range(len(l)):
            left, right = l[i], r[i]
            res[i] = checkArithmetic(nums[left:right+1])

        return res