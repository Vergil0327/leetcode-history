class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        # leftMax[i]: max sum of subarray with length k in nums[0:i]
        leftMax = [0] * n
        leftIdx = [0] * n # idx of subarray with max sum
        currMax = 0
        currMaxIdx = 0
        for i in range(n):
            subSum = presum[i+1]-presum[max(0, i-k+1)]
            if subSum > currMax:
                currMax = subSum
                currMaxIdx = max(0, i-k+1)
            leftMax[i] = currMax
            leftIdx[i] = currMaxIdx

        # rightMax[i]: max sum of subarray with length k in nums[i:n]
        rightMax = [0] * n
        rightIdx = [0] * n # idx of subarray with max sum
        currMax = 0
        currMaxIdx = 0
        for i in range(n-1, -1, -1):
            subSum = presum[min(n, i+k)]-presum[i]
            if subSum >= currMax:
                currMax = subSum
                currMaxIdx = i
            rightMax[i] = currMax
            rightIdx[i] = currMaxIdx

        MAX = 0
        res = [-1, -1, -1]
        for i in range(k, n-2*k+1): # valid range is important!!! {至少k個}{iterate [i:i+k]}{至少k個}
            curr = presum[i+k]-presum[i]
            currMax = leftMax[i-1] + curr + rightMax[i+k]

            if currMax > MAX:
                MAX = currMax
                res[0] = leftIdx[i-1]
                res[1] = i
                res[2] = rightIdx[i+k]
        return res
