# Intuition

直覺想到直接digit DP搜索所有可能

```py
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        lo = "1"
        hi = str(n-1)
        while len(lo) < len(hi):
            lo = "0" + lo

        size = len(hi)

        @cache
        def dfs(i, isGreaterThanLow, isLowerThanHigh, leadingZeros, num):
            if i >= size:
                other = n-num
                return int(str(other).count('0') == 0)
            start = 0 if isGreaterThanLow else int(lo[i])
            end = 10 if isLowerThanHigh else int(hi[i]) + 1

            res = 0
            for d in range(start, end):
                r = (num*10+d) % 10
                if not leadingZeros and r == 0: continue
                res += dfs(
                    i + 1,
                    isGreaterThanLow or d > int(lo[i]),
                    isLowerThanHigh or d < int(hi[i]),
                    leadingZeros and d == 0,
                    num*10+d
                )
            return res
        return dfs(0, False, False, True, 0)
```

但這樣會MLE (Memory Limit Exceeded)

所以要換個方式去進行digit DP

首先目標找出: `X + Y = n`
代表`X`跟`Y`的每個位數相加後(並注意前一位進位`carry`), 會等同於`n`的該位數
所以我們可以一樣用digit DP的遞歸概念, 去遍歷每一位的`X`跟`Y`的digit, `dX`跟`dY`, 並記錄`carry`
每一位必須滿足`dX + dY + carry = target digit in n`

所以可以先寫出遞歸狀態框架:

```py
def dfs(position, carry):
    target = digits[pos]

    res = 0
    for dX in range(10):
        for dY in range(10):
            total = dX+dY+carry
            if (total%10 != target): continue
```

但在逐步建構`X`跟`Y`時, 我們可以在任何一位去停止建構`X`或`Y`, 然後剩餘位數就補上leading zeros
所以我們還需要兩個狀態變數, `endX`, `endY`來表示, 當前的`X`跟`Y`建構完了沒

再加入這兩個變數後, 我們就能以此來排除掉建構過程中, `X`, `Y`不能含有除了leading zero以外的`0`了
- 如果`X`建構結束, 那麼接下來的`dX`只能是0
- 如果`X`還沒建構完, 那麼接下來的`dX`不能為0
- 如果`Y`建構結束, 那麼接下來的`dY`只能是0
- 如果`Y`還沒建構完, 那麼接下來的`dY`不能為0

```py
digits = list(map(int, list(str(n))))
digits.reverse()  # dfs低位往高位處理

# X + Y = n
def dfs(pos, carry, endX, endY):
    target = digits[pos]

    res = 0
    for dX in range(10):
        if endX and dX != 0: continue
        if not endX and dX == 0: continue

        for dY in range(10):
            if endY and dY != 0: continue
            if not endY and dY == 0: continue

            total = dX+dY+carry
            if (total%10 != target): continue

    return res
```

最後, 對於`X`跟`Y`, 我們可以在任意位數停止建構, 來找出所有可能的`X`, `Y` pair, 所以
- 如果已經建構完 `endX == True` 或 `endY == True`, 那麼下個狀態也只能是True (`endX' == endY' == True`)
- 如果還沒建構完 `endX == False`, `endY == False`, 那麼下個狀態可以是True也可以是False (可以繼續建構也可以停止建構)

這邊可以寫成:
```py
newEndXs = [endX]
if not endX:
    newEndXs.append(True)

newEndYs = [endY]
if not endY:
    newEndYs.append(True)

for newEndX in newEndXs:
    for newEndY in newEndYs:
        res += dfs(pos+1, total//10, newEndX, newEndY)
```

所有可能加總起來即為答案

### Base Case

什麼時候才是`X`跟`Y`的合法建構? => `carry == 0 and endX and endY` (沒有多餘進位, 並且`X`跟`Y`都已經標示建構完畢)

### Video Explanation by @HuifengGuan in Chinese

[Youtube](https://www.youtube.com/watch?v=OS_1E9o4k1s)