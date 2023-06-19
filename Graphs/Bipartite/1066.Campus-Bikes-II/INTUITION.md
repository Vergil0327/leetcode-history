# Intuition

workers[i] <---> bikes[j]

帶有權重的二分圖

each workers[i] can choose one of bikes, since workers <= 10 & bikes <= 10, we can use bitmask to represent as choosing state.

if bitmask = 101110, it means 1st, 2nd, 3rd and 5th (from right to left) bike is choosed

thus, we can define dp[state] = minimum disntance sum for current choosing state `state`.

state transfer:

for i-th bike, we iterate all the choosing state (i.e. bitmask) which has j 1-bits (1-indexed)
then, dp[state] = dp[state-(1<<i)]+dist[i][j] where bitmask&(1<<i) == 1


# Other Solution - 求最短路徑

workers[i] <---> bikes[j]

帶有權重的二分圖

總共有`m`個workers
每個workers[i]跟bikes[j]所對應的距離想成weight的話
我們可以想成最終每個worker都挑完bike後, i.e. bitmask = 1111...111 如果用bitmask表示挑選的狀態的話
那們我們要找的就是就相當於state=0 -> state=m 1-bits的最短路徑

因此可以用dijkstra來找
一開始全部bikes都沒挑, state = 0
最後要從bikes中挑出`m`個給workers
第一個有m 1-bits的狀態即為最短路徑