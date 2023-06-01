# Intuition

求最少操作, 首先感覺上先往binary search看看能不能猜出答案
由於限制`x > y`

所以對於`k`個操作來說, 我們可以每個nums[i]都剪去`y * k`
由於`x > y`所以我們還會有額外的`(x-y)*k`個操作可以用來剪去`

我們怎麼操作並不重要, binary search by value中的`check`僅需要知道當前的`mid`是不是可行解即可

因此helper function `check`也很直觀
僅需要查看每個`nums[i]`減去`y*k`後
1. 如果已經`<=0`, 那就合乎條件
2. 如果`>0`
   - 從額外的`(x-y)*k`這些操作拿來將當前的數減至0.
   - 如果無法減至0, 那就返回`False`, 代表當前操作數不夠用
等到全部遍歷完都能處理成`<=0`的數後, 則返回`True`

而找min operation的binary search框架為:
```py
l, r = 0, max(nums)
while l < r:
    mid = l + (r-l)//2
    if check(mid, x, y):
        r = mid
    else:
        l = mid+1
return l
```