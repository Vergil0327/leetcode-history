# Intuition

一開始直覺想到的是top-down DP, 但會MLE
所以這條路行不通, 得換個思路走

```py
def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
    mod = 10**9 + 7
    index1 = {v: i for i, v in enumerate(nums1)}
    index2 = {v: i for i, v in enumerate(nums2)}
    n, m = len(nums1), len(nums2)

    @lru_cache(None)
    def dfs(i, j, isNums1):
        if i == n or j == m: return 0
        if isNums1:
            res = dfs(i+1, j, isNums1)
            if nums1[i] in index2:
                res = max(res, dfs(i, index2[nums1[i]]+1, not isNums1))
            res += nums1[i]
            return res
        else:
            res = dfs(i, j+1, isNums1)
            if nums2[j] in index1:
                res = max(res, dfs(index1[nums2[j]]+1, j, not isNums1))

            res += nums2[j]
            return res
    
    return max(dfs(0,0, True), dfs(0,0, False))%mod
```

因此我們再仔細看一下nums1跟nums2

我們可以把nums1跟nums2分成各個區間, 每個common value其實就是一個分岔點
分岔點跟分岔點間的區間, 我們其實就是取大的那條路走

下面這個例子很明顯的就是先走上再往下走然後再往上再往下
```
nums1 = [XXXXXXXX]O[XX]O[XXXXX]O[X]
nums2 = [YYY]O[YYYYYY]O[YYY]O[YYY]

res = [XXXXXXXX] + O + [YYYYYY] + O + [XXXXX] + O + [YYY]
```

所以我們先找出common value的所在位置, 並儲存在一個queue裡
然後再透過雙指針算出每個common value間的區間個別的sum1, sum2是多少
取`max(sum1, sum2)`並加至我們的答案即可
```py
index1 = {v: i for i, v in enumerate(nums1)}
index2 = {v: i for i, v in enumerate(nums2)}
n, m = len(nums1), len(nums2)

common = deque()
for i in range(n):
    if nums1[i] in index2:
        common.append(nums1[i])

i = j = 0
res = sum1 = sum2 = 0
while common:
    num = common.popleft()
    ii = index1[num]
    jj = index2[num]
    while i <= ii:
        sum1 += nums1[i]
        i += 1
    while j <= jj:
        sum2 += nums2[j]
        j += 1

    res = (res + max(sum1, sum2))%mod
    sum1 = sum2 = 0
```

別忘了走完最後一個common value後, 還要算上最末尾的那段區間
```py
while i < n:
    sum1 += nums1[i]
    i += 1
while j < m:
    sum2 += nums2[j]
    j += 1
res = (res + max(sum1, sum2))%mod
```

# Optimization

但其實這題nums1, nums2都是由小到大排序的
所以其實我們可以不用先求出`index1`, `index2` hashmap
我們借用merge sort的merge step的概念, 直接用雙指針移動即可

一但一方走到盡頭, 就只能走另外一邊
一但一方的值比較小, 就移動該值
直到雙方的值相等時, 代表我們走到了common value的位置
我們將較大的區間加至`res`後並重置`sum1`, `sum2`並繼續移動雙指針

```py
while i < n or j < m:
    if j == m:
        sum1 += nums1[i]
        i += 1
    elif i == n:
        sum2 += nums2[j]
        j += 1
    elif nums1[i] > nums2[j]:
        sum2 += nums2[j]
        j += 1
    elif nums1[i] < nums2[j]:
        sum1 += nums1[i]
        i += 1
    else: # common value position
        sum1 += nums1[i]
        sum2 += nums2[j]
        i, j = i+1, j+1

        res = (res + max(sum1, sum2)) % mod
        sum1 = sum2 = 0
```

# Complexity

- time complexity
$$O(n+m)$$

- space complexity
$$O(1)$$