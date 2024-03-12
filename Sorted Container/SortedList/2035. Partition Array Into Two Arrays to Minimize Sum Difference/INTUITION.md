# Intuition

> Constraints:
> - 1 <= n <= 15
> - nums.length == 2 * n

2^30 ~ 10^9
2^15 = 32768

我們分成兩堆arr1, arr2, 然後用backtracking找出所有subset sum
這樣時間上僅需要2 * 2^15

n = len(nums)//2
subset1[size] = {sum1, sum2, sum3, ...} where 1 <= size <= n
subset2[size] = {sum1, sum2, sum3, ...}

如果我們同時紀錄每個subset_sum的size跟可能的subset_sum
那再來我們只需要搜索k in range(1, n+1)
如果subset1中挑出k個, 那再從subset2中挑出size為`n-k`個裡最互補的subset_sum, 讓整個subset_sum趨近於sum(nums)/2
找出全局最小absolute difference即可

# Optimized

```py
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2      
        res = abs(sum(nums[:n]) - sum(nums[n:]))
        total = sum(nums) 
        target = total // 2 
        
        for k in range(1, n):
            left = [sum(comb) for comb in combinations(nums[:n], k)]
            right = [sum(comb) for comb in combinations(nums[n:], n-k)]
            right.sort()
            for s1 in left:
                i = bisect.bisect_left(right, target - s1) 
                if 0 <= i < len(right):
                    half1 = s1 + right[i]
                    half2 = total - half1
                    diff = abs(half1 - half2)
                    res = min(res, diff) 
        return res
```