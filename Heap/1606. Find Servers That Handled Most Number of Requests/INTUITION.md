# Intuition

看到這種模擬實際情形, 有idle, busy各種狀態的模擬題時, 就先試著模擬出情境就對了

首先我們需要知道有哪些server是idle的, 以及查詢next available server的方法
```py
idle = [True]*k

def check(svr):
    if idle[svr]: return False, svr

    i = (svr+1)%k
    while not idle[i]:
        if i == svr: return True, None
        i = (i+1)%k
    return False, i
```

再來還需要有個queue儲存所有busy server, 由於要將完成時間小於等於當前時間的閒置server加回idle中, 所以很自然地會想到用priority queue (min heap)
```py
processed = [] # min heap, [t, server_id]
```

再來就直接模擬情境
```py
for i, t in enumerate(arrival):
    while processed and processed[0][0] <= t:
        _, svr = heapq.heappop(processed)
        idle[svr] = True


    dropped, assign = check(i%k)
    if dropped: continue

    res[assign] += 1
    idle[assign] = False
    heapq.heappush(processed, [t+load[i], assign])

mx = max(res)
return [svr for svr, cnt in enumerate(res) if cnt == mx]
```

但看下數值會發現`k`的值相當大, 意思是我們可能要有個更高效的方法來找出next available idle server

- 1 <= k <= 10^5
- 1 <= arrival.length, load.length <= 10^5

由於我們要找的閒置server是從i%k, (i%k)+1, (i%k)+2, ...去找
所以我們可以用個SortedList `idle`來維護所有idle servers
- 如果`idle`為空, 那當前request就得drop掉
- 如果不為空那就找出: `target_server_idx = idle.bisect_left(i%k)`
    - 另外如果target_server_idx == len(idle), 那target_server_idx = 0 (繞回第一台閒置server)

然後在隨時間維護好priority queue `busy`跟sorted list `idle`兩邊的狀態即可


time: $O(nlogk)$
space: $O(k)$