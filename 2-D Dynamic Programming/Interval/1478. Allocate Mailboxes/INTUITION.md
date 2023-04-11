# Intuition
houses = H H H H H H H [H H H H H H H]
                        j           i
                              M
依據題意, 我們要用K個Mailbox來涵蓋整個houses

我們先考慮第k個nearest mailbox `M`的情況, 假設它涵蓋的範圍為houses[j:i]
那麼前面整個houses[:j]就是用**k-1**個mailboxes來涵蓋，並且怎麼涵蓋我們不管
因此這看來是個dynamic programming的問題

如果我們這麼定義dp:
dp[i][k]: the minimum total distance between each house and its nearest mailbox considering houses[:i] with k mailboxes

狀態轉移方程則為
dp[i][k] =  min(dp[i][k], dp[j-1][k-1] + distanceBetween(houses[j:i]))

mailbox肯定是放在整個houses涵蓋區間的中位數為最佳
並且由於我們已經排過序所以mailbox位置應為 M = (j+i)//2

所以大體框架為:
```py
class Solution:
    def minDistance(self, houses: List[int], K: int) -> int:
        houses.sort()

        n = len(houses)

        houses = [houses[0]] + houses # to 1-indexed
        dp = [[inf] * (K+1) for _ in range(n+1)] # also 1-indexed
        
        # base case
        dp[0][0] = 0

        def distanceBetween(l, r):
            mid = (l+r)//2 # put mailbox in front of middle house within houses[l:r]
            dist = 0

            for i in range(l, r+1):
                dist += abs(houses[i]-houses[mid])
            return dist

        for i in range(1, n+1):
            for k in range(1, min(i, K)+1):
                for j in range(i, k-1, -1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + distanceBetween(j, i))

        return dp[n][K]
```

雖然這樣可以Accepted, 但效率只有`Beats 11.81%`
看起來是`distanceBetween`這邊反覆計算所導致
所以我們看看有沒有能改善的地方

# optimization
[X X X X X]
 j   M   i

distance = abs(j-M) + abs(j+1-M) + ... + abs(i-M)
         = (M-j) + (M-(j+1)) + ... + (M-M) + (M+1-M) + ... + (i-M)
         = (houses[M]+houses[M]+houses[M]+houses[M]+...+houses[M]) - (houses[j] + houses[j+1] + ... + houses[M]) + (houses[M]+houses[M]+houses[M]+houses[M]+...+houses[M]) - (houses[M] + houses[M+1] + ... + houses[i])
         = houses[M] * (M-j+1) - presum[j:M] + presum[M:i] - houses[M] * (i-M+1)

我想我們可以用個prefix sum配合數學來達到O(1)計算

```py
presum = [0] * (len(houses)+1)
for i in range(1, len(houses)+1):
    presum[i] = presum[i-1] + houses[i-1]

for i in range(1, n+1):
    for k in range(1, min(i, K)+1):
        for j in range(i, k-1, -1):
            # dp[i][k] = min(dp[i][k], dp[j-1][k-1] + distanceBetween(j, i))
            mid = (j+i)//2
            distance = houses[mid]*(mid-j+1) - (presum[mid+1]-presum[j]) + (presum[i+1]-presum[mid]) - houses[mid]*(i-mid+1)

            dp[i][k] = min(dp[i][k], dp[j-1][k-1] + distance)
```