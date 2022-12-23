# Intuition

since description has already told us the next position where we should go:

1. if i-1>=0, i -> i-1
2. if i < n, i -> i+1
3. if i != j anr arr[i] == arr[j], i -> j

we can use BFS to find minimum steps

**performance ?**

we can easily come up BFS with this:

```python
while queue:
    for _ in range(len(queue)):
        curr = queue.popleft()

        if curr == n-1:
            return steps

        if curr-1 >= 0 and visited[curr-1] == 0:
            visited[curr-1] = 1
            queue.append(curr-1)

        if curr+1 < n and visited[curr+1] == 0:
            visited[curr+1] = 1
            queue.append(curr+1)

        for j in val2idx[arr[curr]]:
            if curr == j: continue
            if visited[j] == 1: continue
            visited[j] = 1
            queue.append(j)

    steps += 1
return -1
```

but the problem is we got a nested for-loop to find next `j`.
each time we consider the item in queue, we'll check `val2idx[arr[curr]]` again, and this leads to **O($n^2$)** solution.

**how to solve?**

every time we find `j` for `curr` in `val2idx` hashmap, we'll add **all** the index `j` whose value `arr[j]` is equal to arr[curr].

we don't need to consider curr again anymore because we've add all to the queue.

thus, after we find all the `j` for `curr`, we can directly remove `curr` from `val2idx` to avoid wasting time for check `j` again