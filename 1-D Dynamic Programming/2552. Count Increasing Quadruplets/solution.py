# O(n^2) TLE for python
# i < j < k < l，以中間當作突破口，找出合法j < k 使得 nums[k] < nums[j]
# 然後再看有多少個數，值小於 nums[k]且index < j => 可以提前處理:prefixSum[index][smaller than value]
# 和多少個數，值大於nuims[j]且index > k        => 可以提前處理:suffuxSum[index][greater than value]
# 兩邊個數相乘即得固定j, k的i, j, k, l quadruplets個數
# Explanation: https://www.youtube.com/watch?v=Blv7IQK-zkU
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)

        # prefix sum
        smaller = [[0] * (n+1) for _ in range(n)] # smaller[idx][value], 0 <= value = nums[i] <= n
        for j in range(n):
            for v in range(n+1):
                smaller[j][v] = smaller[j-1][v] if j-1>=0 else 0
                smaller[j][v] += (1 if nums[j] < v else 0)

        # suffix sum
        greater = [[0] * (n+1) for _ in range(n)]
        for k in range(n-1, -1, -1):
            for v in range(n+1):
                greater[k][v] = greater[k+1][v] if k+1<n else 0
                greater[k][v] += (1 if nums[k] > v else 0)

        res = 0
        for j in range(n):
            for k in range(j+1, n):
                if nums[k] < nums[j]:
                    res += smaller[j][nums[k]] * greater[k][nums[j]]
        return res
