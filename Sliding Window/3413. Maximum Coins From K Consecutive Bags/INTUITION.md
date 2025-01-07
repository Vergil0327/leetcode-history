# Intuition

先對coins排序, 然後考察每個coins[i]
1. 首先由左往右, 我們以每個coins[i][0]左端點為基準往右找連續`k`個位置
2. 由右往左, 以每個coins[i][1]右端點為基準往左找連續`k`個位置

兩種方向個進行一次sliding window找出最大coins

但過程中sliding window一直沒維護好所以沒能pass, 主要是因為有些區段可能只是部分包含, 在扣除的地方出了差錯