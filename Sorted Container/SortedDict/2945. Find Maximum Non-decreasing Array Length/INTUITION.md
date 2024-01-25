# Intuition

```
X X {X X X X} {X X X}
           j       i
```

一個non-decreasing subarray, 中間某些數可能是多個小subarray的和

由於必須non-decreasing, 如果我們定義:
dp[i]: the last subarray sum element ending at i

那麼當dp[i] >= dp[j]時, 可更新length[i] = length[j]+1
其中length[i]: 到`i`為止的合法最長長度

所以如果brute force的話會是兩層循環, 外層`i`, 內層找`j`

而且在dp[i]前的dp[j]肯定越小越好, 這樣後面才會有更高機率皆得更長
想法有點像是LIS的O(nlogn) Greedy解法
所以我們找到的第一個合法dp[j]後就可以更新我們的dp[i]
```py
for i in range(1, n+1):
    _sum = nums[i] # 1-indexed
    j = i-1
    while j >= 0 and _sum < dp[j]:
        _sum += nums[j]
        j -= 1

    dp[i] = _sum
    length[i] = length[j]+1
return length[n]
```

那再來就是要想優化的部分

由於我們要找的是: _sum >= dp[j], 其中_sum = presum[i]-presum[j]

所以可寫成: `presum[i]-presum[j] >= dp[j]`
調換一下把同項放在一起即得: `presum[i] >= presum[j]+dp[j]`

其中會發現對於i-th element來說, presum[j]跟dp[j]都會是已知
所以其實我們可以用個Sorted Map來紀錄: `{presum[i]+dp[i]: i}`

這樣我們就能用binary search **bisect_right**來找出這個位置, 找完後記得更新這個Sorted Map

但要注意更新時, 必須維護這個Sorted Map的**value**是單調遞增的, 因為

MAP = {key1: index1, key2: index2, ...}

如果今天更新`MAP[presum[i]+dp[i]] = i`
那們所有key >= presum[i]+dp[i]位置的都必須移除掉, 因為在同樣都為合法條件下, 當前的length[i]必定大於等於length[key], 所以我們保留MAP[presum[i]+dp[i]]就好

time: O(nlogn)

這題最重要的就是維護presum[i]+dp[i]的單調性質
所以其實也可以用monotonically increasing stack來做
找到的第一個就是我們要找的dp[j]
時間複雜度可壓到**O(n)**

```py
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        stk = [(0, 0, 0)]  # last + pre, pre, dp

        presum, res = 0, 0
        i = j = 0
        while i < n:
            presum += nums[i]
            j = min(j, len(stk) - 1)

            while j + 1 < len(stk) and presum >= stk[j + 1][0]:
                j += 1
            (val, pre_presum, pre_dp) = stk[j]
            res = curr_dp = pre_dp + 1

            last = presum - pre_presum
            while len(stk) > 0 and stk[-1][0] >= last + presum:
                stk.pop()
            stk.append((last + presum, presum, curr_dp))
            i += 1
        return res
```