# Intuition

經典的digit DP, 可惜當下沒做出來
我們逐個digit來看, 重點就是只出[1,high]裡的全部合法stepping number後再扣掉[1,low-1]內的stepping number

而digit DP的重點是我們必須要維護prefix, 其中必須包含幾個資訊才能藉此決定下個digit有多少種可能
1. last digit: 我們必須維護last digit, 這樣才能知道加上下個digit是否是合法stepping number
2. 但同時組出來的數字必須在[low,high]之間, 所以我們還必須維護`isGreaterThanLow`, `isLowerThanHigh`, 也常有人用`tight`表示, 也就是用boolean來存下我們當前建構的數值是不是貼在邊界上.這會影響我們下個digit的範圍
   1. 如果目前建構的數值`isGreaterThanLow=True`, 代表下個digit從`0`開始組都會比`low`還要大. 反之, 最低必須高過low[i]
   2. 如果目前建構的數值`isLowerThanHigh=True`, 代表下個digit最高到`9`都可以使用. 反之, 最高不得超過`high[i]`
3. 另外由於不准有leading zero, 所以我們還得判斷當前有沒有leading zeros, 以及組完之後的下個狀態有沒有leading zero. 狀態轉移為`hasLeadingZero and current_digit == 0`
   - 如果有leading zero, 那我們下個數可以接任意digit, 代表我們正打算開始建構數字. 但如果沒有leading zeros, 代表我們正建構到一半, 這時就必須加上`isGreaterThanLow`跟`isLowerThanHigh`來判斷有哪些合法digit

那這邊有個小技巧是, 我們將`low`前面加上leading zero補滿到跟`high`同位數, 這樣我們在進行top-down DP cursion時比較好處理

```py
low = '0' * (len(high) - len(low)) + low
```

那接下來就用dfs來找出合法的stepping number, 那合法的stepping number條件是:
1. 某個位數的第一個digit一定是合法stepping number. 或者說一位數必定是stepping number => 所以當有`hasLeadingZero=True`時, 必定是第一位數
   - 當有leading zero時, 我們可以選擇append合法[1,9]來建構.
   - 或是繼續append `0`來搜索下個位數
   - ex. `0XXXX`, `1XXXX`, `2XXXX`, ...其中XXXX又可以是`0YYY`, `1YYY`, `2YYY`, ...
2. 再來就是相鄰兩digit的差為1, `abs(prevDigit - current_digit) = 1`

```py
# low = 1 => low = 00001
#           high = 10001
mod = 1_000_000_007
def dfs(i, isGreaterThanLow, isLowerThanHigh, prevDigit, hasLeadingZero):
    if i == n: return 1

    start = 0 if isGreaterThanLow else int(low[i])
    end = 10 if isLowerThanHigh else int(high[i])+1
    
    cnt = 0
    for d in range(start, end):
        if hasLeadingZero or abs(prevDigit-d) == 1:
            cnt += dfs(i+1,
                    isGreaterThanLow or d > int(low[i]),
                    isLowerThanHigh or d < int(high[i]),
                    d,
                    hasLeadingZero and d == 0)
            cnt %= mod
    return cnt
return dfs(0, False, False, -1, True)
```

**base case**

當我們查看完`n`位數後, 代表我們也找完範圍內全部stepping number了
`if i == n: return 1`