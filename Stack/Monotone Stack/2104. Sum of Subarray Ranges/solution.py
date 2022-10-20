# Optimized: https://leetcode.com/problems/sum-of-subarray-ranges/discuss/1624222/JavaC%2B%2BPython-O(n)-solution-detailed-explanation
# actually, we can find next and prev in one pass monotonic stack checking
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:        
        # monotonically increasing stack to find prevSmaller & nextSmaller
        # since we only calculate res in while loop (in pop action),
        # add -inf as border to make sure every num in stack will be popped and calculate its subarray sum
        res = 0
        
        numsNegInf = [float("-inf")] + nums + [float("-inf")]
        stk = []
        for i in range(len(numsNegInf)):
            while stk and numsNegInf[stk[-1]] > numsNegInf[i]:
                index = stk.pop()
                l, r = stk[-1], i
                res -= (index-l)*(r-index)*numsNegInf[index]
            stk.append(i)
        
        # monotonically increasing stack to find prevGreater & nextGreater
        # since we only calculate res in while loop (in pop action),
        # add inf as border to make sure every num in stack will be popped and calculate its subarray sum
        numsInf = [float("inf")] + nums + [float("inf")]
        stk.clear()
        for i in range(len(numsInf)):
            while stk and numsInf[stk[-1]] < numsInf[i]:
                index = stk.pop()
                l, r = stk[-1], i
                res += (index-l)*(r-index)*numsInf[index]
            stk.append(i)
        
        return res

# Monotonic Stack Solution: O(n)
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        
        nextSmallerOrEq = [N for i in range(N)]
        
        stack = []
        for i in range(N):
            while stack and nums[stack[-1]] >= nums[i]:
                index = stack.pop()
                nextSmallerOrEq[index] = i
            stack.append(i)
        
        prevSmaller = [-1 for i in range(N)]
        
        stack.clear()
        for i in range(N-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                prevSmaller[index] = i
            stack.append(i)
        
        nextGreaterOrEq = [N for i in range(N)]
        
        stack.clear()
        for i in range(N):
            while stack and nums[stack[-1]] <= nums[i]:
                index = stack.pop()
                nextGreaterOrEq[index] = i
            stack.append(i)
        
        prevGreater = [-1 for i in range(N)]
        
        stack.clear()
        for i in range(N-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                prevGreater[index] = i
            stack.append(i)

        total = 0
        for i in range(N):
            total += (i-prevGreater[i])*(nextGreaterOrEq[i]-i)*nums[i]
            total -= (i-prevSmaller[i])*(nextSmallerOrEq[i]-i)*nums[i]

        return total
        

# O(n^2)
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            maxVal, minVal = float("-inf"), float("inf")
            for j in range(i, len(nums)):
                maxVal = max(maxVal, nums[j])
                minVal = min(minVal, nums[j])
                total += maxVal-minVal
        return total
                