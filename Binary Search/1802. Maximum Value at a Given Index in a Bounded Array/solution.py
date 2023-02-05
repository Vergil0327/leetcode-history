# nums[i]: [0, n)
# max possible nums[i]: maxSum
# nums[index] is max value
# we can try to greedily generate nums
# since abs(nums[i]-nums[i+1]) <= 1
# => nums[i]-1 <= nums[i+1] <= nums[i]+1
# => nums[i]-1 <= nums[i-1] <= nums[i]+1
# we can start from `index` to left, decrement nums[i] by 1
# and start from `index` to right, decrement nums[i] by 1
# and nums[i] must be 1 at least
# thus, nums = [1,1, ..., 1,2,3, ... , maxVal, ..., 3,2,1, ..., 1,1,1]
# => use sum(left ones) + (1+maxVal)*n//2 (left portion) + (1+maxVal)*m//2 (right portion) + sum(right ones) - duplicate maxVal
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # TLE check
        # def check(maxVal):
        #     nums = [0] * n
        #     nums[index] = maxVal
        #     left = maxSum - maxVal

        #     # abs(nums[i]-nums[i+1]) <= 1
        #     # -1 <= nums[i]-nums[i+1] <= 1
        #     # nums[i]-1 <= nums[i+1] <= nums[i]+1
        #     for i in range(index, n-1):
        #         nums[i+1] = max(nums[i]-1, 1)
        #         left -= nums[i+1]
        #         if left < 0: return False
            
        #     # nums[i+1]-1 <= nums[i] <= nums[i+1]+1
        #     for i in range(index, 0, -1):
        #         nums[i-1] = max(nums[i]-1, 1)
        #         left -= nums[i-1]
        #         if left < 0: return False
        #     return True

        def check(maxVal):
            # sum[:index+1] + sum[index:]
            # index = 1, nums = [2,3,2,1,1,1,1]
            #            index   0 1 2 3 4
            l = max(maxVal-index, 1) # must positive integer
            leftSum = (maxVal + l) * (maxVal-l+1) // 2
            
            # nums[i] must be 1 at least. [1,1, ..., 1,2,3,4, ... , maxVal, ..., 3,2,1, ..., 1,1,1]
            leftSum += index - (maxVal-l) # left ones

            r = max(maxVal-(n-1-index), 1) # must positive integer
            rightSum = (maxVal + r) * (maxVal-r+1) // 2
            
            # nums[i] must be 1 at least. [1,1, ..., 1,2,3,4, ... , maxVal, ..., 3,2,1, ..., 1,1,1]
            rightSum += n-1-(index+maxVal-r) # right ones

            return (leftSum + rightSum - maxVal) <= maxSum

        l, r = 0, maxSum
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l
