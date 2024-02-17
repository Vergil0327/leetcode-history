# Intuition

如果是farmland, 亦即`land[i][j] == 1`, 我們就BFS+floodfill或是用union-find找出connected component
然後再從這之中找出top-left跟bottom-right即可

- top-left: 在同個group裡, 找出(min_row, min_column)
- bottom-right: 在同個group裡, 找出(max_row, max_column)

但其實這題仔細閱讀, 有個更快的做法

> meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

上面這句保證所有farmland都是合法矩形
這代表我們直接在land[row][col]位置, 分別往右往下找出max_row, max_col即可
