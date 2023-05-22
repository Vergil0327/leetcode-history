# Intuition

看到subarray, 首先想到是不是能固定一個邊界然後高效地找出另一個邊界
也就是利用**Two Pointers**來進行

我們要找所有`max`符合[left,right]這區間的subarray
那透過sliding window, 我們可以求出不大於K的subarray

對於要求不大於K的sliding window如下
相當於我們固定左邊界, 然後有`r-l`個合法右邊界構成的subarray
```py
# [l:r)
def lessThan(k):
    res = l = r = 0
    mx = -inf
    while r < n:
        mx = max(mx, nums[r])
        r += 1

        while l < r and mx > k:
            mx = -inf
            l = r
        res += r-l
    return res
```

那麼[left,right]這區間的subarray便可轉化為
lessThan(right) - lessThan(left-1)

# Other Solution - One Pass

我們一樣用two pointers `l`, `r`來代表一個區間(subarray)
一但`nums[i] > right`, 代表含有nums[i]的subarray都不符合
所以我們把左右邊界都重置在`i`位置

一但`nums[i] >= left`, 代表這時的`i`為合法右邊界
由於我們會維持一個left exclusive的區間`(l:r]`
這時的合法subarray個數為`r-l`
相當於固定左邊界`l`,  我們有`r-l`的合法右邊界`r`

```
X X X X X X X X X
                i
l         r
```
