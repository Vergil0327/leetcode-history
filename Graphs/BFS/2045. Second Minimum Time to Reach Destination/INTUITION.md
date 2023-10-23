# Intuition

minimum time => try BFS
but what about 2nd min time ?

about green/red flag, if we BFS with time_elapsed we should be able to find the current flag:
`green if (time_elapsed//change) % 2 == 0 else red`

but what about example 2 ?

according to example 2, the 2nd min time is the time we visited 2nd times and time_elapsed is greater than previous, both conditions must be true.

thus, let's record each node's:
1. visited[node]: visited_times
2. distance[node]: time_elapsed from start to node
3. and we only visited node 2nd times when current time_elapsed is greater than previous time.

so, our BFS should be:
```py
while queue:
    t, node = queue.popleft()

    v, m = divmod(t, change)
    is_green = v%2 == 0
    if is_green:
        t = t+time
    else:
        wait = change - m
        t = t+wait+time

    for nei in graph[node]:
        if visited[nei] < 2 and dist[nei] < t:
            visited[nei] += 1
            dist[nei] = t
            queue.append([t, nei])

            if nei == n and visited[nei] == 2:
                return t
```