# Intuition

遇到design問題, 先想一下整個流程

首先想到的是我們必須高效的儲存key-value pair `timeline = {timestamp: price}`

所以需要用到hashmap

再來我們需要查詢最近一次的record
由於timestamp是持續遞增的
所以我們在更新的時候持續對timestamp取`max`更新當前時間, 這樣即可用O(1)時間查詢`timeline[latest_time]`

再來要找max和min, 直覺想到是max heap跟min heap
但由於值可能會out-dated, 所以在返回maxHeap[0]跟minHeap[0]前, 先確認當前的值有沒有out-dated, 有的話先更新

```py
pq = self.maxH
while pq and -pq[0][0] != self.timeline[pq[0][1]]:
    _, ts = heapq.heappop(pq)
    heapq.heappush(pq, [-self.timeline[ts], ts])

max = -pq[0][0]

pq = self.minH
while pq and pq[0][0] != self.timeline[pq[0][1]]:
    _, ts = heapq.heappop(pq)
    heapq.heappush(pq, [self.timeline[ts], ts])

min = pq[0][0]
```