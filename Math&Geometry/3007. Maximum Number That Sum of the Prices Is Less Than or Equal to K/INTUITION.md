# Intuition

price of nums代表[1,num]這區間的每個數, 所有每個能被x整除的bit位上的1的總和 (**1-indexed**)
所以很明顯能看出num越大, 他的prices總和也越大且具有單調遞增性質

因此很自然的能想到binary search, 核心框架如下

```py
l, r = 1, 10**15
while l < r:
    mid = r - (r-l)//2
    if check(mid, k, x):
        l = mid
    else:
        r = mid-1
return l
```

所以這時最大的問題就是, 該如何寫這個helper function `check`?

```
bits of num = X X X 0 Y Y Y
                    i
```

首先如果bit[i] of num = 0
那麼[1,num]之間有多少個i-th bit是1的?

- 高位bits, X X X, 可以是000 ~ XXX-1
- 低位bits, Y Y Y, 可以是任意0/1 bit, 也就是000~111
- 所以[1,num]之間總共有: XXX * 2^i 個1在i-th bit上

```
bits of num = X X X 1 Y Y Y
                    i
```
那麼如果bit[i] of num = 1
那麼[1,num]之間有多少個i-th bit是1的?

- 高位bits, X X X, 可以是
    1. 比 X X X 小:
        - 那麼XXX範圍`0~XXX-1`, 那麼低位bits, Y Y Y, 可以是任意數, 所以總共有 XXX * 2^i 個小於num的數在i-th bit有1
    2. 跟 X X X 一樣:
        - XXX只有一種可能, 那麼低位bits, YYY, 只能是000~ YYY, 所以是YYY+1個數在i-th bit上有1

這個計算的想法跟[leetcode 233. Number of Digit One](../233.%20Number%20of%20Digit%20One/README.md)很像