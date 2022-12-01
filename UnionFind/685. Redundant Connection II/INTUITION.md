### Union-Find

這題在找`redundant edge`時要注意兩個case

首先可能有兩種情況:
1. 如果有某個edge形成兩個**root**，那代表其中一個edge是多餘的 ex. [[1,2],[1,3],[2,3]]
2. 每個節點都只有一個**root**，那代表有環的存在. ex. [[1,2],[2,3],[3,4],[4,1],[1,5]]

那我們就分開兩種情況來討論
- 如果`candidates`為空，那就透過union-find找出最後一個形成環的edge即可
- 如果`candidates`不為空，那一定有兩個候選的edge，其中一個必為`redundant`。那我們就試著刪除其中一個後，嘗試看看能不能順利生成樹(Kruskal Algorithm)
  - 如果可以那麼另一個edge即為redundant edge
  - 如果有環的存在，那代表未被刪除的edge為redundant edge
