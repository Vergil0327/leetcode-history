# Intuition

```
X X X [X X X X X X] X
       i        i+k-1
if XOR([i:i+k-1]) == 0 and XOR([i+1:i+k]) == 0, nums[i] must equal nums[i+k]
```

所以我們可以以`k`為循環, {nums[i], nums[i+k], nums[i+2k], ...}都視為同一個group來看
一但我們為了使XOR SUM為0而替換nums[i], 那麼這同個SET裡的數都得替換

SET1 = {nums[i], nums[i+k], nums[i+2k], ...}
SET2 = {nums[i+1], nums[i+1+k], nums[i+1+2k], ...}
...

這題最重要的是, 其實我們只要關注這k個group即可
並且目的是最終這k個group的XOR sum為0

再來就是個小技巧, 看constraint能不能有些提示
`k <= n <= 2000`且nums[i] < 2^10 -> O(k * 2^10) ~ 1e6級別, 這是可接受的時間複雜度

所以我們往這方面去想
我們定義`dp[i][j]`是對於前`i`個SET來說, 如果我們要使其的XOR SUM為`target`的最小次數
照這定義, 最終答案就是`dp[k-1][0]`, 總共K個set的XOR SUM為0的最小次數

遍歷全部可能的值為1024, 是因為我們要求的是前面k-1個SET再加上最後一個SET後為0
所以前面k-1個SET的XOR SUM並不確定是多少, 所以全部遍歷一遍

那這樣狀態轉移會是

```py
for i in range(k):
    for t in range(1024): # 前i個SET的XOR sum 為target
        for v in rnage(1024):
            # 當前的SET替換成v, 那麼前i-1個SET的XOR sum必須為 v^t, 這樣 (v^t) ^ v = t = 當前 XOR sum
            dp[i][t] = min(dp[i][t], dp[i-1][v^t] + cost) where cost = make all the number in SET[i] be v
```

再來就是如何改善時間複雜度

```py
for v in rnage(1024):
    dp[i][t] = min(dp[i][t], dp[i-1][v^t] + cost) where cost = make all the number in SET[i] be v
```

上面這段, 由於計算的cost跟SET有關, 這時如果分成兩種情況討論
- v 在SET裡: cost = total count of SET[i] - count of v in SET
- v 不在SET裡: cost = total count of SET[i] - 0

但v不管在不在SET裡, 都可以透過這個式子來算, `totalCount[i] - count[i][v]`

所以原狀態轉移可寫成以下pseudo code

```py
for i in range(k):
    for t in range(1024): # 前i個SET的XOR sum 為target
        # v not in set
        for v not in SET[i]:
            dp[i][target] = dp[i-1][v^target] + totalCnt[i]

        # v in set[i]
        for j in range(i, n, k):
            v = nums[j]
            dp[i][target] = min(dp[i][target], dp[i-1][v^target] + totalCnt[i] - count[i][v])
```

對於所有不在set的v, 由於後面加上的cost是個constant, 所以它們的dp[i][target]其實就是從前`i-1`個dp裡找最小即可
所以可以提前算出來

```py
for i in range(k):
    minCost = inf # dp[i-1][target]
    x = None
    for target in range(1024):
        if dp[i-1][target] < minCost:
            minCost = dp[i-1][target]
            x = target

    for target in range(1024): # 前i個SET的XOR sum 為target
        # v not in set[i]
        # dp[i][target] = dp[i-1][x] + totalCnt[i]
        # dp[i][target] = minCost + totalCnt[i]
        dp[i][target] = minCost + totalCnt[i] - count[i][v]
        

        # v in set[i]
        for j in range(i, n, k):
            v = nums[j]
            dp[i][target] = min(dp[i][target], dp[i-1][v^target] + totalCnt[i] - count[i][v])
return dp[k-1][0]
```

`dp[i][target] = minCost + totalCnt[i]`這個表達式的前提是我們當前替換的v不在SET[i]時才成立
但`dp[i][target] = minCost + totalCnt[i]  - count[i][v]`是對所有的v都成立

所以對於v not in set[i]的情況, 由於我們為了免去遍歷所有的不在set[i]的v, 所以我們用第二種表達式來cover這部分的更新
如此一來就能免去一個循環

再來注意edge case
我們`i`從1開始遍歷來避免dp[i-1]越界, `i=0`就提前處理

對於dp[0][target] where 0 <= target <1024
就看Set[0]裡的數替換成的target的cost是多少即是

# Complexity

- time complexity
$$O(k * (1024 + 1024 * n/k))$$
