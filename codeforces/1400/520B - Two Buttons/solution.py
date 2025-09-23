# minimum distance => try BFS

from collections import deque
 
n, m = list(map(int, input().split()))
 
queue = deque([n])
 
pressed = 0
visited = set()
while queue:
    found = False
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == m:
            found = True
            break
        if x in visited: continue
        visited.add(x)
 
        if x < m:
            queue.append(x*2)
        if x-1 > 0:
            queue.append(x-1)
    if found: break
    pressed += 1
print(pressed)