# Intuition

dp[i][j]: the minimum score until (i, j)

狀態轉移: dp[i][j]只能從兩個方向轉移過來 => dp[i-1][j], dp[i][j-1]
以及自身數值, 因此 dp[i][j] = min(dp[i-1][j], dp[i][j-1], grid[i][j])

而對於(i,j) cell, 我們要在該(i,j)cell拿到最高分差的話, 肯定是從最低分那邊轉移過來, 並且一樣只有兩個方向
因此: score = max(score, grid[i][j] - min(dp[i-1][j], dp[i][j-1]))
我們持續取全局最大score即可
