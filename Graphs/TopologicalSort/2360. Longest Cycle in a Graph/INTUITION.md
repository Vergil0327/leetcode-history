# Intuition

每個node最多只有一個out degree，因此每個node只可能參與一個cycle
並且indegree為0的node不可能是cycle的一部分

ex.
```
1 -> 2 -> 3 -> 4 <- 9
               |    |
     5 -> 6 -> 7 -> 8
```

因此我們可以利用DFS，一但我們遇到一個訪問過的node `i`，代表我們形成了一個環，此時目前走的步數扣掉distance[i]即為還的長度

而這其實就是Topological Sort!

比起我們`first try`版本，每次都傳入一個[-1]*n的array，我們可以reuse `dist`, `visited` & `cycle` array

訪問過的節點記錄在`visited`裡避免重複訪問，並利用`dist`儲存node走到每個`i`節點的步數，再利用`cycle`來記錄當前的DFS是否已經訪問過`i`節點，如果訪問過代表我們找到了一個環

結束後再把cycle還原(backtracking)，然後重複使用，繼續遍歷找尋下個環

同樣地，我們也可以利用indegree + BFS的topological sort先把indegree為零的節點先標記`visited`移除掉

如下圖所示，當我們持續把所有indegree=0的節點一步步移除掉後，最終只會留下多個環
最後在遍歷一遍即可

```
# indegree[node1] ＝ indegree[node5] = 0
# 移除掉node1, node5後，indegree[node2] = indegree[node6] = 0
# 持續進行topological sort從外層一層一層剝掉indegree為0的節點後，剩下的都是indegree不為零的節點，也就是剩下多個環存在，在每個遍歷一遍並標記｀visited[node]`即可

1 -> 2 -> 3 -> 4 <- 9
               |    |
     5 -> 6 -> 7 -> 8

10 -> 11 -> 12 -> ...

24 <- 25
|     |
27 -> 26
```

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$