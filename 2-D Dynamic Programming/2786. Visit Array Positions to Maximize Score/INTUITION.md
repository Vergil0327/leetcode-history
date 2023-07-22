# Intuition

*Note that initially you have nums[0] points.*
所以重點是parity
如果當前nums[i]跟前一次選擇的parity一樣, 由於不會花費任何cost, 那就直接加上score
但如果不同, 我們就有兩個決策可以選擇:
    1. 如果選了nums[i], 那分數就 += nums[i]-x, 並且parity變為nums[i]%2
    2. 如果不挑nums[i], 那分數跟parity就都不變
    3. 那我們就是兩種決策挑最佳的

所以top-down DP可以很直覺的寫成

```py
@lru_cache(None)
def dfs(i, parity):
    if i == n: return 0
    
    if nums[i]%2 == parity:
        return dfs(i+1, parity) + nums[i]
    else:
        return max(dfs(i+1, nums[i]%2) + nums[i] - x, dfs(i+1, parity))
```

由於parity只可能是`0`, `1`
所以time complexity: O(n*2)

bottom-up也是一樣概念

定義:
dp[i][0]: the maximum score if last element%2 == 0 considering nums[:i]
dp[i][1]: the maximum score if last element%2 == 1 considering nums[:i]

如果**nums[i]%2 == 0**:
那麼dp[i][0]可以從:
1. dp[i-1][0] + nums[i]轉移過來
2. 但我們也可以花費`x`從dp[i-1][1] + nums[i] - x轉移過來

所以`dp[i][0] = max(dp[i-1][0] + nums[i], dp[i-1][1] + nums[i] - x)`

至於dp[i][1]則只能從dp[i-1][1]轉移過來, 因為我們規定dp[i][1]為最後一個挑選元素的parity為1

同理, 如果**nums[i]%2 == 1**:
那我們就能更新dp[i][1]並且一樣有兩種決策

那狀態轉移方程則為:

```py
if nums[i]%2 == 0:
    dp[i][0] = max(dp[i-1][0] + nums[i], dp[i-1][1] + nums[i] - x)
    dp[i][1] = dp[i-1][1]
else:
    dp[i][0] = dp[i-1][0]
    dp[i][1] = max(dp[i-1][1] + nums[i], dp[i-1][0] + nums[i] - x)
```