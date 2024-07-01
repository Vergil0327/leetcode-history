# Intuition

首先想到的brute force方式是:
1. 我們將所有可能的modulo pair找出來, 如果m = (subseq[i]+subseq[i+1])%k
2. 然後再依照順序找出subsequence

```py
n = len(nums)

arr = [num%k for num in nums]

res = 0
possiblePairOrder = defaultdict(set)
for i in range(k):
    for j in range(k):
        possiblePairOrder[(i+j)%k].add((i, j))

for orders in possiblePairOrder.values():
    for order in orders:
        cnt = orderIdx = 0

        for num in arr:
            if num == order[orderIdx]:
                cnt += 1
                orderIdx = (orderIdx+1)%2
                res = max(res, cnt)
return res
```

順著上述思緒:
m = (nums[i]+nums[i+1])%k
m = (nums[i+1]+nums[i+2])%k
=> nums[i]%k = nums[i+2]%k = (m-nums[i+1])%k

所以對於(nums[i+1]%k)來說, 他能接在nums[i]之後, 也就是接在(m-nums[i+1])%k後
所以我們可以這麼定義dp: dp[nums[i]%k][m]: the longest valid subseq. ended with modulo `m` and nums[i]

那麼狀態轉移也很明顯了:
dp[nums[i]%k][m] = dp[prevNum][m] = dp[(m-nums[i])%k][m]+1

因此整體框架如下:
```py
n = len(nums)
dp = [[0]*k for _ in range(k)]

res = 1
for num in nums:
    x = num%k
    for m in range(k):
        prev = (m-num)%k
        dp[x][m] = max(dp[x][m], dp[prev][m]+1)
        res = max(res, dp[x][m])
return res
```

time: O(nk)
space: O(k^2)