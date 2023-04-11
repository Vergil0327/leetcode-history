# Intuition

題意主要是說要把jobs分成d個連續區間來完成, 每次需要的difficulty為該區間取max

首先如果`d`超過整個區間長度的話，那麼我們不可能將jobs分成`d`個區間
直接返回`-1`

jobs = X X X X X X X X X [X X X X]
                      j-1 j     i

我們這麼定義dp:
dp[i][d]: the minimum difficulty of jobs[:i] completed within d days
考慮jobs[i]的話, 往前找一段區間jobs[j:i]然後更新dp[i][d]
由於不知道哪個j才是最佳，所以我們全部找一遍, dynamic programming 就是try them all with memorization

所以狀態轉移方程為

dp[i][d] = min(dp[i][d], dp[j-1][d-1] + difficulty(jobs[j:i]))
由於difficulty是該區間的最大值, 所以我們在找`j`的同時應該還需要同時紀錄當下的difficulty

由於狀態更新會需要用到dp[j-1][d-1]所以我們全部改成1-indexed來避免out-of-bounds error
dp[i]跟jobDifficulty都改成1-indexed後, 遍歷範圍變成[1:n+1]

然後再注意一下base case
dp[1][1]會需要用到dp[0][0]來更新

dp[0][0] = 0 # 0個job, 0天 -> 所以difficulty = 0