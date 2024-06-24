# Intuition

依據題意, 我們要再滿足所有requirements的前提下, 求 **the number of permutations perm of [0, 1, 2, ..., n - 1] such that for all requirements[i], perm[0..endi] has exactly cnti inversions**
    
目的是求合法permutations數目, 數據規模也至少能O(n^3) < 10^6, 可往dynamic programming方向去想

首先先照著要求的東西去定義: dp[i][j]: the number of permutations of array with length `i` and inversions `j`

```
perms = {X X X X X X X} X
```

再來看狀態轉移, 我們由小到大每加入一個新的`X`, 依據插入位置不同分別會得到相對應的`index`個inversion
ex. {1,2,3,4} + 5 => {5,1,2,3,4}, {1,5,2,3,4}, {1,2,5,3,4}, ...

依照這思想的話, dp[i]只跟dp[i-1]有關, 並且隨著當前插入位置不同去更新inversions數: `dp[length][inversions+inserted_pos] += dp[length-1][inversions] for inserted_pos in range(length)`
所以為了更新整個dp[i][j], 我們遍歷所有可能的`length`跟`inversion`跟插入位置`pos`去更新dp[i][j]

```py
for length in range(1, n+1):
    for inversions in range(maxCnt+1):
        if dp[length-1][inversions] == 0: continue

        for pos in range(length):
            dp[length][inversions+pos] += dp[length-1][inversions]
            dp[length][inversions+pos] %= mod
```

但要特別注意, 我們這樣求出來的, 是`the number of permutations of array with length i and inversion j`而已
我們還得滿足所有**requirements**, 對於那些不符**requirements**的方法數, 都是不合法的, 所以我們還得再遍歷一遍, 將不合法的方法數設為**0**

```py
for length in range(1, n+1):
    for inversions in range(maxCnt+1):
        if dp[length-1][inversions] == 0: continue

        for pos in range(length):
            dp[length][inversions] += dp[length-1][inversions+pos]
            dp[length][inversions] %= mod

    # check requirements
    for endIdx, cnt in requirements:
        if (size:=endIdx+1) == length:
            for inv in range(maxCnt+1):
                if inv != cnt:
                    dp[length][inv] = 0
```

那這樣最後答案就是`sum(dp[n])`