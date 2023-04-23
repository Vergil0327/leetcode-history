# Intuition

這題當初在解的時候，首先想到的是

如果nums裡面已經有`1`存在的話, 任何數跟1的gcd都是1
所以操作數就是看剩下有多少個不為`1`的數，即為所需操作數

```py
if 1 in set(nums):
    return len([num for num in nums if num != 1])
```

再來想的是就是怎樣才會不可能有解?
仔細觀察example 2可得知最重要的一個關係式

如果整個區間的每個數的共同gcd不為1的話，那肯定無解

```py
GCD = gcd(nums[0], nums[1])
for i in range(1, n-1):
    GCD = gcd(GCD, gcd(nums[i], nums[i+1]))

if GCD > 1: return -1
```

所以整個區間的`GCD>1`的話, 那我們肯定找不到一個可以將nums[i]轉變為1的操作

再來就是想到有沒有辦法用binary search來找最佳解
框架如下:

```py
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

如果我們能找到一個`check` helper function來判斷當下個`mid`是不是個可行的操作數
那就可以透過binary search來解

這個`check`首先想到的是能不能用Greedy的方式來判斷可不可行
這時會發現其實我們要找的就是一個最小的區間其整個區間的每個數都用上後, GCD為1
`GCD = gcd(GCD, gcd(nums[i], nums[i+1]))`


假如這個區間可以這麼轉換的話，並且他為最小區間的話
那麼他的所需操作數為`2*length-2`
```
[{X X} X]    -> {X,X} gcd為Y
[X  {Y  Z}]  -> {Y,Z} gcd為1
[X  {Y  1}]  -> 把剩下轉為1
[X  1  1]
[1  1  1]
```

可以再看一下這個例子, 如果最小可以找到gcd=1的區間, 長度為2的話
`operations = 2*length-2`
```
[X X]
[X 1]
[1 1]
```

那再來剩下多少個數就須額外加上多少操作數
nums = X X X X X X [X X X X X X] X X X X X X X
                    i         j
operations = 2*(j-i+1)-1 + 左半邊 + 右半邊
           = 2*(j-i+1)-1 + i + (n-1-j)

所以我們的`check` helper function為:

我們區間的長度從2開始遍歷, 最多到mid, 如果超過mid那肯定無法將整個區間轉為1
因為我們已經在前面這行排除掉有1的情況了, 在操作數為`2*length-2`的情況下
再怎樣都不可能可以再利用`mid`次操作下將長度超過`mid`的subarray全轉為1
```py
if 1 in set(nums):
    return len([num for num in nums if num != 1])
```

我們從小區間遍歷到大區間，一但找的一個區間其`GCD=1`時
我們就計算看需要多少操作數, 最終判斷操作數 <= mid, 代表mid為可行解

```py
def check(mid):
    found = False
    res = -1
    for length in range(2, mid+1):
        for i in range(n-length+1):
            j = i+length-1
            GCD = nums[i]
            for k in range(i, j+1):
                GCD = gcd(GCD, nums[k])
                if GCD == 1:
                    found = True
                    break
            if found:
                res = 2*length-2 + i + (n-1-j)
                break
        if found:
            break
    return res <= mid
```

但由於二分的上界, 看不出是多少
所以這邊我是隨意用個相對大的數2^32次方

# Other Solution

但仔細看會發現, 其實我們`check` helper function已經是Greedy Solution了
無需再用二分法來找答案

[詳細見這篇](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/3445739/simple-observations-an-age-old-codeforces-problem/)

所以其實我們僅需要討論
1. nums有1的情況
2. nums沒有1的情況

如果是第一種情況, 我們可以計算一下`1`的個數
```py
n = len(nums)
counter = Counter(nums)
if counter[1] > 0: return n-counter[1]
```

再來討論第二種情況
我們一樣用$O(n^2)$時間找出`gcd=1`的最小區間
```
nums = X X X X X X X X X X X
       l               r->
```

所們持續計算區間的GCD, 一但`GCD=1`這時所需的操作數為
```
{X X} X X
X {Y X} X
X Y {Z X}
X Y Z 1   -> 這時所需操作數為 r-l
          -> 再來從1開始往外擴散, 整個長度為n的nums需要n-1次操作
          -> 所以總操作為: r-l+(n-1)
```

```py
res = inf

for l in range(n):
    GCD = nums[l]
    for r in range(l+1, n):
        GCD = gcd(GCD, nums[r])
        if GCD == 1:
            res = min(res, r-l+(n-1))
return res if res != inf else -1
```

# Complexity

- time complexity

$$O(n^2)$$