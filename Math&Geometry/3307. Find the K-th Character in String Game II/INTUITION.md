# Intuition

append step:

```
final step:
size: n
target: k
[X X X X X X X X X X X X X X X O]
                               k

prev step
size: n/2
target: k-n/2
[X X X X X X X O ... ... ... ...]
              k/2

prev step
size: (n/2) /2
target: (k-n/2) - ((n/2)/2)
[X X X O ... ... ... ... ... ...]
      k/4

prev step
size: ((n/2) /2)/2
target: (k-n/2) - ((n/2)/2) - (((n/2) /2)/2)
[X O ... ... ... ... ... ... ...]
  k/8

back to first step

[O ... ... ... ... ... ... ...]
k/16
```

change step:

在大小, 位置方面也是一樣
只是每操作一次, `shift`就`+1`

所以大致上我們要做的, 是從`n`, `k`, `shift=0`開始遞歸回到第一步


所以首先, 我們得先知道要多少操作才會覆蓋`k-th element`

```py
n = 1
op = 0
while n < k:
    n *= 2
    op += 1
```

那在知道我們需要多少操作數以及字串長度後, 我們就`(n, k)`逆著對應`operations[i]`處理即可

> 其實`n`跟`op`可以直接透過數學解出來, 看k需要多少次2的倍數才能涵蓋, 那知道後也能知道n為多少
> op = ceil(log2(k))
> n = pow(2, op)

- 如果`operations[i] == 0`:
  - 判斷當前`k`在前半還是後半
    - 在前半的話位置不變, 然後長度`n //= 2`
    - 在後半的話位置變為`k - n//2`, 然後長度`n //= 2`

- 如果`operations[i] == 1`:
  - 位置變化如上, 差別在於`shift += 1`

那最後我們就知道`a`從第一個步驟開始, 變化到`k-th element`經歷多少次`shfit`
返回`"a" + shift%26`即為答案

```py
APPEND, SHIFT = 0, 1

shift = 0
for i in range(op-1, -1, -1):
    if k > n//2: # 代表是透過操作得到的
        if operations[i] == APPEND:
            k = k-n//2
        else:
            k = k-n//2
            shift = (shift+1)%26
    # else:
    #     do nothing

    n //= 2

return chr(ord("a") + shift)
```
