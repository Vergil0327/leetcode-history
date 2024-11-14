# Intuition

這題初看會想到DFS或BFS, 看(0,0)能不能抵達(m-1, n-1)
但由於只需要知道能不能, 其實就用union-find互相連通的道路給連接來即可

對於grid[r][c]來說, 根據道路方向, 我們就看右方跟下方有沒有能連接的區域
那這樣由左到右, 由上到下遍歷並試著`union`, 最後判斷`find(key(0, 0)) == find(key(m-1, n-1))`即可

# Other Approach

using BFS
當前位置(r,c)與下個位置(row, col)如果道路方向連通

那麼應當滿足:
1. row + direction_row = r
2. col + direction_col = c
