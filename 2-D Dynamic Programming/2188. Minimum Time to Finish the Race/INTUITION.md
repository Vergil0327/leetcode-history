# Intuition

至少得想到這是個DP題，我們可以這樣來想，我們這樣定義dp:

dp[i]: the minimum time to finish i laps

由於我們的決策是輪胎跑幾圈的時候要換，所以我們考慮最近一次我們的輪胎跑了幾圈就好
這樣一想，狀態轉移就清楚了

由於不知道輪胎在i圈裡要用幾圈才合適，所以我們遍歷一遍取最佳:
```py
for i in range(1, numLaps+1):
    for j in range(1, i+1):
        if j == i:
            dp[i] = min(dp[i], dp[i-j] + minimumTimeToFinish(j))
        elif j < i:
            dp[i] = min(dp[i], dp[i-j] + changeTime + minimumTimeToFinish(j))
```    

我們考慮最後一個輪胎用了`j`圈, 如果`j==i`，那代表我們最後一個輪胎跑了完整的`i`圈沒有更換，所以不需要changeTime

如果`j<i`，代表我們有更換過一次，所以加上`changeTime`

所以我們欠缺的就是`minimumTimeToFinish(j)`
我們可以預先處理求出每個輪胎跑j圈所需要的時間，並且從中取最短時間的用

minTime放的是跑完`lap`圈所需花費的最短時間
這代表我們要遍歷每一圈並累加看跑`lap`圈每個輪胎要花多少時間，我們選最佳的
這邊的totalTime(i, lap)算的是: 對於第`i`種輪胎來說，跑完`lap`圈所需要花費的時間
```py
minTime = [inf] * (numLaps + 1)
for lap in range(1, numLaps+1):
    for i in range(n):
        minTime[lap] = min(minTime[lap], totalTime(i, lap))

# 公比級數為: f * r^(x-1)
# 因此公比級數的和為: f * (r**(x-1))//(r-1)
def totalTime(tire, lap):
    f, r = candidateTires[tire][0], candidateTires[tire][1]
    # f * r^(lap-1)
    # f * r^0 + f*r^1 + f*r^2 + ... + f*r^(lap-1)
    return f * (r**lap-1)//(r-1)
```

因此預處理加上狀態轉移後則為:

```py
for i in range(1, numLaps+1):
    for j in range(1, i+1):
        if j == i:
            dp[i] = min(dp[i], dp[i-j] + minTime[j])
        elif j < i:
            dp[i] = min(dp[i], dp[i-j] + changeTime + minTime[j])
```

**Base Case**

由於是要取minimum time, 所以初始值我們可以設inf
dp = [inf] * (numLaps + 1)

其中由於i會等於j, 代表我們會需要用到dp[0], 對於dp[0]這個base case則為:
dp[0] = 0
他所代表的是，跑零圈時需要花費的時間，那就是0

# Optimized

那這邊可以optimize的地方有兩個

1. 首先是輪胎

我們可以觀察一下輪胎，發現其實有先輪胎其實性能很差，完全可以被另外一個替代
對於f * r^(x-1)來說，要麻f很小，不然就是r要很小
以現實來講就是一個是硬胎跑得慢但比較耐久、另一個是軟胎跑得快磨損快

所以我們可以對輪胎以`r`做排序，然後我們`f`找一個單調遞減的序列
由於排過序，因此當前這個輪胎`r`值一定比前一個大，這時如果他的`f`值也比較大，那就完全可以被前一個取代
因此我們完全沒必要考慮他
如果`f`值比前一個小，那才有所差異，才有機會用
所以我們可以用這個概念先淘汰掉一些輪胎

```py
tires.sort(key=lambda x:x[1])
candidateTires = []
for tire in tires:
    if not candidateTires:
        candidateTires.append(tire)
    elif tire[0] < candidateTires[-1][0]:
        candidateTires.append(tire)
```

2. 第二點是我們可以觀察一下 `f * r^(x-1)`這個公式

由於changeTime最多就`10^5`
那`f * r^(x-1)`又是個指數級別的公式，這代表如果`f * r^(x-1)`大於changeTime的上限的話
我們沒理由繼續使用，肯定是換胎比較好

由於`r`最小值為2, 2的20次方就會超過`10^5`, 也就是會超過changeTime的上限了
因此代表其實`x`上限最多就20，每個輪胎最多只會跑20圈，再多肯定是更換會更好
所以在內層遍歷的`j`可以加上個上限`min(20, i)`

同時也代表我們的minTime最高也只需要計算到20圈即可

```py
minTime = [inf] * (numLaps + 1)
for lap in range(1, min(20, numLaps)+1):
    for i in range(n):
        minTime[lap] = min(minTime[lap], totalTime(i, lap))


dp = [inf] * 1001
dp[0] = 0
for i in range(1, numLaps+1):
    for j in range(1, min(20, i)+1):
        if j < i:
            dp[i] = min(dp[i], dp[i-j] + changeTime + minTime[j])
        elif j == i:
            dp[i] = min(dp[i], dp[i-j] + minTime[j])

return dp[numLaps]
```