# Intuition

利用BFS搜索最短路徑, 這題的關鍵在於如何避免不必要的BFS路徑分支

這邊我們用個hashmap紀錄`visited[(row, col, state)] = best battery remaining`

在相同位置相同狀態下, 如果電量較以前某個選擇差, 那就沒必要再繼續往後嘗試BFS了

另外由於`1 <= m == classroom.length <= 20, 1 <= n == classroom[i].length <= 20`, 規模很小, 所以我們用個mask來紀錄當前的litter收集狀態