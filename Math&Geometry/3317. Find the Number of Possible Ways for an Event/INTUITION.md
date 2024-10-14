# Intuition

每個stage有`pow(y, stage, mod)`種分數
如果我們直接將`n`分配到`x`個stages, 可能會有些stage為空舞台, 這樣不好計算後續每個stage的分數可能性

所以我們遍歷所有非空stage的可能性再加總起來:
1. 首先先從`x`個stages中取出`non_empty_stage for non_empty_stage in range(1, min(n, x)+1)`個非空stage => 組合數 C(x,non_empty_stage)
2. 再來每個stage的評分有`y`種, 所以舞台分數的可能性為: `comb(x, non_empty_stage) * pow(y, non_empty_stage, mod)`
3. 剩下就計算`n`個表演者分配到`non_empty_stage`有多少可能性
   - 將`n`個物品分配到`k`個非空集合 => 數學上有個名詞叫做`stirling number`
   - **stirling number**的關係式為: dp[n][k] = k * (dp[n-1][k] + dp[n-1][k-1])
     1. 當前performer分配到`k`個舞台中任一 => k * dp[n-1][k]
     2. 當前performer分配到`k`個舞台中任一後, 拿掉該舞台 => k * dp[n-1][k-1]
     3. 當前分配情況為兩種情況加總

主框架如下
```py
res = 0
for non_empty_stage in range(1, min(n, x)+1):
    # there are `non_empty_stage` stages containing 1 performers at least
    stage_scores = comb(x, non_empty_stage) * pow(y, non_empty_stage, mod)
    
    res += dfs(n, non_empty_stage) * stage_scores
    
return res%mod
```

### stirling number

```py
# top-down
@cache
def dfs(n, s):
    """
    distribute `n` performers to `s` non-empty stage => stirling number
    """
    if n < s: return 0 # 不可能將`n`表演者分配到全部舞台
    if s == 1: return 1 # 剩一個舞台, 只剩一種分配方式

    # 1. distribute to current stage: s choices => s * dfs(n-1, s)
    # 2. distribute to current stage and exclude that stage: s choices => s * dfs(n-1, s-1)
    return (s * dfs(n - 1, s) + s * dfs(n - 1, s - 1)) % mod

# bottom-up
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[0][0] = 1
for n in range(1, 1001):
    for x in range(1, n + 1):
        dp[n][x] = x * (dp[n - 1][x] + dp[n - 1][x - 1]) % mod
```