# 3-pass O(n)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        minLeft = list(range(n)) # store index j in minLeft[i] for nums[j] < nums[i]
        minimum = [nums[0], 0] # [value, index]
        for i in range(1, n):
            if minimum[0] < nums[i]:
                minLeft[i] = minimum[1]

            if nums[i] < minimum[0]:
                minimum[0] = nums[i]
                minimum[1] = i
        
        maxRight = list(range(n))
        maximum = [nums[n-1], n-1]
        for i in range(n-2, -1, -1):
            if maximum[0] > nums[i]:
                maxRight[i] = maximum[1]

            if nums[i] > maximum[0]:
                maximum[0] = nums[i]
                maximum[1] = i
        
        for i in range(1, n-1):
            if minLeft[i] < i and maxRight[i] > i:
                return True
        return False

# O(nlogn)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        tails = []
        for i in range(n):
            j = bisect.bisect_left(tails, nums[i])
            if j == len(tails):
                tails.append(nums[i])
            else:
                tails[j] = nums[i]
            if len(tails) == 3: return True
        return False

# Optimal O(n) Solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float("inf")
        for num in nums:
            # only one of the if statements gets executed with elif or else
            if i >= num: # only gets updated if left side of i
                i = num
            elif j > num: # only gets update if not left side of i and left side of j
                j = num
            elif num > i and num > j:
                return True
        return False