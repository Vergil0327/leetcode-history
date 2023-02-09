# Intuition

最直接的想法就是求出所有subarray的和然後排序在相加，時間複雜度為$O(n^2)$

# Other Solution
再來如果我們能知道如何求出第k大的subarray和的話，那我們就可以用binary search來一個個找出範圍內的subarray和了

對於subarray的和，長度越長肯定和越大
因此我們可以用雙指針，一但目前的和 `currSum` 加上 nums[r] 後還小於等於 `targetSum`，我們就移動 `r` 指針
這樣等到跳出循環後 `r-l`就是和小於`targetSum`的數量
然後在移動 `l` 左指針繼續找，即可找出sum(subarray)小於某個和的subarray數量

```py
def smallerOrEqual(targetSum):
    cnt = currSum = r = 0
    for l in range(n):
        while r < n and currSum+nums[r] <= targetSum:
            currSum += nums[r]
            r += 1
        cnt += r-l
        currSum -= nums[l]

    return cnt
```

以 targetSum=5, nums = [1,2,3,4]為例, 如下所示
```
targetSum = 5

[1,2,3,4]
 l   r
[1,2,3,4]
   l   r
[1,2,3,4]
     l r
1
1+2
cnt += (r-l) = (2-0)
2
2 + 3
cnt += (r-l) = (3-1)
3
cnt += (r-l) = (3-2)
```