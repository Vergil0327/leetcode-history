# Intuition

如果以mountain peak為分界, 左右都是有序的
因此只要找出peak, 就可以分別對兩段做binary search找target位置

而找peak的方式也很簡單
我們一樣做binary search, 然後判斷`mid`跟`mid+1`的值就能知道目前是處於遞增還是遞減序列

```py
n = mountain_arr.length()
l, r = 0, n-1

# find peak
while l < r:
    mid = l + (r-l)//2
    x = mountain_arr.get(mid)
    y = mountain_arr.get(mid+1)
    if x < y:
        l = mid+1
    else:
        r = mid
peak = l
```

再來就分別對`[0,peak]`跟`[peak,n-1]`這兩個區間做binary search即可