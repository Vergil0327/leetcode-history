# Intuition

- 3 <= n <= 10^5
- 1 <= queries.length <= 10^5
- There are no two queries such that i != j and queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1].

我們肯定得依序遍歷queries.length => 代表時間複雜度上只能接受O(n)或O(nlogn)

再來看到第三個限制:
代表每次的queries[i]都是連通一段快速通道: [queries[i][0], queries[i][1]]
也就是從[queries[i][0]+1, queries[i][1]-1]全都消失, 從queries[i][0]可直接抵達queries[i][1], 不會有queries[i]跟queries[j]交錯發生

O(n^2) brute force很簡單:

```py
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        SET = set(range(n))
        for u, v in queries:
            for i in range(u+1, v):
                if i in SET:
                    SET.remove(i)
            res.append(len(SET)-1)
        return res
```

那麼延續brute force想法, 我們可以將線性時間刪除hashset的部分改成用有序容器
並配合binary search找出我們要刪除的元素區間將元素刪除掉
由於每個元素最多只會刪除一次, 所以整體會是O(queries.length * logn)時間

```py
from sortedcontainers import SortedList

sl = SortedList(range(n))
for u, v in queries:

    # delete [u+1, v-1] interval
    i = sl.bisect_left(u)
    j = sl.bisect_right(v)-1
    if sl[i] == u:
        i += 1
    if sl[j] == v:
        j -= 1
    for _ in range(j-i+1):
        sl.pop(i)

    # remaining distance
    res.append(len(sl)-1)
```

# Optimized Solution

記錄一下我們甚至可以用O(queries.length + n)時間完成

我們用hashmap記錄起初每個`[i, i+1] for i in range(n-1)`區間
再來我們遍歷`queries`時, 我們就看[queries[i][0], queries[i][1]]這段區間
持續從hashmap中移除掉
移除完後只留下`hashmap[queries[i][0]] = queries[i][1]`

那這樣我們遍歷過程中, hashmap裡面各個小區間都只會移除掉一次
所以整體時間會是O(queries + n)

```py
union = {i: i + 1 for i in range(n - 1)} # i -> i+1 for 0 <= i < n initially

res = []
for u, v in queries:
    # delete [u+1, v-1] interval
    if u in union and union[u] < v:
        start = u
        while start < v:
            start = union.pop(start)
        union[u] = v

    res.append(len(union))
return res
```