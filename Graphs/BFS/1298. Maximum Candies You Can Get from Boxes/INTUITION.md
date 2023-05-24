# Intuitiond

這題只要模擬整個流程即可

首先我們當前有這麼多個箱子`initialBoxes`
再來每個輪次我們就把手中的箱子都試著打開看看

- 如果打不開, 我們重新放回queue裡
- 如果打開
  - 那就更新candies
  - 並且看有沒有鑰匙, 更新`status[key]=1`
  - 看有沒有找到新的box (containedBoxes[box]), 如果有則加進queue裡

所以這很明顯可以用BFS來輪次開箱

再來就是要注意這個BFS什麼時候停止?
1. 箱子全開完
2. 手中的箱子都是鎖住的

所以我們在用個`hashset`來紀錄當前手中有哪些鎖住的箱子
然後再找到key的時候判斷是不是能已經擁有的箱子, 如果有則把箱子從`hashset`中移除

最後判斷如果手上剩的都是鎖住的箱子的時候, 就跳出BFS
來避免死循環
```py
if len(locked) == len(queue): break
```