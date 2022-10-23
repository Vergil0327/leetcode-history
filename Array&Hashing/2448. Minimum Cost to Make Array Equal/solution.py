# https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734183/Python3-Weighted-Median-O(NlogN)-with-Explanations
# find weighted median
# [13,23,54] [10,3,4] => unweighted: [13,13,13,13,13,13,13,13,13,13,23,23,23,54,54,54,54]
# where the weight is the number of times that a given data appears. Now, you have 17 data. The weighted median is the value in 9th position, that is, 13.
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        order = sorted(range(len(nums)), key=lambda i: nums[i])
        arr = [(nums[i], cost[i]) for i in order] # [(num, cost)]
        
        totalWeight = sum(cost)
        targetWeightMedian = totalWeight // 2
        weight = 0
        weightedMedian = 0
        for num, wei in arr:
            weight += wei
            # if len is odd, only one median
            # if len is even, we'll get two median(lower median and upper median),
            # and the result of moving element is the same for choosing either of them
            if weight > targetWeightMedian:
                weightedMedian = num
                break
        return sum(abs(weightedMedian-num)*weight for num, weight in arr)

# https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734162/JavaC%2B%2BPython-Binary-Search
# Ternary Search
# Assume the target value is x
# the total cost function y = f(x) is a convex function
# on the range of [min(A), max(A)].

# To find the minimum value of f(x),
# we can binary search x by comparing f(mid) and f(mid + 1).

# If f(mid) <= f(mid + 1),
# the minimum f(x) is on the left of mid,
# where x <= mid

# If f(mid) >= f(mid + 1),
# the minimum f(x) is on the right of mid + 1,
# where x >= mid.

# just like finding peak element in asscending array
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = [(num, cst) for num, cst in zip(nums, cost)]
        
        def getCost(target: int):
            return sum(abs(num-target)*cst for num, cst in arr)
        
        l, r = min(nums), max(nums)
        while l < r:
            mid = l + (r-l)//2
            costMid1, costMid2 = getCost(mid), getCost(mid+1)
            if costMid1 < costMid2:
                r = mid
            else:
                l = mid+1
        
        return getCost(l)