# Intuition

由於是要找k-th smallest, 首先想到用min heap


我們有m個size為n的sorted array

由於已經排序過, 每一行的第一個元素或是該行最小的, 所以1-th smallest sum為:
```py
sum1 = sum(row[0] for row in mat)
```

[[1,10,10]
 [1,4,5]
 [2,3,6]]

 [1,1,2], index=[0,0,0]
 [1,1,3], index=[0,0,1]
 [1,4,2], index=[0,1,0]
 [1,4,3], index=[0,1,1]
 [1,1,6], index=[0,0,2]
 [1,5,2], index=[0,2,0]
 [1,5,3], index=[0,2,1]

 從一開始的index=[0,0,0]開始的[1,1,2] (sum=4)

 再來就看每一個row的下個index哪個值是最小的, 如果rowi[j]為下個最小
 那麼: sum' = sum + rowi[j] - rowi[j-1], where index[i] = j

所以我們可以一開始用minHeap儲存: [sum1, [0]*m], 其中
1. 1st element代表當前選擇的sum
2. 2nd element代表當前每一row所選擇的column的狀態

再來可以用BFS + min heap

對於當前選擇狀態index=[0,0,0], 我們將下個可能狀態全部加入到min heap裡然後再取sum最小的出來
定義index[i] = j代表當前i-th row選的是j-th column
那這樣一開始index=[0,0,0], 再來將index=[1,0,0],[0,1,0],[0,0,1]狀態的sum全加入到min heap裡
next_sum = sum + mat[i][index[i+1]] - mat[i][index[i]]
同時注意對於相同的index我們應避免重複, 所以我們以tuple(index)為key加入到hashset裡
最後取出第k個即為答案

整個BFS + min heap 框架為:
```py
minHeap = [[tot, tuple([0]*m)]]
visited = set()
while k:
    total, pick_idx = heapq.heappop(minHeap)
    if pick_idx in visited: continue
    visited.add(pick_idx)

    for i in range(m):
        if pick_idx[i]+1 >= n: continue
        nxt = list(pick_idx)
        nxt[i] += 1
        key = tuple(nxt)
        if key in visited: continue
    
        heapq.heappush(minHeap, [total + mat[i][nxt[i]] - mat[i][nxt[i]-1], key])
```

O(k * (log(m*n) + m*(m + log(m*n))))
