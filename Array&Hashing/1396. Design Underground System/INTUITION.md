# Intuition

為了計算站跟站之間的平均時間, 我們**checkIn**需要存每個`id`的進站時間以及站名.
這樣在**checkout**的時候就能計算出進站到出站所耗費的時間

所以我們需要個hashmap來紀錄每個id的checkIn紀錄
```py
# checkIn
self.records[id] = (t, stationName)
```

並在checkout更新average time
```py
# checkout

t0, enterStationName = self.records[id]
accumulateTime, timeUntil = average[enterStationName][leaveStationName]
average[enterStationName][leaveStationName] = [accumulateTime + (t-t0), timeUntil + 1]
```

有了紀錄後就能紀錄兩站之間的總花費時間以及進出站的人次
求平均再兩者相除即可

所以還需要另一個hashmap來紀錄:
`average[enterStationName][leaveStationName] = (totalDuration, times)`