class Solution:
    def lastRemaining(self, n: int) -> int:
        i = 1
        steps = 1
        startFromLeft = True
        while n > 1:
            if startFromLeft:
                i = i+steps
            else:
                if n&1==0: # total number of remaining nums is even
                    i = i
                else:      # total number of remaining nums is odd
                    i = i+steps
            startFromLeft = not startFromLeft
            steps *= 2
            n //= 2
        return i

# Brute Force: Memory Limit Exceeded
class Solution:
    def lastRemaining(self, n: int) -> int:
        nums = list(range(1, n+1))
        steps = 1
        isOdd = True
        while len(nums) > 1:
            if isOdd:
                tmp = [num for i, num in enumerate(nums) if i%2==1]
                nums = tmp
                isOdd = not isOdd
            else:
                res = []
                n = len(nums)
                if n&1==0:
                    for i in range(len(nums)):
                        if i&1==0:
                            res.append(nums[i])
                else:
                    for i in range(1, len(nums)):
                        if i&1:
                            res.append(nums[i])

                nums = res
                isOdd = not isOdd
        return nums[0]