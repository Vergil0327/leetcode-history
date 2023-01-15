# Intuition

這題最關鍵的思路是**從邊界著手**，外圍一圈邊界湧入海水後，如果內部更低則會填滿
因此我們可以從最低的邊界開始持續湧入

從低的邊界開始是因為，如果從高的，水往低處流，最後能填滿的最終還是取決於最低的那道牆
引此我們整個四周從低到高開始往內湧入找出能填滿的區域

由於要持續找出最低的邊界，因此我們將全部邊界以高度加入min heap裡，然後以BFS持續搜索

每當從min heap裡取出一個，便更新海平面到最新的高度 `seaLevel or wallHeight`，此時往四個方向進行BFS，能每一格能填充的水即為 `seaLevel/wallHeight - heightMap[current cell]`
持續加總即得最終能困住的水

# Complexity

- time complexity

$$O(mnlog(mn) + ElogV)$$
, where E = edges V = vertices

thus, we can turn ElogV into
$$O(mnlog(mn) + mnlog(mn))$$

- space complexity
$$O(n)$$