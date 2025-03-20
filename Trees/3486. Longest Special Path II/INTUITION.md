# Intuition

其實這題想法很直覺, 但就是不好實作
這題其實就是在Tree DFS Traversal下進行sliding window
然後對於每個合法sliding window都試著更新答案

比較直覺的寫法會TLE

那後來看到其他python解答發現, 可以只存近兩個位置即可, 並透過排序來找出最小的兩個位置來優化整體時間

```py
# TLE
def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
    n = len(nums)
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    self.res = [0, n+1]
    count = [0] * (max(nums)+1)
    self.path, self.distance = [], []
    def dfs(r, parent, dist, duplicate, l):
        self.path.append(r)
        originalPos = l

        # check if current sliding window is invalid
        count[nums[r]] += 1
        if count[nums[r]] >= 2:
            duplicate += 1 

            while duplicate >= 2:
                if count[nums[self.path[l]]] != 1:
                    duplicate -= 1
                count[nums[self.path[l]]] -= 1
                dist -= self.distance[l]
                l += 1

        # try updating result with current valid window 
        m = len(self.path)
        if dist > self.res[0]:
            self.res[0] = dist
            self.res[1] = m - l
        elif dist == self.res[0] and m - l < self.res[1]:
            self.res[1] = m - l

        # backtracking
        for child, length in graph[r]:
            if child == parent: continue
            self.distance.append(length)
            dfs(child, r, dist + length, duplicate, l)
            self.distance.pop()

        # backtracking: since `l` should back to original position `cur`, we also need to update count[nums[path[j]]] where j from `l` back to `cur`
        self.path.pop()
        count[nums[r]] -= 1
        for i in range(l-1, originalPos-1, -1):
            count[nums[self.path[i]]] += 1

    dfs(0, -1, 0, 0, 0)
    
    return self.res
```