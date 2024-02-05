# Intuition

首先肯定是要依照arrival_time排序, 讓朋友們依序入座

由於Each arrivali time is **distinct**, 我們可以用arrival_time代表friend_id
那這樣我們的`target_arrival_time = times[targetFriend][0] # 排序前`

那再來我們就模擬情境
由於我們永遠都優先分配座標最小的座位, 所以我們可以用個有序容器裝目前可用的chair_id

```py
available_chairs = SortedList([i for i in range(n)])
```

再來我們就讓朋友依序入座, 並且讓所有leave_time <= 當前arrival_time的人離席

所以我們得用個有序容器紀錄每個入席人的(leave_time, chair_id), 這樣就能以log(n)時間移除所有應當離席的人, 並釋放chair_id, 重新將chair_id放入available_chairs中

如此一來, 整個情境的邏輯就清晰了, 我們只要返回targetFriend的chair_id即可:

```py
occupied = SortedList() # (leave_time, chair_id)

times.sort()
for arrival, leave in times:
    while occupied and occupied[0][0] <= arrival:
        available_chairs.add(occupied.pop(0)[1])

    chair_id = available_chairs.pop(0)
    if arrival == target: return chair_id
    occupied.add((leave, chair_id))
return -1
```
