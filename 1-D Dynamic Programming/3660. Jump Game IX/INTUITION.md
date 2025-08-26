# Intuition

往右跳, 只能跳比自己小的
往左跳, 只能跳比自己大的

ex. nums=[30,21,5,35,24], answer=[35,35,35,35,35]

1. 30 -> 24 -> 35
2. 21 -> 30 -> ... -> 35
3. 5 -> 30 -> ... -> 35
4. 35
5. 24 ->35

所以對`i`來說, 如果知道prefix max, 就知道過往能跳的最大值多少
如果知道suffix min, 就能知道右邊能跳的最小值是多少, 那如果跳到右邊的值, 如果小於prefix max
代表能跳向右邊, 然後再從右邊跳往左邊更大的值.

如果定義res[i]: the reachable max value for starting `i`
一但能跳往右邊然後再跳往左邊, 代表可以更新res[i] = max(res[i], res[i+1])

所以求得prefix max `max_from_left`後, max_from_left可以作為res的起始值
然後遍歷一遍查看suffix min是否**小於**prefix max, 小於的話就能進一步更新答案`res[i] = max(res[i], res[i+1])`

由於res[i]依賴res[i+1], 所以從後往前遍歷