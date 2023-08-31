# Intuition

首先想到的是從n出發, 計算每個點與n的最短距離

我們將與n的最短距離紀錄在`distanceToLastNode` array裡, 用BFS+priority queue從n出發來更新distanceToLastNode

那再來很明顯就是利用DFS從1到n並且從節點`i`出發到`i+1`只有當distanceToLastNode[i+1] < distanceToLastNode[i]時我們才能走, 計算到達n的總路徑數即為答案 => 用top-down dp (DFS+memorization)即可求解
