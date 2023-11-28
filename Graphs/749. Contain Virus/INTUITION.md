# Intuition

use union-find or dfs to find/mark connected components

首先先想病毒不傳播的話, 該怎麼算出包圍的牆:
- 用遍歷一遍用union-find把病毒地區union在一起, 每個infected cell往四個方向查看
- 在這四個方向中, 如果是infected cell那就union再一起, 如果沒有但也不是邊界, 那就wall += 1
如此以來就能算出所需boundary

但實際上病毒每晚都會往外擴散一格, 而這常見的模擬方式是用BFS來進行

再來就想如果有多個infected area, 該先封鎖哪個好?
=> Greedy: 最關鍵突破口是想到我們應該優先封鎖**會傳染較多地區**的infected area

所以想法上會是用BFS模擬每天傳染情境, 然後每天(也就是每次iteration)在用dfs或union-find查看哪個地區會傳染最多, 我們再優先封鎖傳染最多的地區
=> 從這看到我們可能會需要個priority queue找出會傳染最多地區的infected connected component進行封鎖
=> 再將剩餘地區開始傳染

所以整理一下, 整體框架為:
1. 首先題目保證一定會持續向外感染, 就算是一格一格感染也只需要m*n天, 所以我們用個`m*n`次的iteration
2. 再來遍歷整個grid並用DFS找出connected component, 同時在DFS過程中計算每個connected component的
    - 封鎖所需的牆數wall_count
    - infected cell的位置, 放入hashset裡避免重複, 同時後續假如選擇該區封鎖的話, 把這些位置都標記為`-1`
    - danger cell的位置, 也就是如果沒封鎖的後續傳染格子, 同樣把這些座標加入到hashset裡, hashset.size作為max heap的key
3. 利用priority queue找出優先封鎖的地區, 也就是感染最多地區的infected area. 如果無代表封鎖結束
    - 更新所需牆數
    - 把封鎖的傳染地區標記`-1`, 以避免重複計算
    - 未封鎖地區開始傳染