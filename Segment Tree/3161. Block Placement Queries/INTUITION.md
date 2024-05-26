# Intuition

持續切分出多個interval between [0, inf]
然後看能不能在[0,x]內找到一段interval的長度是**大於等於**sz的

[0, x1, x2, x3, inf]

brute force:

```py
from sortedcontainers import SortedDict, SortedList
            
def getResults(self, queries: List[List[int]]) -> List[bool]:
    intervals = SortedDict()
    intervals[0] = inf # start: end


    res = []
    for q in queries:
        if q[0] == 1:
            x = q[1]
            idx = intervals.bisect_right(x)-1
            start, end = intervals.peekitem(idx)

            intervals[start] = x
            intervals[x] = end

        else:
            x, sz = q[1], q[2]
            idx = intervals.bisect_right(x)-1

            l, _ = intervals.peekitem(idx)

            found = x-l >= sz
            for i in range(idx):
                start, end = intervals.peekitem(i)

                if end-start >= sz:
                    found = True
                    break

            res.append(found)

    return res 
```

每次放下一個obstacle在`x`位置, 我們就要在[0,x]之間找一個可以放置大小為`sz`的區間
區間求max => segment tree
但當下卡在如何高效地加入每個區間去更新當前的segment tree

首先我們先找出segment tree的空間範圍=> [0, max(queries[i][1])]
再來我們紀錄當前的所有區間, 紀錄起點終點在segment tree內 => segment_tree[start] = size
整個大體框架會是:

```py
ans = []
for query in queries:
    if query[0] == 1:
        insert_val(query[1])
    else:
        x, size = query[1], query[2]

        if size > x:
            ans.append(False)
            continue

        # max_value = seg_tree.query(0,x-size+1)
        max_value = seg.query(0, x-size)
        ans.append(max_value >= size)

return ans
```

其中最麻煩的就是helper func `insert_val`, 除此之外, 就是基本的segment tree
但當初contest應該要寫出來的, 其實已經想了一半了
我們能很直覺的想到用一個有序容器來記錄隨時間增加的obstacle位置 => SortedList
這樣我們就能用binary search去找出當前`x`會是在哪個位置, 並能以O(1)時間去找出前後obstacle `prev`跟`next`
然後將原本的[prev, next]拆分成[prev, x] + [x, next]

所以對於insert_val這helper func, 我們需要做的就是去維護一個Sorted List
並找出前後`prev`, `next`去更新segment tree
```py
sorted_list = SortedList([0])
def insert_val(x):
    sorted_list.add(x)
    idx = sorted_list.bisect_left(x)

    if idx-1 >= 0: # prev exists
        prev_x = sorted_list[idx-1]
        seg[prev] = x-prev

    if idx+1 < n: # next exists
        next_x = sorted_list[idx+1]
        seg[x] = next_x-x
    else: # x is the last obstacle
        seg[x] = inf
```

# Complexity

- time: O(queries.length * log(x))