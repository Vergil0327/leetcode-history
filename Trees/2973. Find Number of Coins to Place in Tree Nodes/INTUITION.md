# Intuition

這邊紀錄一下我整個思緒
一開始看到是顆樹, 然後我們要找出subtree的三個節點的最大乘積
首先想到的就是post-order DFS, 我們從葉子節點出發, 然後一路往上找

由於要找最大成績, 首先想到的就是需要個有序容器來裝subtree的所有**cost[node]**

那這時很容易想到的就是: 那我們就定義DFS返回subtree的所有節點cost[node]

由於條件說明如果subtree.size小於3, 那就返回1
因此我們一開始就將res[i]初始化為1

那再來就是用dfs來計算每個subtree的最大乘積

如果有序容器的size為3, 那我們就是直接三個相乘
然後依據題目說明, 乘積負數的話返回0

但如果size > 3呢?
這邊就要注意, 由於cost[node]有正有負, 所以最大乘積我們有兩種情況要考慮:
1. 三個正數
2. 兩個負數 * 一個正數

同時也會發現, 我們需要紀錄的, 其實就是整個有序容器的前三根後三個數值即可 (以便於找出最大的三個正數及最小的三個負數)

因此整個dfs過程中, 我們僅需要維護至多size為6(或甚至5)的大小即可