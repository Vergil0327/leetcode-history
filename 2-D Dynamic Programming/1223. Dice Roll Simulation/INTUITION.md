# Intuition

首先基本上dp狀態肯定至少為 dp[i][dice], 每一輪根據前一輪狀態來判斷，然後骰子有6面
再來由於每一面最多只能連續骰rollMax[dice]次, 所以我們還得紀錄這訊息來判斷當前狀態是不是合法

所以dp狀態我們可以這麼定義:
dp[i][d][cnt]: the number of distinct sequences that can be obtained with exact n rolls which dice is ended with `d` after `cnt` consecutive times.

那麼當目前連續次數`cnt>1`時, 代表一定是骰的跟前一輪一模一樣, 所以狀態轉移為:
```py
dp[i][d][cnt] += dp[i-1][d][cnt-1]
```

如果當連續次數`cnt=1`時，代表目前為第一次骰出, 代表前一輪必定骰出不同面, 並且可以從任意合法的連續次數轉移過來, 所以狀態轉移為:

```py
for prevD in range(6):
    for k in range(rollMax(prevD)+1):
        dp[i][d][cnt] += dp[i-1][prevD][k]
```

因此整個狀態轉移就出來了，然後我們注意一下邊界條件
當我們第一輪的時候，前一輪什麼都沒骰，因此`cnt=1`並且也不會從其他骰子轉移過來,
所以第一輪的時候我們單獨處理一下, 上述的狀態轉移從第二輪開始:

```py
for d in range(6):
    dp[0][d][1]  = 1
```