# Intuiion - Solution 1

先對ranges排序, 然後將每個連續區間合併
最後看存不存在一個區間包含[left,right]

time : O(nlogn) 

# Intuition - Solution 2

我們用個diff array標記每個區間的涵蓋範圍
最後遍歷[left,right]看有沒有被diff array給cover到

time: O(max(end, right))