# Intuition

1 <= n == time.length <= 12 => 首先想到可以用bitmask來表示誰已經過岸, 而誰還沒有
minimum time => 想到可以用BFS (Dijkstra)?

從這思路去想的話, 先試著用dijkstra思緒來定義:

```
pq = [(0,0,0)] # (current_time, current_stage, bitmask_of_people_on_destination)
```

再來就是模擬渡河情況:

- 先渡河
    1. 如果還有沒過河的人, 就要有人回來
    2. 如果已經全都過河, 就不用回來
- 紀錄每個時間階段的最短時間, 以避免多餘的計算: minTime[state][stage] = current_time if current_time < minTime[state][stage]