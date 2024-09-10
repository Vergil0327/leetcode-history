# Intuition

一開始從nums[i]起跳, 假設下個目的地是nums[j], 那麼分數就是: `nums[i] * (j-i) + nums[j] * (k-1-j)` where k is next next position

從這式子可發現: nums[j]肯定優先選那些**大於nums[i]**的數, 不然nums[i]多跳一格拿的分數還比未來nums[j]來得多
所以: nums[j] 必須大於 nums[i]

那既然只要nums[j] > nums[i]就能有更多獲利, 那代表我們直接greedily計算遞增序列的獲利即可
也就是只要當前nums[i]>nums[prev], 我們就能獲利nums[prev] * (i-prev), 然後更新prev=i
直到我們最終抵達n-1位置

## Concise Solution

也相當於我們持續加上current max

```py
# Concise
n = len(nums)
mx = res = 0
for i in range(n - 1):
    mx = max(mx, nums[i])
    res += mx
return res
```