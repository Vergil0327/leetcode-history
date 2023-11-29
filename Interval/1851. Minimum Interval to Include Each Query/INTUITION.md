# Intuition

對於時間的問題, 首先先排序看有沒有幫助
再來對於任意queries[i]來說, 要找出所有符合intervals[i][0] <= queries[i] <= intervals[i][1]的區間, 並找出size 最小的一個
這邊就想到可以把符合的區間都放入一個有序資料結構，找出最小的

在配合先前對時間做排序的話, 突破口就在於我們我們也依照時間順序來解決queries[i]
這樣的話隨著時間增加, 我們可以持續把符合的intervals[i]都加入到min heap裡, 同時也隨著時間把不符合的intervals[i]從min heap中淘汰掉
這樣就能利用min heap的特性找出queries[i]要的最小size

# Approach

1. 對intervals進行由小到大排序
2. 對queries由小到大排序, 並記住原本index
3. 遍歷queries[i]
   - 將所有intervals[j][0] <= queries[i]的都加入到min heap裡
   - 將min heap裡所有不合法的intervals[j]都給淘汰掉, 也就是將intervals[j][1] < queries[i]的都給pop掉
   - 那麼res[queries[i].original_index] = minHeap[0].size