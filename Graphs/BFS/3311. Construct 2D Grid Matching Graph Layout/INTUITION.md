# Intuition

首先觀察到:
- 角落: minimum indegree
- 四個邊: minimum indegree + 1
- 中間部分, minimum indegree + 2

挑選任意角落節點為左上起點出發
然後再沿著邊節點繼續往下, 先找出grid的維度`m`
那再來就只需要每個`row`往右延伸即可

所以一開始我們用BFS先完成grid的first column, 我們就從左上出發, 然後挑一個沒使用過的**邊節點**持續往下走, 直到我們連接到另個角落節點

> indegree of 邊節點 = indegre 角落節點 + 1
> indegree of 中心內部節點 = indegree of 邊節點 + 1

等到我們完成第一個column後, 那再來就簡單了
我們從第一個column的每一個grid[i][0]開始往右進行BFS找出臨近節點即可

# Approach

### 找出第一個column

從起始角落節點出發, 沿著邊節點, 最後抵達另個角落節點
所以這邊我們還得skip掉內部節點
```py
END_ROW = False
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()

        # check if we found the opposite corner node
        for nxt in graph[node]:
            if nxt in visited: continue

            if indeg[nxt] == CORNER_DEG:
                visited.add(nxt)
                END_ROW = True
                grid.append([nxt])
                break
        if END_ROW: break

        # keep append node in rows
        for nxt in graph[node]:
            if indeg[nxt] == INSIDE_DEG: continue
            if nxt in visited: continue
            visited.add(nxt)
            
            queue.append(nxt)
            grid.append([nxt])
            break

    if END_ROW:
        break
```

### 完成每row的剩餘column

```py
queue = deque(grid[i][0] for i in range(len(grid)))
row = {}
for r in range(len(grid)):
    row[grid[r][0]] = r

while queue:
    for _ in range(len(queue)):
        node = queue.popleft()

        for nxt in graph[node]:
            if nxt in visited: continue
            visited.add(nxt)

            queue.append(nxt)
            row[nxt] = row[node]
            grid[row[node]].append(nxt)
return grid
```

# Edge Case

當`CORNER_DEG == 1`時, 代表整個grid只有one row

```py
if CORNER_DEG == 1: # only 1 row: [start_node, ...]
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            for nxt in graph[node]:
                if nxt in visited: continue
                visited.add(nxt)
                grid[0].append(nxt)
                queue.append(nxt)
    return grid
```