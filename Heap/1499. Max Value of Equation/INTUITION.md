# Intuition 1

題意是希望找出**max(yi + yj + |xi - xj|)**, 那直覺肯定是想說先拆掉絕對值|...|:

=> 由於已經依照xi排序, 拆掉絕對值得出: **max(yi + yj - xi + xj) where xi-xj <= k**
=> 調換一下順序發現: **max((yi-xi) + (xj+yj))**

那如果我們預處理:
```py
A = [(y-x) for x, y in points]
B = [(x+y) for x, y in points]
```

那就變成求**max(A[i]+B[j]) where xi-xj <= k**
那首先想到的就是two pointers (或sliding window), 我們利用雙指針i, j找出符合xi-xj <= k的數, 由於我們是要找**max(A[i]+B[j])**, 所以我們用max heap來儲存B[j], A[i]

```py
j = 0
res = -inf
pq1, pq2 = [], []
for i in range(len(points)):
    while j < len(points) and points[j][0]-points[i][0] <= k:
        heapq.heappush(pq1, (-A[j], j))
        heapq.heappush(pq2, (-B[j], j))
        j += 1
```

那再來就簡單了, 首先先排除不符合條件的point:

考慮i-th point時, [0,i-1]的所有點都得排除掉

```py
while pq1 and pq1[0][1] < i:
    heapq.heappop(pq1)
while pq2 and pq2[0][1] < i:
    heapq.heappop(pq2)
```

再來就利用heap的性質找出max(A[i]-B[j]):
- if pq2[0][1] != pq1[0][1] (相異兩點): res = max(res, (-pq2[0][0]) + (-pq1[0][0]))
- else 兩點是同一點:
  1. pop pq1, then res = max(res, (-pq2[0][0]) + (-pq1[0][0]))
  2. pop pq2, then res = max(res, (-pq2[0][0]) + (-pq1[0][0]))

time: O(nlogn)


# Intuition 2 - O(n) solution

target: **max((yi-xi) + (xj+yj))**

use monotonically decreasing deque to find maximum element
過程持續維護monotonical decreasing deque, 然後利用**deque[0] = y-x (max element)**求出:

res = max(res, deque[0] + x+y)

首先維護一個monotonically decreasing deque如下:

```py
queue = deque()
res = -inf
for x, y in points:
    while queue and x-queue[0][1] > k: # pop invalid point[i]
        queue.popleft()

    # find max result here

    while queue and queue[-1][0] <= y-x: # monotonically decreasing
        queue.pop()
    queue.append([y-x, x])
```

再來就在中間找出條件符合的max result即可, queue[0][0]為符合條件的max element

```py
if queue:
    res = max(res, queue[0][0] + y + x)
```
