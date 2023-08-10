# Intuition

see example 1: d = 1, low = 1, high = 13

直覺想到經典的digit DP, 維護這三個變數isGreaterThanLow, isLowerThanHigh, hasLeadingZero
我們每個位數來看, 找出介於[low =  01, high = 13]間的所有digit string

- 不可小於low, 所以要看前面的位數是不是貼著邊界
  - 如果前面位數已經大於low, 當前位數0-9都可選
  - 如果前面位數等於low, 那幫前位數不可選超過low[i]這位
- 不可大於high, 同理, 一樣看前面位數是不是已經貼著邊界
  - 如果前面位數已經小於high, 當前位數0-9都可選

所以我們定義`def dfs(i, dCount, isGreaterThanLow, isLowerThanHigh, hasLeadingZero)`返回所有含有`d`的digit string, 也就是試著用dfs來產生digit string然後計算所有含有d的valid digit string的數目

# Approach

首先先把low跟high轉成string並補成相同長度
ex. low=10, high=1234 => low = "0100", high="1234"

```py
low = str(low)
high = str(high)
while len(low) < len(high):
    low = "0" + low
```

那最終答案就是`dfs(0, 0, False, False, True)`

首先我們從第一位開始, 當前含有`d`的數目`dCount`為0, 並且一開始沒有大於low也沒有小於high, 必且看作前面有leading zero

所以根據這些條件, 我們就能選出當前位數的合法digit使得組成的數能介於[low,high]之間

```py
start = 0 if isGreaterThanLow else int(low[i])
end = 10 if isLowerThanHigh else int(high[i])+1
res = 0
for valid_digit in range(start, end):
    res += dfs(i+1,
               dCount + (1 if valid_digit == d else 0),
               isGreaterThanLow or valid_digit > int(low[i]),
               isLowerThanHigh or valid_digit < int(high[i]),
               hasLeadingZero and valid_digit == 0)
```

**base case**

那base case就是等到我們探討全部位數後, 亦即`i==n`後, 返回當前`dCount`即可