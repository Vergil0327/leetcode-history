# Intuition

第一種想法: DP, Longest Increasing Subsequence
找看看當前nums存不存在長度`n-1`的LIS, 如果有, 則可以透過一次變換使得整體變成non-decreasing
但時間上會是O(n^2) => TLE

第二種想法: GREEDY!
一但發現nums[i] > nums[i+1], 那兩種可能處理方式使得這對pair non-decreasing:
1. 降低nums[i]: nums[i] = nums[i+1]
2. 拉高nums[i+1]: nums[i+1] = nums[i]

之後就檢查兩種情況的處理方式有沒有合法的即可

time: O(nlogn)
