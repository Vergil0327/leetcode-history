# Intuition

首先我們先找出`n`落在哪個位數的區間

首先`digits`從一位數開始
每個位數有`10**d - 10**(d-1)`個數字
因此就有`d*(10**d) - d*(10**(d-1))`個characters

```
digits=1 (< 10): 1~9
digits=2 (< 100): 10~99
```

我們可以持續遞增digits來找出`n`落在哪個區間
```
digits = 1
cnt = count(digits)
while n > cnt:
    n -= cnt
    digits += 1
    cnt = count(digits)
```

找出`n`落在哪個`digits`範圍後，假設 digits=2, n=5
代表我們從10開始往後找, 10,11,12,13,...

```python
i = n//digits
j = n%digits
```

-> i=2, j=1 -> ans = "12"[0]

`digits=2`代表 base為 10**(digits-1)=10開始
`i`代表我們要在`digits`位數開始找第`i`個數 (0-index)
因此`i=2`代表10開始的第二個數 = base + i = `12`

但還要判斷`j`，`j`要分兩個case討論:
- 如果`j=0`，代表我們要找的數是base+i的前一個數的最後一個字符.
  - `ans = str(base+i-1)[-1]`
- 如果`j>0`，代表我們要找的是`str(base+i)`的第`j-1`的字符
  - `ans = str(base+i)[j-1]`
  - j為1-index