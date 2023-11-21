# Intuition

抵達rooms[i]奇數次: nextVisit[i] => 0 <= nextVisit[i] <= i, 只會往回走
抵達rooms[i]偶數次: (i+1) % n => 唯一會繼續前進的策略

想法是找出從nextVisit[i]走回rooms[i]需要多少天, 最後再加總起來
從nextVisit[i]走回rooms[i], 介於中間的所有房間必定都得經過偶數次後才能抵達rooms[i], 不然會持續退回到nextVisit[j] where nextVisit[i] < j < i
等到走回rooms[i]後的那次為偶數次, 所以能往前一格到rooms[i+1], 這時又會回到nextVisit[i+1], 如果nextVisit[i+1]又經過rooms[i]這時又要再重新加上上一輪一次
整個過程是個遞歸, 當前需要的天數會依靠先前經過的房間所需天數, 有dynamic programming的感覺

所以定義dp[i]: the days you need to arrive at i at first time
```
所以dp[i+1] = dp[i] + 1 + (dp[i] - dp[nextVisit[i]]) + 1
            = 抵達i + 1天退回nextVisit[i] + 從nextVisit[i]再回到i的天數 + 1天抵達i+1
```