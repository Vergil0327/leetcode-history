# Intuition

一開始想法是subgraph可能由以下三種情況組成:

1. src1 -> dest + src2 -> dest
2. src1 -> src2 -> dest
3. src2 -> src1 -> dest

我們計算這三種可能情形的總權重, 挑最小的即可

但會fail在這test case:
n=6, edges=[[0,2,10],[0,4,2],[1,4,2],[1,3,10],[3,5,10],[4,5,20],[2,5,10]]
src1=0, src2=1, dest=5
expected=24

實際上情況應該要更generalized來想, minimum weighted subgraph應由以下三種最短路徑情況組成:
- src1 -> common node
- src2 -> common node
- common node -> dest

所以:
1. 我們先求src1到每個節點的最短路徑 (dijkstra + dp array)
2. 再用同樣方法求出src2到每個節點的最短路徑 (dijkstra + dp array)
3. 再來反過來求出dest到其他點的最短距離 (dijkstra + dp array)

三者都求出來後我們就能遍歷所有節點作為中間節點, 找出:
min(dp1[mid] + dp2[mid] + dp3[mid] for mid in range(n))