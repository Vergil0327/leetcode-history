### MST Kruskal - Union-Find

根據定義:
- critical edge: MST移除後總權重會增加
- pseudo-critical edge: 使用或移除，MST總權重不變

根據Kruskal，我們必須對所有邊排序，然後從最小邊開始連接
因為最後要返回原始邊的index，因此我們儲存index在每個edge裡

然後首先找出我們MST的最小權重`minCost`

#### Find critical edge

找到後開始遍歷每個邊，看看移除後會不會使得新的MST總權重增加

*這邊要注意，我們必須確認移除該邊後，是否能生成合法的MST，連接的邊數必須等同於總node數減1*
如果移除後無法生成MST(無法連接每個點)，我們返回inf作為他的權重，同時這個邊亦為critical edge

#### Find pseudo-critical edge

再來我們遍歷每個邊找pseudo-critical edge
1. pseudo-critical不可能為critical edge
2. 再來我們必須確認我們一定有使用這個邊來生成MST，如果總權重不變，即為pseudo-critical edge
   - 這裡我們將`current edge`插入首位，根據kruskal算法，起始邊一定會用上
   - 因為kruskal屬於greedy algorithm，除了起始邊外，我們無法確認是否一定會用上