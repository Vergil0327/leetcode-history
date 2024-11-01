# Intuition

想法很簡單, 一開始想到下面這例子
會發現隨著`l`往右, `r`會是單調往左的
所以想到可以用two-pointer 先找出左右兩側的subarray
再配合prefix sum就能知道兩側以及中間`1`的個數

並且會發現只有`l`跟`r`接續著連續`0`的時候, 我們的隔板才能移動
所以對於當前`l`, `r`來說方法數為: **(左邊連續0個數+1) * (右邊連續0個數+1)**

```
1 | 000...000 1 000...000 | 1
  l                       r
方法 = (左邊連續0個數+1) * (右邊連續0個數+1) => +1是因為把全拿掉也是一種情形
```

因此我們如果預先處理好`consecutive0Right[i]`跟`consecutive0Left[i]`, 表示從`i`位置開始, 往右往左有多少個連續0的話

那我們就能配合上面的two pointers以Ｏ(1)時間計算總共有多少方法數, 大致框架如下:

```py
res = 0
r = n-1
for l in range(n):
    if s[l] == "0": continue

    left = presum[l+1]
    while l < r and presum[n]-presum[r] < left:
        r -= 1
    right = presum[n] - presum[r]
    middle = presum[n] - left - right
    if left == middle == right:
        res += (consecutive0Right[l+1]+1) * (consecutive0Left[r-1]+1)
        res %= mod
return res
```

## 預處理

```py
presum = [0]* (n+1)
for i in range(n):
    presum[i+1] = presum[i] + int(s[i] == "1")

consecutive0Right = [0] * (n+1)
for i in range(n-1, -1, -1):
    if s[i] == "0":
        consecutive0Right[i] = consecutive0Right[i+1] + 1

consecutive0Left = [0] * n
for i in range(n):
    if s[i] == "0":
        consecutive0Left[i] = (consecutive0Left[i-1] if i-1>=0 else 0) + 1
```

## Edge Case

但有個特殊情況是當s[i]全都是`"0"`的話, 這時我們就是任選兩個位置放隔板即可:

```py
if presum[n] == 0:
    # method 1
    ways = comb(n-1, 2)

    # method 2
    ways = (n-1)*(n-2)//2

    # method 3
    # 或者遍歷n-1個隔板位置, 當其中一個隔板放置i, 另個隔板能放的位置剩(i-1)個位置
    # 也就是對於隔板i來說, 有i-1種方法, 總和即可
    ways = 0
    for i in range(1, n):
        ways += (i-1)
        ways %= mod
    return ways
```

# Optimization

其實要切出三等份, 只可能有一種情形
我們也不需要用two pointer去找, 我們紀錄每個`"1"`的index
然後

- left_consecutive_0 = ones[target] - ones[target-1] - 1
- right_consecutive_0 = ones[target*2] - ones[target*2-1] - 1

所以同樣地, 方法數就是:

```py
ones = []
for i, ch in enumerate(s):
    if ch == '1':
        ones.append(i)

target = presum[n]//3
left = ones[target] - ones[target-1]
right = ones[target*2] - ones[target*2-1]

return left * right % mod
```

# Complexity

- time: O(n)
- space: O(n)