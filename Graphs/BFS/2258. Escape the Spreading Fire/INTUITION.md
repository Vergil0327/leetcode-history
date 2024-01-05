# Intuition

首先直覺想到得利用BFS去找出火與人抵達終點的最短時間

定義:
person[row][col]: the minimum time to arrive (row, col) for person
fire[row][col]: the minimum time to arrive (row, col) for fire

所以比較直覺能想到的是:
- if fire[m-1][n-1] == inf: return 10**9 # 火抵達不了終點
- if person[m-1][n-1] == inf: return -1 # 人本身就抵達不了
- if person[m-1][n-1] > fire[m-1][n-1]: return -1 # 人比火晚到

排除上述情況後, 我們至少能待:
diff = fire[m-1][n-1] - person[m-1][n-1]

再來最難的點是如何判斷待幾天
當前的`diff`是我們能在原地待著的最久時間

那麼火跟人抵達終點會有哪些情況?

對於終點(m-1, n-1)來說, 抵達終點前的前一步只可能是在(m-1, n-2)或(m-2, n-1)這兩個位置
如果火(fire)的路徑標記`F`, 人(person)的路徑標記為`P`

如果人跟火**可以**在抵達終點前路徑沒有相交, 由於順序上是人先抵達, 火在抵達
所以允許在原地等待`diff`在移動
```
      [F]
      [F]
[P][P][終]
```

如果人跟火在抵達終點前就路徑相交, 那麼代表人跟火會在終點前就先相交, 然後再同步抵達終點
但這樣其實在終點前就先被燒死了, 所以這時人只能等待`diff-1`時間
```
    [F]
    [F]
[P][F/P] [F/P] [終]
```

但要注意火是從多個方向過來的, 所以有可能同時[m-1][n-2]跟[m-2][n-1]都是火的最短路徑
這代表不管人是怎麼走的, 都一定會跟火在終點前就相交, 所以只能等待`diff-1`

另外要注意, 人也有可能可以同時從[m-1][n-2]跟[m-2][n-1]都是最短路徑
所以如果優先判斷人跟火同方向會錯, 因為更好的選擇是人可以走不同方向的那條路

```py
# 錯誤判斷
if fire[m-1][n-2] == fire[m-2][n-1]:
    return diff-1

if fire[m-1][n-2] < fire[m-2][n-1]:
    if person[m-1][n-2] == person[m-1][n-1]-1: # 人跟火同方向
        return diff-1
else:
    if person[m-2][n-1] == person[m-1][n-1]-1: # 人跟火同方向
        return diff-1
return diff
```


要正確判斷出這段還是比較難的:
```py
diff = fire[m-1][n-1] - person[m-1][n-1]
if fire[m-1][n-2] < fire[m-2][n-1]: # 火從fire[m-1][n-2]抵達
    if person[m-2][n-1] == person[m-1][n-1]-1: # 人跟火可以不同方向抵達
        return diff
    return diff-1
elif fire[m-1][n-2] > fire[m-2][n-1]: # 火從fire[m-2][n-1]抵達
    if person[m-1][n-2] == person[m-1][n-1]-1: # 人跟火可以不同方向抵達
        return diff
    return diff-1
else: # 火的兩個方向[m-1][n-2]跟[m-2][n-1]都是最短路徑
    return diff-1
```

所以如果已經知道要麻diff要麻diff-1的話, 其實也可以就跑一遍BFS確認一下就行了

```py
diff = fire[m-1][n-1] - person[m-1][n-1]
if check(diff):
    return diff
else:
    return diff-1
```

helper function

```py
def check(days):
    m, n = len(grid), len(grid[0])
    visited = [[0]*n for _ in range(m)]
    queue = deque([(0,0)])
    visited[0][0] = 1
    
    step = days
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col>=n: continue
                if grid[row][col] == 2: continue
                if visited[row][col]: continue
                if (row != m-1 or col != n-1) and step+1 >= fire[row][col]: continue # 火已先到

                visited[row][col] = 1
                queue.append([row, col])
                if row == m-1 and col == n-1 and step+1 <= fire[row][col]:
                    return True
        step += 1
    return False
```