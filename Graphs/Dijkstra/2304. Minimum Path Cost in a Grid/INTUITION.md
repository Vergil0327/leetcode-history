# Intuition

其實就是從一個帶有權重的圖, 起點為i=0, j=0, 1, ..., n, 找出一個最短路徑抵達i=m-1 where m=len(grid), n=len(grid[0])

所以我們可以用Dijkstra algorithm來找這條路徑