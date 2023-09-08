# Intuition

critical connections: 移除connections[i]後會有node不再跟整個graph連接在一起
ex. connections = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]], output = [[1,3]]
```
0-1-2-0
  |
  3-4-5
  |   |
   - -
```

O(n^2)解法就看移除connections[i]後, 在看剩餘的connections連通起來還會不會是完整的network graph
我們需要的是一個高效的方式在遍歷connectsions[i]過程中快速查看, 移除connections[i]後還是不是完整的network graph
這題考的是Tarjan's algorithm, 特定算法的問題

首先能觀察到的是: 如果connections[i]是criitcal connection, 那這條邊肯定不在cycle裡
所以我們可以:
- 每當遇到cycle, 也就是遇到已經訪問過的節點, 我們更新low[node] = min(low[node], low[nei])
    - 其中**low[node]**代表的是`node`所能訪問到的最早的祖先節點, 其中我們對每個節點都紀錄個timestamp, 紀錄他們是第幾次遞歸時訪問到的, 這邊我們用**dfn[node]**來記錄這個時間戳的訊息

- 如果沒遇到cycle
    - 那我們先紀錄parent[nei] = node, 以免後續在進行DFS時走回頭路
    - 然後繼續DFS遞歸, 當`node`在DFS過程中遇到下個節點`nei`時:
      1. 如果`low[nei] > low[node]`, 代表`nei`如果不經由[node, nei]這條邊的話, 到達不了low[node]這個位置, 所以[node, nei]為critical edge
      2. 但如果low[nei] <= low[node], 那我們就更新`low[node] = min(low[node], low[nei])`, 紀錄`node`所能到達的最早的祖先節點為`low[nei]`

    - 順帶一提, 如果low[nei] >= dfn[node], 代表node是critical vertex, 代表移除掉node後, connected component會增加

# Complexity
- time complexity: O(connections.length)
- space complexity: O(n)