# Intuition

我們紀錄每個task時間點的所需天數: days[i]: we complete task i for days[i] day
同時紀錄前個task的index於 prevTaskIdx[task],  那這樣`days[i] - days[prevTaskIdx]`就知道中間過了多少天
假如小於space, 我們就補上breaks = space - (days[i] - days[prevTaskIdx])
然後在滿足space條件後, 完成task也需一天: days[i] += 1
所以個框架如下, 最終答案就是完成n個task的天數 days[len(tasks)]

```py
days = [0]*(len(tasks)+5) # day for task i to complete
prevTaskIdx = {}

for i, tsk in enumerate(tasks, start=1):
    days[i] += days[i-1]

    if tsk in prevTaskIdx:
        prev = prevTaskIdx[tsk]
        breaks = max(0, space - (days[i] - days[prev]))
        days[i] += breaks

    days[i] += 1
    prevTaskIdx[tsk] = i

return days[len(tasks)]
```

time: O(n)
space: O(n)