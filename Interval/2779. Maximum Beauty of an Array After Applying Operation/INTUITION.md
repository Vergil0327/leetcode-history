# Intuition

每個nums[i]都可換成[nums[i]-k, nums[i]+k]
所以把每個nums[i]轉換成一個interval
那這樣我們要求的就變成最多overlapping的interval數目

所以我們轉換成interval後對interval[i][1] where interval[i] = [start, end]排序
然後就可以用sliding window:

對於當前的interval[i]來說, 如果作為左端點
只要右端點interval[j][0] <= interval[i][1], 那就代表有重疊可以持續移動
```py
j = 1
for i in range(n):
    while j < n and interval[j][0] <= interval[i][1]:
        j += 1
    res = max(res, j-i)
```
那我們就持續在合法範圍, 更新res = max(res, j-i)即可

# Other Solution

但實際上我們可以直接對nums排序

那我們要找的就是一個sliding window nums[l:r], 使得nums[r]-nums[l] <= 2*k

```py
def maximumBeauty(self, nums: List[int], k: int) -> int:
    nums.sort()
    i = 0
    for j in range(len(nums)):
        if nums[j] - nums[i] > k * 2:
            i += 1
    return j - i + 1
```