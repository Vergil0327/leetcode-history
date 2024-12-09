# Intuition

題目連狀態轉移都說明了, 而且每次的cost也都很清楚
很明顯是個求帶有權重的最短路徑問題, 因此兩點之間的最段路徑用Dijkstra Algorithm即可

因此我們`n`, `m`轉換成str來找尋最短路徑即可
但這邊有個需要注意的小細節是, 過程中不可以有leading zero

```py
s, t = str(n), str(m)

pq = [[n, s]]
visited = set()
while pq:
    cst, s = heapq.heappop(pq)
    if s in visited: continue
    visited.add(s)
    if s == t: return cst

    for i in range(len(s)):
        pre, suf = s[:i], s[i+1:]
        d = int(s[i])
        if d < 9:
            ss = pre + str(d+1) + suf
            if ss not in visited and not isPrime[int(ss)]:
                heapq.heappush(pq, [cst + int(ss), ss])
        if d > 0 and not (leadingZero := i==0 and d==1):
            ss = pre + str(d-1) + suf
            if ss not in visited and not isPrime[int(ss)]:
                heapq.heappush(pq, [cst + int(ss), ss])
return -1
```