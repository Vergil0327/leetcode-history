# Intuition

我們要從位於[low, high]這範圍內找出所有k的倍數並且該數要符合
`奇數的數目要等於偶數的數目`這條件

也就是我們要查看在[low,high]範圍內, 我們能組出多少`num`使得:
1. 計算`num`的每個位數的digit後, 奇數的個數必須等於偶數的個數
2. 同時`num`必須能被`k`整除

這很明顯是digit DP

digit DP的套路是：

`用dfs組出所有符合條件的num`

首先我們將`low`, `high`轉成string, 並且對`low`補上leading zeros使得`low`,`high`位數相等
那這樣我們等等在dfs的過程中, 就可以透過low[i]跟high[i]知道我們當前能選擇的digit範圍是從哪到哪

我們dfs只要配合`isGreaterThanLow`, `isLowerThanHigh`, `leadingZeros`三種狀態即可追蹤我們當前第`i`位數有哪些選擇使得當前組出來的num位於[low,high]之間

- 如果`isGreaterThanLow = True`, 代表在前面步驟時, num已經 > low, 因此當前digit就可以從`0`開始
不然的話就只能從low[i]開始, 不然組出來的`num`不會`>= low`.
    - ex. low = "032567", num目前是"04", 那這樣num的下一位接0也可以
    - ex. low = "032567", num目前是"03", 那這樣num的下一位只能從2,3,4開始往後組, 不然num="031"的話不管怎麼組都不會在[low,high]之間
- 而`isLowerThanHigh`也是一樣道理

所以:
```py
start = 0 if isGreaterThanLow else int(low[i])
end = 10 if isLowerThanHigh else int(high[i])+1
for valid_digit in range(start, end):
    # dfs
```

再來我們要看怎樣才能符合我們要的合法num
由於最終的num必須`odd == even`, 所以我們在組的過程中同時紀錄我們當前選擇的digit是奇數還是偶數

`def dfs(i, isGreaterThanLow, isLowerThanHigh, leadingZeros, odd, even):`

- 當`valid_digit >= 1 and valid_digit%2 != 0`時, 代表我們當前選擇的digit是奇數, `odd += 1`
- 但valid_digit為偶數時比較特別, 因為可能有leading zero的存在, 所以當`valid_digit=0`時必須特別判斷他是不是leading zero, 不是的話才是合法的digit
  - `not leadingZeros and valid_digit == 0`, 此時`even += 1`
  - `valid_digit >= 2 and valid_digit%2 == 0`, 此時`even += 1`

而最後`num`還必須能被k整除, 要判斷能不能被`k`整除, 我們只知要知道當前的餘數即可, 所以我們的dfs再多紀錄`remainder`變成:

`def dfs(i, isGreaterThanLow, isLowerThanHigh, leadingZeros, odd, even, remainder):`

每加上一個`valid_digit`代表當前的`num`的餘數變成: `(remainder * 10 + valid_digit)%k`

所以最終dfs的狀態轉移為:

```py
def dfs(i, isGreaterThanLow, isLowerThanHigh, leadingZeros, odd, even, remainder):
    start = 0 if isGreaterThanLow else int(lo[i])
    end = 10 if isLowerThanHigh else int(hi[i])+1

    res = 0
    for d in range(start, end):
        res += dfs(i+1,
                isGreaterThanLow or d > int(lo[i]),
                isLowerThanHigh or d < int(hi[i]),
                leadingZeros and d == 0,
                odd + (1 if d >= 1 and d%2 != 0 else 0),
                even + (1 if (not leadingZeros and d == 0 or d>=2 and d%2 == 0) else 0),
                (remainder*10 + d)%k)
    return res
```

而base case就是當組完`n`位數後:
必須被能`k`整除並且奇數個數等於偶數個數
`return 1 if remainder == 0 and even == odd else 0`


# English

we can use DFS with these 3 state `isGreaterThanLow`, `isLowerThanHigh`, and `leadingZeros` to explore every possible `num` within [low,high] range.

since we want our final `num` is divisible by `k` and number of odd digit equals number of even digit, we add three more state in our dfs.

thus, we can define:
`def dfs(i, isGreaterThanLow, isLowerThanHigh, leadingZeros, oddCnt, evenCnt, remainder)` return the number of valid num within [low,high]

state transfer is clear:
- $remainder = (remainder*10 + d)%k$
- $odd = odd + (1 \ if\ d >= \ 1\ and\ d\%2\ != 0\ else\ 0)$
- since leading zeros is not part of even digit,
    - `even = even + (1 if not leadingZeros and d == 0 else 0)`
    - `even = even + (1 if d>=2 and d%2 == 0 else 0)`
