# Intuition

首先能很直覺想到的是$O(n^2)$的DP解法

想法是
dp[i]: the maximum number of non-empty non-overlapping subarrays ended at `i` index

X X X X X X X [X X X X]
               j     i

狀態轉移就是往前找一個j使得nums[j:i]這個subarray的sum[j:i] == target
dp[i] = max(dp[i], dp[j-1] + 1) if sum[j:i] == target

再來dp[i]也有個基本值，那就是`dp[i] = dp[i-1]`，就算當前沒能組成合法subarray
至少也有先前的`dp[i-1]`個合法subarray

另外由於我們要判斷區間和，所以可以預先處理prefix sum

但由於從數據規模看來，$O(N^2)$是不行的
看起來必須是O(N)或頂多O(NlogN)，這樣看來可能是有什麼Greedy的解法或是更好的決策

X X X X X X X [X X X X]
      j        j     i

由於我們要找的是non-overlapping subarray，那這樣我們盡可能的去組成合法的subarray肯定是比較好的
所以我們不用每次都往前遍歷到底去找，我們的j只要找最靠後的那個位置即可

所以我們可以把原狀態轉移改一下, 由於`presum[i]-presum[j-1] = target`
所以 `presum[j-1] = presum[i] - target`

我們用個hashmap `seen` 來記錄每個presum的最新(最靠後)的index
如果找到presumJ，就代表找到一段區間能組成sum為target的合法subarray，因此能進行狀態轉移

最後有個很重要的一點是hashmap `seen` 的初始值
由於如果sum(nums[:i]) == target, 前i個和就已經是target的時候，我們必須找一個presumJ為0的index
所以我們的hashmap必須提前加入base case seen = {0: 0}

*p.s. 因為我已經轉成1-indexed 所以seen[0] = 0*

```py
dp = [0] * (n+1)
seen = {0: 0}
for i in range(1, n+1):
    dp[i] = dp[i-1]
    presumJ = presum[i] - target
    if presumJ in seen:
        dp[i] = max(dp[i], dp[seen[presumJ]]+1)
    
    seen[presum[i]] = i
    # for j in range(1, i+1):
    #     if presum[i]-presum[j-1] == target:
    #         dp[i] = max(dp[i], dp[j-1] + 1)
```