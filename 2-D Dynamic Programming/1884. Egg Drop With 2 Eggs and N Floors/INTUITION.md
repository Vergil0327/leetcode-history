# Intuition

一層一層丟, 當雞蛋丟在第`i`層時:
- 如果破了, 那麼所需操作數為`i`
- 如果沒破, 那就是後續的`n-i`層還可再丟一次, 所需操作數`1 + self.twoEggDrop(n-i)`

由於我們是要找出準確的那層樓(with certainty), 所以我們真正在意的是**worst case**
所以我們兩種決策要取次數最多的那個, 該操作數代表這時我們才能真正確定是哪層樓是丟了蛋會碎
所以對於`i`層來說, 最低所需操作數為`max(i, self.twoEggDrop(n-i)+1)`

最終我們在全部**worst case**中取全局最小的即為答案

```py
class Solution:
    @cache
    def twoEggDrop(self, n: int) -> int:
        if n == 1: return 1

        moves = inf
        for i in range(1, n+1):
            moves = min(moves, max(i, self.twoEggDrop(n-i)+1))
        return moves     
```

這題的follow-up為[887. Super Egg Drop](https://leetcode.com/problems/super-egg-drop/description/)

我們能這麼定義dp:

`dp[k][i]: the maximum floor we can cover with k eggs and i try`

base case:
dp[0][i] = 0, maximum floor we can check with certainty with 0 egg and i try
dp[k][0] = 0, maximum floor we can check with certainty with k egg and i try

state transfer:
- if egg breaks, the maximum floor we can cover is same as dp[k-1][i-1]
  - dp[k][i] = dp[k-1][i-1]
- if egg not breaks, keep trying with k eggs and i-1 try and we check 1 floor with certainty
  - dp[k][i] = dp[k][i-1] + 1
- 所以dp[k][i] = dp[k-1][i-1] + (dp[k][i-1]+1)

那如果將這個generalized state transfer function應用在這題的話
我們就是bottom-up的方式持續更新, 去找到一個合適的ops使得dp[k][ops]剛好能覆蓋n層樓

> n層樓最多只需要n次嘗試, 所以我們dp空間為O(k*n)

```py
k = 2 # two eggs
dp = [[0] * (n+1) for _ in range(k+1)]

ops = 0
while dp[k][ops] < n:
    ops += 1
    for kk in range(1, k+1):
        dp[kk][ops] = dp[kk-1][ops-1] + (dp[kk][ops-1]+1)
return ops
```
