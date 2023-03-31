# Intuition

1,0,1,0,1, goal = 2

我們要找一個subarray的和為`goal`
對於一個subarray, 我們可以把它轉成一個prefix sum的形式

```
X X X X X X X X X X X X X X X X X
        j'      j               i
```

我們要找prefix[i]-prefix[j] = goal
因此prefix[j] = prefix[i] - goal

所以我們遍歷i的時候，如果我們能找到一個prefix[j] = prefix[i] - goal
那就代表我們找到一個subarray其和為goal
如果有 n 個prefix[j], 就代表對於i來說, 有n個j使得sum(subarray[j:i])為goal

因此對於prefix[j]的個數, 我們可以在計算prefix[i]的時候就利用一個hashmap來記錄次數
-> `dp[presum[i]] = dp.get(presum[i], 0) + 1`

這樣我們在遍歷過程中就能計算，對於右邊界為i的subarray, 能有多少個j可以使得subarray的和為goal
```py
dp = {0: 1}
for i in range(1, n+1):
    presum[i] = presum[i-1]+nums[i-1]

    if presum[i]-goal in dp:
        answer += dp[presum[i]-goal]
    dp[presum[i]] = dp.get(presum[i], 0) + 1
return answer
```

這邊要注意初始值:
`dp = {0: 1}`
因為如果prefix[i]本身就等於goal得話，相當於我們找到一個prefix[j]=0的j
考慮到這種情況，所以要設hashmap的初始值為{0: 1}