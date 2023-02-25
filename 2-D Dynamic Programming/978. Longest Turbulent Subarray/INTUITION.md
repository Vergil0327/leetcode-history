# Intuition

首先想到的是這題可以用Dynamic Programming來解，看起來是基本的DP題求最長合法subarray

由於有兩種情形(如下所示)，因此我們用兩個dp狀態來儲存資訊

dp[i][0]: the length of longest turbulent subarray considering arr[i:] which is first type
dp[i][2]: the length of longest turbulent subarray considering arr[i:] which is second type

```
第一種
- For i <= k < j:
  - arr[k] > arr[k + 1] when k is odd, and
  - arr[k] < arr[k + 1] when k is even.

# 第二種
- Or, for i <= k < j:
  - arr[k] > arr[k + 1] when k is even, and
  - arr[k] < arr[k + 1] when k is odd.
```

那我們可以明顯看到arr[k]依賴於arr[k+1]，因此可以想到我們必須從後面往前遍歷
並且在符合情況時:

`dp[i] = dp[i+1]+1`

因此可以推出:

```py
for i in range(n-1, -1, -1):
    if i%2 == 0:
        if arr[i] < arr[i+1]:
            dp[i][0] = dp[i+1][0] + 1
        elif arr[i] > arr[i+1]:
            dp[i][1] = dp[i+1][1] + 1
    else:
        if arr[i] > arr[i+1]:
            dp[i][0] = dp[i+1][0] + 1
        elif arr[i] < arr[i+1]:
            dp[i][1] = dp[i+1][1] + 1
```

並且且注意arr[i]跟arr[i+1]的關係必須是嚴格大於或嚴格小於才行

再來注意邊界條件跟base case

首先base case:

因為每個元素基本的長度為1，所以dp[i][0]跟dp[i][1]的初始值為`1`

`dp = [[1, 1] for _ in range(n+1)]`

再來邊界條件可以看到當`i`等於`n-1`時，arr[i+1]會越界
因此我們可以在arr的最後加上一個跟arr[n-1]一樣的數，由於必須嚴格大於或嚴格小於才符合turbulent subarray的條件，因此加上一個一樣的數不會誤算turbulent subarrary的長度

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$