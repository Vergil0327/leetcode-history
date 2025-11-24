# Intuition

兩個範圍內的所有數, 找出所有wave => 想到用digit DP構築所有數值, 並計算Waviness

我們只要紀錄前兩個digit, 那麼再加上當前加上的digit `d`就能知道有沒有合法waviness
並額外記錄到變數`count`裡

所以我們可以修改我們的digit DP template:

```py
low = str(num1)
high = str(num2)
while len(low) < len(high):
    low = "0" + low

@cache
def dfs(i, isGreaterThanLowerbound, isLowerThanUpperbound, prev, mid, count):
    if i == len(high): return count

    start = 0 if isGreaterThanLowerbound else int(low[i])
    end = 10 if isLowerThanUpperbound else int(high[i]) + 1

    res = 0
    for d in range(start, end):

        x = int(
            prev != -1
            and ((prev < mid > d) or (prev > mid < d))
        )

        res += (
            dfs(
                i + 1,
                isGreaterThanLowerbound or d > int(low[i]),
                isLowerThanUpperbound or d < int(high[i]),
                mid,
                d,
                count + x,
            )
        )
    return res

```

但這樣還不夠, 合法的waviness不可以有`prev`是leading zero的情況
因為`063`實際上等於`63`, 長度不足3位數的的waviness為0, 所以必須再額外紀錄現在是否已經滿足長度**3**

```py
valid = valid or prev > 0

# ...
x = int(prev != -1 and valid and ((prev < mid > d) or (prev > mid < d)))
```