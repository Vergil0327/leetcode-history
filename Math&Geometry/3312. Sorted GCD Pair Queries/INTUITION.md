# Intuition

一般來說都是考慮遍歷queries, 然後再以O(logn)或O(1)去查詢解答
或是處理nums的過程中去回填queries[i]的解答

這題得注意到`nums[i] <= 5 * 10^4`這條件, 會發現我們其實是可以遍歷nums[i]的
對於所有GCD, 其範圍肯定落在`[1, max(nums)] <= 5*10^4`
所以如果我們可以遍歷所有可能的GCD `g`, 並知道其個數的話, 最後我們就能利用binary search去找個數大於queries[i]的元素是什麼

ex. example 2
Input: nums = [4,4,2,1], queries = [5,3,1,0]

gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4]
相當於: g=1有3個, g=2有2個, g=4有1個
g     = [1, 2, 4]
count = [3, 2, 1]
這時我們再將個數化成prefix sum
pre_count = [3, 5, 6]

我們就能利用binary search找出k-th element
例如: queries[0]要找的是gcdPairs的gcdPairs[5]
所以就是跳過前5個後的下個元素, `bisect_right(pre_count, queries[0]) = 2` => 答案就是g[2] = 4

主要框架如下:

```py
res = []
for q in queries:
    i = bisect_right(pre_count, q)
    res.append(g[i])
return res
```

那再來就是pre_count跟g要怎麼預處理

1. countD[d]: number of (i) with nums[i] % d == 0
首先先看每個nums[i]對divisor所貢獻的個數是多少


```py 
MX = 50001
divisors = [[] for _ in range(MX)]
for x in range(1, MX):
    for y in range(x, MX, x):
        divisors[y].append(x)

countNum = Counter(nums)

countD = Counter()  # countD[d]: number of (i) with nums[i] % d == 0
for num, freq in countNum.items():
    for d in divisors[num]:
        countD[d] += freq
```

再來就能遍歷`[1, max(nums)]`這範圍, `countD[g]`代表有多少數有g這個因數
任選兩個作為pair的個數為`countG[g] * (countG[g] - 1) // 2`
但這些是還有包括g的倍數, 也就是這些個數代表的是: **gcd(nums[i], nums[j]) == g, g*2, g*3, ...**
所以還得扣掉dupliate, 留下**exactly gcd(nums[i], nums[j]) == g**

```py
countG = Counter()  # countG[g]: number of (i < j) with gcd(nums[i], nums[j]) == g
for g in range(mx, 0, -1):
    c = countD[g]
    if c <= 1:
        continue

    countG[g] = c * (c - 1) // 2
    countG[g] -= sum(countG[x] for x in range(2 * g, mx + 1, g))
```

那有了countG後, 我們也就擁有我們要的最終gcdPairs list了

```py
gList = []
vList = []
for g, v in reversed(countG.items()):
    gList.append(g)
    vList.append(v)
presum = list(accumulate(vList))

res = []
for q in queries:
    i = bisect_right(presum, q)
    res.append(gList[i])
return res
```