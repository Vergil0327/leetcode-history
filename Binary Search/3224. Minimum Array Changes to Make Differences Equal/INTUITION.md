# Intuition

首先我們能找出可能的X:

```py
countX = defaultdict(int)
for i in range(n//2):
    x = abs(nums[i] - nums[n-i-1])
    countX[x] += 1
```

再來目標是遍歷所有可能X, 然後有以下3種可能:
1. 本身已是合法pair: 這在尋找X的時候能順便求出
2. 可以更改pair其中一邊來達到min(nums[i] - nums[n-i-1]) == x
3. 必須更改pair兩邊來達到min(nums[i] - nums[n-i-1]) == x

透過constraint得知: `0 <= nums[i] <= k <= 10^5`
代表每一個invalid pair都可以透過1次(至多2次)操作使得`abs(nums[i], nums[n-i-1]) == x`
所以我們目標是要能高效求出有多少pair是兩邊都要更換的才能滿足abs(nums[i] - nums[n-i-1]) == x

首先我們看(nums[i], nums[n-i-1]) pair:

我們令a < b => a, b = min(nums[i], nums[n-i-1]), max(nums[i], nums[n-i-1])
因此根據定義, `x = abs(nums[i] - nums[n-i-1]) = b-a`

對於1次操作來說, 我們能滿足的**X**範圍上限為:
1. 將a變為0: x = b-0 = b
2. 將a變為k: x = k-a

代表透過一次操作, (nums[i], nums[n-i-1]) pair能涵蓋的範圍為 [0, max(b, k-a)]
這時我們將每對pair都找出上限並排序的話, 那麼我們在遍歷可能**X**的過程中:

1. 我們能透過`n//2 - countX[x]`得知invalid pair的數目, 這些至少需要1次操作
2. 我們在透過binary search去搜索**X**, 對於那些涵蓋上限小於**X**的pair來說, 代表他們需要兩次操作才能使pair合法

因此兩者數目相加, 就是對於**X**來說, 所需要的操作數
我們取全局最小即可

```py
for x in countX.keys():
    invalid = n//2 - countX[x]
    cntChange2 = bisect_left(change1Threshold, x)

    res = min(res, invalid + cntChange2)
```