# Intuition

```
O O O O O O O O O O O O

~after k merges~

O X X O O X X X O X X O
```

dp[i][j]: the minimum travel time with j consecutive merges at i considering position[:i]

```py
for i in range(n):
    for j in range(i-1, max(0, i-1-K), -1):
        dp[i][j] = min(dp[i][j], dp[j-1][K-(i-j)])
```

但上面這樣永遠都只考慮K次合併都落在i-th以及j-th元素上
但有可能在更早之前就已經用完K次合併

所以我們應該還要再遍歷, 當前還剩下幾次合併, 因此定義

dp[i][j][k]: the minimum travel time with j consecutive merges at i and remain `k` merges considering position[:i]

然後我們改成top-down寫法個人感覺更直覺一點:

定義: dfs(i, k, merge_start_idx): the minimum travel time at i with k merges remain and previous merge position is `merge_start_idx` which means we merge `merge_start_idx, merge_start_idx+1, merge_start_idx+2, ..., i-1, i` together.

then we have:

```py
def dfs(i, k, merge_start):
    if i == n-1:
        return 0 if k == 0 else inf

    rate = sum(time[tt] for tt in range(merge_start, i+1))
    res = inf
    for next_pos in range(i+1, min(n-1, i+1+k)+1):
        merges = next_pos - i - 1
        distance = position[next_pos] - position[i]

        res = min(res, dfs(next_pos, k - merges, i+1) + distance * rate) # merge {i+1, i+2, ..., next_pos-1} with next_pos
    return res
```

# Complexity

time: O(k * n * k * n)
space: O(n * k * n)