palindromic = []
for i in range(1, 10 ** 5 + 1):
    palindromic.append(int(str(i) + str(i)[::-1]))
    palindromic.append(int(str(i) + str(i)[:-1][::-1]))
palindromic.sort()

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]

        idx = bisect.bisect_left(palindromic, median)

        res = inf
        for i in range(max(0, idx-1), idx+2):
            x = palindromic[i]
            res = min(res, sum(abs(num-x) for num in nums))
        return res

