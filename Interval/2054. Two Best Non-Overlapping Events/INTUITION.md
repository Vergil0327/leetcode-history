# Intuition

如果我們對看任意時間點events[i]:

```
- - - - - [start_time, end_time] - - - - - 
```

我們另一個events[j]的搜索範圍為:
1. < start_time
2. > end_time

所以我們可以用一個prefixMax[j]跟suffixMax[j]來紀錄兩邊的截至到j的最大值

- prefixMax[j]
  - 對events以end_time由小到大排序
  - 這樣我們就能從左到右遍歷, 紀錄截至到events[i].end_time為止的最大值為prefixMax[j]

- suffixMax[j]
  - 對events以start_time由小到大排序
  - 我們從右到左遍歷, 用suffix[j]紀錄在events[i].start_time之後的max

也就是
```
prefixMax[start_time-1] [start_time, end_time] suffixMax[end_time+1]
```

所以我們從prefixMax以及suffixMax兩者間取大, 然後遍歷[0,n-1]找出全局最大即為答案
`max(events[i].val + max(prefixMax, suffixMax)) where i from 0 to n-1`

# Optimization

首先我們先對start_time排序:
`events[0], events[1], ..., events[i]`

對於events[i], 我們遍歷`i`的時候可以同時紀錄`max_val_until`

res = max(res, events[i].val + max_val_until)

其中,
max_val_until = max(max_val_until, events[j].val) where events[j].end_time < events[i].start_time

所以我們可以用個minHeap來紀錄 (end_time, value)
把所有events[j] where j < i加入到minHeap裡

一但minHeap的end_time小於events[i].start_time時, 我們便可以將它從minHeap中彈出並更新max_val_until