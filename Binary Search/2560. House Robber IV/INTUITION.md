# Intuition

這提要求的是一個 MinMax
在任何要求minimum max的時候，都可以試著看能不能使用Binary Search

```py
l, r = min(nums), max(nums)
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

這題最難的是在於 helper function `check(mid)`
我們該如何確認，對於當前猜的`mid`作為capacity時，nums可以滿足`mid`作為min max capacity?

這邊可試著以Greedy的方式盡可能找出符合的pair，然後看個數有沒有足夠k個
方式是:
1. 如果當前這個nums[i] <= target cap，那我們就先取他然後記錄當前位置
2. 如果我們前一個有取，那當前這個一定不能取，必須跳過
   - 跳過後，對於任何 <= target cap的nums[i]，我們就又能再取了

只要符合條件，盡可能越早取越好，越後面取肯定會取得比前面取的還要少
因此透過這樣的方式來check

```py
def check(cap):
    takePrev = False
    cnt = 0
    for i, num in enumerate(nums):
        if takePrev:
            takePrev = False
            continue
        if num <= cap:
            cnt += 1
            takePrev = True
    return cnt >= k
```

那當我們 `check(mid)` 後
- 如果夠，那代表這個cap可能是答案，binary search就可以縮短上界
- 如果不夠，那就提高binary search下界，拉高cap往上猜

# Complexity

- time complexity

$$O(nlogn)$$
- space complexity

$$O(1)$$