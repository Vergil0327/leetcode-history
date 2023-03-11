# Intuition

首先很直覺想到我們能組成的可能為 `組成root的個數 = 組成left + 組成right`
所以想法是由小到大來組成一棵樹
然後我們依序把次數疊加起來

首先先對`arr`由小到大排序然後考慮每個數值當作root的可能性

```py
arr.sort()
for i in rnage(len(arr)):
    # logic here
```

對於`arr[i]`來說，我們可以往前找一個可以整除`arr[i]`的因數，並看相對應的因數存不存在
如果存在，那麼組成arr[i]的組合方法為 (# of arr[j]) * (# of arr[i]//arr[j])
左右子樹可以任意搭配組合，所以是乘法

並且我們可以用個`dp`數組來存每個數值的方法數，並且初始值為1

```py
n = len(arr)
dp = [1] * n
for i in rnage(n):
    for j in range(i):
        if nums[i]%nums[j] == 0 and nums[i]//nums[j] in arr:
            dp[i] = dp[j] * dp[idx of nums[i]//nums[j]]
```

由於這邊可以看到我們需要判斷`nums[i]//nums[j]`存不存在，以及必須知道`nums[i]//nums[j]`的index

所以我們可以用一個hashmap `val2idx` 預先先儲存每個`arr[i]`的index

```py
val2idx = {}
for i, v in enumerate(arr):
    val2idx[v] = i
```

所以上面程式碼可改寫尾
```py
n = len(arr)
dp = [1] * n
for i in rnage(n):
    for j in range(i):
        if nums[i]%nums[j] == 0 and nums[i]//nums[j] in val2idx:
            idx = val2idx[nums[i]//nums[j]]
            dp[i] = dp[j] * dp[idx] # 左子樹方法 * 右子樹方法
            dp[i] %= 1000000007
```

那最後答案就是每個可能方法數的總和並對1e9+7取餘數