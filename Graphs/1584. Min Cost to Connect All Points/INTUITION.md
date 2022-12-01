## Prim

從任一起點開始，每次連接最近的一個點，逐漸擴大相互連接的區域
透過min heap找尋最接近的點
透過hashset來避免找重複的點，變成無限迴圈

## Kruskal

有點Greedy的思想
將所有的edge以長度排序，優先選擇最短的邊將兩點相互連接
透過union-find來避免重複連接