# Intuition

rowConditions跟colConditions表明了每個node在row與column上的先後順序
所以我們可以把這兩個維度看成directed graph
在rows上的順序為: rowConditions[i][0] -> rowConditions[i][1]
在column上的順序為: colConditions[i][0] -> colConditions[i][1]

如此一來就能得出每個node的indegree並進行topological sort
一但有了rows跟columns的topological sort
我們就能將順序轉換成`{row/col: node}`的hashmap後, 並一一放入matrix裡