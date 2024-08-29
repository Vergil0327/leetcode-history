# Intuition

good rob day的條件是security[i]的:
- 前面至少有至少`time`個non-increasing元素
- 後面至少有至少`time`個non-decreasing元素

所以我們可以先由左往右遍歷一遍, 定義:

```py
dp = [0] * n # maximum consecutive non-increasing for prefix security[:i]
cnt = 0
for i in range(1, n):
    if security[i-1] >= security[i]:
        cnt += 1
    else:
        cnt = 0

    dp[i] = cnt
```

dp[i]: the number of maximum consecutive non-increasing elements for prefix security[:i]

那這樣我們只要再從後往前遍歷一遍, 找出the number of maximum consecutive non-decreasing elements的同時, 查看dp[i]是否大於等於time, 即可知道i-th day是不是合法

```py
res = []
cnt = 0 # 相當於 numNonDec = [0] * n # maximum consecutive non-decreasing for suffix security[i:]
for i in range(n-1, -1, -1):
    if i < n-1 and security[i] <= security[i+1]:
        cnt += 1
    else:
        cnt = 0
    if dp[i] >= time and cnt >= time:
        res.append(i)
return res

```