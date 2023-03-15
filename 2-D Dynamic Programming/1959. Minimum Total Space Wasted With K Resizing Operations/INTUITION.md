# Intuition

這題最重要的突破口是resize的決策在哪

如果我們在第i個位置resize, 那我們就是把它resize成nums[i]
X X X X X X X X [X]
                 i, size = max([X])

如果我們在j位置resize, 那最不浪費容量的大小就是resize成max(nums[j:i]) # j, i both inclusive
X X X X X X X [X X]
               j i, size = max([X X])
X X X X X X [X X X]
             j   i, size = max([X X X])
X X X X X [X X X X]
           j     i, size = max([X X X X])

只要這麼一想，Dynamic Programming的形式就出來了
我們可以這麼定義DP:
**dp[i][j]: the minimum total space wasted considering the array[:i] with j times resize operations**

那狀態轉移也就出來了，我們對於每個nums[i]都往前找`j`然後計算waste space
然後resize的數目從1到K次，同時在不超過K的情況下第i個元素頂多只會有i次可以resize

i = 0 -> 沒必要resize
i = 1 -> 最多就resize一次, nums[0] -> resize -> nums[i]
以此類推

那往回找j的過程中, 最理想最不浪費空間的resize大小肯定是resize成那段區間的最大元素
所以回頭找的時候也能順便求出一個rolling resize = max(nums[j:i])

那既然有了size大小, nums[j:i]這段區間的waste space也就能計算出來了
`waste space = size * (i-j+1) * sum(nums[j:i+1])` where both i and j are inclusive

所以DP轉移如下
```py
for i in range(n):
    for k in range(1, min(i, K)+1):
        maxSize = -inf
        for j in range(i, -1, -1): # the previous time we resize
            maxSize = max(maxSize, nums[j])
            dp[i][k] = min(dp[i][k], dp[j-1][k-1] + maxSize*(i-j+1) - sum(nums[j:i+1]))
return min(dp[n-1])
```

然後我們可以發現`sum(nums[j:i+1])`這個值其實也可以用rolling sum的方式持續求得
```py
for j in range(i, -1, -1): # the previous time we resize
    maxSize = max(maxSize, nums[j])
    accuSum += nums[j]
    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + maxSize*(i-j+1) - accuSum)
```

那最後答案就是`min(dp[n-1])`, 考慮全部n-1個元素並且從所有可能的resize數目中取最小的

**Edge Case & Base Case**

由於我們是要取minimum, 所以dp初始值可以設為inf

```py
n = len(nums)
dp = [[inf]*(K+1) for _ in range(n)]
```

然後我們發現如果j=0的話dp下標中的[j-1]有可能會變-1
所以我們的`j`應該是從`i`往回遍歷到`0`
```py
for j in range(i, 0, -1): # the previous time we resize
    maxSize = max(maxSize, nums[j])
    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + maxSize*(i-j+1) - sum(nums[j:i+1]))
```

- 那這樣會發現`i=0`時不會更新到DP，所以我們`i`從1開始然後`i=0`單獨處理
- 還有k=1時我們會用到dp[k-1]這的值，所以我們也要給k=0時的DP預先處理

i=0時, dp[0][0] = 0, 0次resize，intial size = 0, waste space = 0

再來提前處理k=0的情況, `dp[i][0]`
也就是不resize的情況下的minimum waste space, 處理方式跟上面的dp狀態更新一樣
最佳的size就是那段區間的最大值, 所以:
`dp[i][0] = size * (number of elements) - sum of all the number of elements`

```py
size = SUM = 0
for i in range(n):
    size = max(size, nums[i])
    SUM += nums[i]
    dp[i][0] = size*(i+1) - SUM
```