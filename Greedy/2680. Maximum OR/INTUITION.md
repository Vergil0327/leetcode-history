# Intuition

剛開始是想說用dp來解, `*=2`相當於bit左移一位`<<=1`
由於不知道要移哪個, 所以我們每個`nums[i]`都移看看, 最多移`k`次

定義dp[i][k]: the maximum or result by shift k times totally considering first i elements

那麼當前如果操作k次, 上一次操作prevk次, 那麼這次就能左移`k-prevk`次
所以狀態轉移可以很快的寫出以下式子:

```py
n = len(nums)
nums = [0] + nums
dp = [[0]*(K+1) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(K+1):
        for prevk in range(k+1):
            dp[i][k] = max(dp[i][k], dp[i-1][prevk] | (nums[i]<<(k-prevk)))
        
return dp[n][K]
```

但這樣會TLE
實際上這題需要想到一個貪心解(Optimal way)

由於我們每次操作可以`*=2`, 也相當於`<<=1`
那最佳策略肯定是把所有操作用在某個`nums[i]`上, 這樣左移最多, `num[i]`形成的值也最大
然後再將`nums[i]<<k`與其他數進行**OR**操作, 然後求出全局最大OR

```py
n = len(nums)
res = 0
for i in range(n):
    curr = nums[i]<<k
    for j in range(i):
        curr |= nums[j]
    for j in range(i+1, n):
        curr |= nums[j]
    res = max(res, curr)
return res
```

其中可以用prefix OR sum來替代`OR_SUM(nums[:i])`
```py
# for j in range(i):
#     curr |= nums[j]
curr |= prefix[i]
```

並用suffix OR sum來替代`OR_SUM(nums[i+1:])`
```py
suffix = [0] * (n+1)
for i in range(n-1, -1, -1):
    suffix[i] = suffix[i+1] | nums[i]

# for j in range(i+1, n):
#     curr |= nums[j]
curr |= suffix[i+1]
```