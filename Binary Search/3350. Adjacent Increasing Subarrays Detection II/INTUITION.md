# Intuition

這題是[3349. Adjacent Increasing Subarrays Detection I](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/)的follow-up

如果知道前置題目的話會知道, 我們可以透過O(n)時間判斷存不存在一個符合題意且長度為`k`的兩個連續subarray

```py
n = len(nums)

max_length = [0] * (n+1)
for i in range(n):
    if nums[i] > nums[i-1]:
        max_length[i+1] = max_length[i] + 1
    else:
        max_length[i+1] = 1

def check(k):
    for i in range(1, n+1):
        if i-k >= 0 and max_length[i] >= k and max_length[i-k] >= k:
            return True
    return False
```

那有了這項條件後, 其實我們就透過binary search去猜測這個合法最長長度即可
利用bianry search可以以O(nlogn)時間去猜出最大合法長度`k`

search range: `[1, len(nums)//2]`

```py
l, r = 1, n//2
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```