# Top-Down DP

## Intuition

對於一個數`n`來說，我們每次都拆分成 i + n-i，那麼其乘積則為i * (n-i)
並且每次選擇，我們都可以選擇`不拆分`，或是`繼續拆分`，類似常見的take-or-skip strategy
如此一來，decision tree 就很明顯了

```
for num in range(1, n):
    res = max(res, num * (n-num))
    res = max(res, num * dfs(n-num))
```

遞歸到最後即可得知最大乘積為多少

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$

# Bottom-Up

## Intuition

思維跟Top-Down一樣，只是Bottom-Up的話，我們必須從小求到大

對於`num`來說：
1. 它可以拆分成 `i + (num-i) 其中 i 從1到num-1`，此時的product=i * (num-i)
2. 但也可以繼續對`num-i`拆分

因此定義dp[num]為`maximum product of intergers which sum(integers) = num`

狀態轉移方程則為

```
dp[num] = max(dp[num]), 拆分為i+(num-i), 繼續拆分(num-i))
        = max(dp[num], i * (num-i), i * dp[num-i])
```

並且 Base case 恰好定義為0即可

