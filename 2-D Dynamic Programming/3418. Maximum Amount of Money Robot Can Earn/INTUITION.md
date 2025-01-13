# Intuition

定義`dfs(r,c,x): the maximum amount at (r,c) and already nertralized x times`
那再來就是把每個選擇都嘗試一遍:

1. neutralized: 只有當`x < 2 and coins[r][c] < 0`時
2. 不neutralized

全局取`max`即可


time: O(4*rcx)
space: O(rcx)