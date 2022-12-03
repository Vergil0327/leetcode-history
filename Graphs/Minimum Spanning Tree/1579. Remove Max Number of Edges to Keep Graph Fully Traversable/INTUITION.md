### Union-Find

兩邊所需要的最少路徑，沒有多餘的邊且連接所有的點，會形成一棵樹，如果邊有權重則會形成Minimum Spanning Tree(最小生成樹)。n個節點最少會需要n-1個邊

如此一來我們可以藉由Kruskal的思想，將alice和bob各自擁有的邊組成MST後，全部的邊扣掉必要的邊即為答案

同時這邊有個greedy思想是，雖然每個邊沒有權重，但我們應當優先利用type3來組成MST，因為type3為雙向的，一個type3組成可省下alice & bob的單向邊

因此如果要找最多能移除掉多少邊的話，我們應該優先使用type3來使用

最後必須注意edge case，如果alice或bob無法組成MST，即無法連接所有的點的話，應該返回`-1`