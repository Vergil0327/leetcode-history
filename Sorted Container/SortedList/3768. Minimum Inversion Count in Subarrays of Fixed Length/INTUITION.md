# Intuition

sliding window + SortedList去維護固定長度的subarray裡, 有多少inverse count

每當元素增減, 都去計算inverse count的貢獻並維護
並在過程中找出全局最低inverse count即可