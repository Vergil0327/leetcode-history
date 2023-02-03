# Intuition

要將每個nums[i]依據quantity[j]分配給每個 `j-th` customers，我們那nums裡真正需要關注的是他們的個數（或稱frequency)

所以我們可以先數一下每個數有幾個可以分

```py
count = counter(nums).values()
```

```py
n, m = len(count), len(quantity)
```

其中:
- 最多僅有50個unique values，因此 n <= 50
- 最多就10個客戶，因此 m <= 10

再來就是想要如何分配，每個count[i]，可以分給多個customer的subset
由於最多就10個，因此我們可以透過一個$2^10$的bitmask來表達我們目前滿足了哪幾個customer

`dp[i][bitmask]: 我們是否可以用count[0:i]來滿足當前 bitmask 這些客戶`

由於 n <= 50, m <= 10，因此dp空間僅需要 dp[50+1][2^10]
這邊將i移成1-index，所以開出`50+1`的空間，這樣後續再更新dp[i]跟dp[i-1]的關係時比較好處理邊界

那再來就是考慮如何更新狀態了

對於dp[i][bitmask]來說，dp[i][bitmask]要為`True`的情況為:
1. count[i]滿足 submask of bitmask
2. 前i-1個count(count[0:i-1])滿足count[i]以外的submask，也就是
   - dp[i-1][bitmask-submask] = True

因此最重要的狀態轉移可以寫成
首先遍歷i來看前i個count[0:i]
然後遍歷所有可能bitmask看能不能被count[0:i]滿足

如果`dp[i-1][bitmask] = False`
那就繼續看有沒有什麼submask的組合可以被滿足

那最終答案就是看前n個count是否能滿足所有客戶，滿足所有客戶狀態為`111... = (1<<m) - 1`，因此返回`dp[n][(1<<m)-1]`

```py
for i in range(n+1):
    for bitmask in range(1<<m):
        # 如果dp[i-1][bitmask]為True，那就不用再遍歷submask來判斷了
        if dp[i-1][bitmask]:
            dp[i][bitmask] = True
            continue

        # 遍歷bitmask subset的模板
        submask = bitmask
        while submask:
            if not dp[i-1][bitmask-submask]:
                submask = (submask-1)&bitmask
                continue
            
            if self.canSatisfySubmask(counter[i], quantity, submask):
                dp[i][bitmask] = True
                break
            submask = (submask-1)&bitmask

return dp[n][(1<<m)-1]
```

**Base Case**
再來就是檢查下標有沒有超出範圍，可以看到i=0時dp[i-1]會越界，因此我們改成從1開始，同時bitmask也從1開始

```py
for i in range(1, n+1):
    for bitmask in range(1, 1<<m):
        if dp[i-1][bitmask]:
            dp[i][bitmask] = True
            continue

        # 遍歷bitmask subset的模板
        submask = bitmask
        while submask:
            if not dp[i-1][bitmask-submask]:
                submask = (submask-1)&bitmask
                continue
            
            if self.canSatisfySubmask(counter[i], quantity, submask):
                dp[i][bitmask] = True
                break
            submask = (submask-1)&bitmask
```

那這時i=0跟state=0的base case我們就得單獨處理

首先`dp[i][0]`
對於bitmask為0來說，也就是用前i個來滿足0個customer，因此肯定都為True，所以

```py
for i in range(n+1):
    dp[i][0] = True
```
再檢查一下對於`dp[0][bitmask]`來說，只有當bitmask=0時，才能為True

**Helper Method**
那剩下的就是完成`canSatisfySubmask`這個method了
概念就是當dp[i-1][bitmask-submask]為True的情況下，判斷submask是不是能被當前的count[i]來滿足

但由於這樣python會TLE，因此我們乾脆就把所有可能的submask需要的count都提前處理

```py
masksum = defaultdict(int)
for mask in range(1<<m):
    for i in range(m):
        if (mask>>i)&1:
            masksum[mask] += quantity[i]
```

這樣我們就能透過 `count[i] >= masksum[submask]` 來判斷當前count[i]能不能滿足submask了

# Complexity

- time complexity

$$O(N * 3^M)$$

**為什麼是3^M?**

```py
# 遍歷bitmask subset的模板
for bitmask in range(1, 1<<m):
    submask = bitmask
    while submask:
        print(submask)
        submask = (submask-1)&bitmask
```
ex. 如果 bitmask = 111
那麼這模板會找出所有的submask
submask = 111, 110, 101, 100, 011, 010, 001

對任何bit來說:
1. 可能在bitmask裡且在submask裡
2. 可能在bitmask裡但不在submask裡
3. 不在bitmask裡

不可能不在bitmask裡然後又在submask裡，因此只會有三種狀態，所以是$3^m$
