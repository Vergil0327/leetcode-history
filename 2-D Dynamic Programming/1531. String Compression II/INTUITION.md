# Intuition

一開始想法是先將`s`分成每個encoded parts, 看每個字母個別有幾個count
然後我們看當前的s[i]刪除[0:K]個後的encoded length變化

但當時沒想周全的是:
`Example 2. s = "aabbaa"`
當我們把中間兩個b刪除後, 答案並不是a2 + a2 = 4
而是a2+a2 = a4 = 2 (running length encoded)

所以我們還需要知道在前`i`個字母中, 我們在刪除s[j]後
s[1:j)這段跟s[j=1:i]這段拼起來的encoded length
如果這結果紀錄在dp的話會像是:
`dp[i][k][ch][cnt] = dp[i-1][k-1][ch] + addedLength(s[j+1:i])

dp[i][k][ch][cnt] = considering s[1:i] in 1-indexed, the minimum length with `k` characters removed, the last character as `ch` and the repeating number of ch is `cnt`

> 由於- 1 <= s.length <= 100, 0 <= k <= s.length. 原本第四個維度`cnt`的空間大小應為100, 最多就repeating 99次
> 但由於encoded的關係, 在repeating number of ch `cnt >= 10`之後的encoded length跟`cnt <= 99`的encoded length都一樣長. (ex. a10 ~ a99)
> 所以空間並不需要開到100, 我們僅需要開10即可
> 從`>=10`後都得encoded length都不會變

```
s = [X X X X X X] X {X X X X X}
                  j          i
```

但每個dp[i][k][ch][cnt]的前驅狀態有很多種可能, 並不好推斷
但是對於當前的dp[i][k][ch][cnt]的下一個狀態, 相對好判斷
當我們加上s[i+1]後, 我們可以基於dp[i][k][ch][cnt]上更新dp[i+1][k'][ch'][cnt']

所以我們接下用當前狀態更新未來狀態的方式來計算dp[i][k][ch][cnt]

**初始化**

`i`用**1-indexed**

```py
s = "#" + s

# dp[i][k][ch][cnt]
# dp = [[[[inf]*101 for _ in range(27)] for _ in range(K+1)]for _ in range(n+1)]
dp = [[[[inf]*11 for _ in range(27)] for _ in range(K+2)]for _ in range(n+1)]
```

**base case**

the minimum length for 0 characters, 0 removed, use 26 to represent empty character (0-25 is a-z), 0 number of character is `0`

`dp[0][0][26][0] = 0`

**狀態轉移**

```
s = [X X X X X X] X X X X X X
               i i+1
              ch
```

如果當前最後一個repeating character為`ch`, 當前狀態為`dp[i][k][ch][cnt]`

- 如果我們決定刪除s[i+1]
  - 那麼下個狀態為:`dp[i+1][k+1][ch][cnt] = min(dp[i+1][k+1][ch][cnt], dp[i][k][ch][cnt])
- 如果我們決定保留s[i+1]
  - 如果ch == s[i+1], 那我們要merge, 然後再看長度變化多少
    - dp[i+1][k][ch][min(10, cnt+1)] = min(dp[i+1][k][ch][min(10, cnt+1)], dp[i][k][ch][cnt]+added)
    - if cnt == 1:               # "a" -> "a2"
    - elif cnt > 1 and cnt <= 8: # "a2" -> "a9"
    - elif cnt == 9:             # "a9" -> "a10"
    - elif cnt > 9:              # "a10" -> "a99"
    - 注意這邊我們沒有cover到這個case: s="aaa...aaa" where s.length = 100. 為了省空間省時間, 我們只cover到a99
      - 所以我們額外handle K=0 的情況

  - 如果ch != s[i+1], 那麼我們就是原本長度再多上一個新的s[i+1]字符
    - dp[i+1][k][or(s[i+1])-ord("a")][1] = min(dp[i+1][k][or(s[i+1])-ord("a")][1], dp[i][k][ch][cnt] + 1)