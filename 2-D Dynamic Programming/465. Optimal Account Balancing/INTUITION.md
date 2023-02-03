# Intuition

這題經典解法是使用 `bitmask` 壓縮狀態的DP問題

如果目前這組人的淨負債為零，總共有`n`個人的話那麼最多需要`n-1`次交易來清償負債，所以這題的核心思想是

我們要盡可能地將人分成數個淨負債為零的小組，這樣最終答案就是總人數減掉小組數目

*總共十個人互相有債務關係，最多可以分成五個小組彼此能清償債務，這樣每組需要交易一次，總共需要交易`5`次即可全部清償完畢*

因此我們用bitmask來表示有哪些人被選為一組
例如`bitmask = 1110001101`，1就是代表備選中，第`i-th bit`就代表第`i`位人

所以我們就遍歷所有可能組合，然後計算他們的總債務，如果`SUM[state]=0`，代表他們的淨負債為0，我們可以試圖將它分成兩個submask，使得dp狀態轉移為:

```py
if SUM[bitmask] == 0:
    # 透過bin(bitmask).count("1")可知道有多少人
    # n個人需要n-1次交易
    dp[bitmask] = bin(bitmask).count("1")-1

    submask = bitmask
    while submask:
        if SUM[submask] == 0:
            dp[bitmask] = min(dp[bitmask], dp[submask]+dp[bitmask-submask])
        submask = (submask-1)&bitmask
```

由於這個高效率遍歷submask的算法必須不能為0
因此我們遍歷bitmask時，從1開始，0就單獨處理

dp[bitmask]的定義為: 從bitmask可得知，當有現在這些人時的最少交易次數
因此dp[0]的意思就為0人的時候的可清償負債的最少交易次數，那就是0，因為沒有任何債務關係

那這個遍歷submask的模板，時間複雜度為O(3^n), n為bit數

```py
submask = bitmask
while submask:
    if SUM[submask] == 0:
        dp[bitmask] = min(dp[bitmask], dp[submask]+dp[bitmask-submask])
    submask = (submask-1)&bitmask
```

詳細可參照這[Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html)

# Complexity

- time complexity

$$O(3^n)$$

- space complexity

$$O(2^n)$$