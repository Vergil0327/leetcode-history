# Intuition

總共有m個step可操作
最大突破口就是操作數具有單調性
如果我們最早可以在x步就能mark所有位置, 那麼在x+1步肯定也可以
但如果在x步還不行, 那x-1步也不行
在具有單調性條件下, 我們可以嘗試用binary search去猜這個x
那麼再來就考慮我們能不能完成helper function `check`

那麼整體框架是如下, 由於這題可能無解, 最後找出的答案`l`還得在check過一遍

```py
n, m = len(nums), len(changeIndices)
l, r = 0, m
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1

if not check(l): return -1
return l
```

至於`check` helper function該怎辦?

先greedy來想, 每個nums[i]我們都盡可能在最後才mark, 在這之前的每個nums[i]都可以自由分配
而在mark之前需要nums[i]個step
所以我們由右往左, 遇到的第一個就nums[i]就mark, 並記錄需要多少step在`need += nums[i]`上
之後如果再遇到已經mark的, 代表這時我們可以拿它來自由進行`if need > 0: need -= 1`的操作

遍歷完最後看能不能滿足:
1. 每個都有mark到: sum(mark) == n
2. 所需操作為0: need == 0
即可

```py
def check(sec):
    mark = [0] * (n+1)
    need = 0
    for i in range(sec-1, -1, -1):
        idx = changeIndices[i]-1
        if not mark[idx]:
            mark[idx] = 1
            need += nums[idx]
        else:
            if need > 0:
                need -= 1
    return sum(mark) == n and need == 0
```