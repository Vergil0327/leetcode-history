# TLE
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        self.res = [0, n + 1]
        count = [0] * (max(nums) + 1)
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
                if child == parent:
                    continue
                self.distance.append(length)
                dfs(child, r, dist + length, duplicate, l)
                self.distance.pop()

            # backtracking: since `l` should back to original position `cur`, we also need to update count[nums[path[j]]] where j from `l` back to `cur`
            self.path.pop()
            count[nums[r]] -= 1
            for i in range(l - 1, originalPos - 1, -1):
                count[nums[self.path[i]]] += 1

        dfs(0, -1, 0, 0, 0)

        return self.res


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        self.res = [0, 1]
        graph = defaultdict(list)
        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        curpath = []
        last = defaultdict(lambda: -1)

        def dfs(node, parent, curr_cost, seen):
            lastcolor = last.get(nums[node], -1)
            last[nums[node]] = len(curpath)
            curpath.append(curr_cost)

            start = seen[0]  # first allowed index

            m = len(curpath)
            if (new_cost := curr_cost - curpath[start]) > self.res[0]:
                self.res[0] = new_cost
                self.res[1] = m - start
            elif new_cost == self.res[0]:
                self.res[1] = min(self.res[1], m - start)

            for nxt, cost in graph[node]:
                if nxt == parent:
                    continue

                nextstart = seen
                if last[nums[nxt]] != -1 and start <= last[nums[nxt]]:
                    nextstart = seen + [last[nums[nxt]] + 1]

                dfs(nxt, node, curr_cost + cost, sorted(nextstart)[-2:])

            last[nums[node]] = lastcolor
            curpath.pop()

        dfs(0, -1, 0, [0, 0])
        return self.res


class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        maxLength = 0
        minNodes = 1
        graph = [[] for _ in range(len(nums))]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        prefix = [0]
        lastSeenDepth = {}

        def dfs(
            node: int,
            parent: int,
            leftBoundary: list[int],
        ) -> None:
            nonlocal maxLength, minNodes
            prevDepth = lastSeenDepth.get(nums[node], 0)
            lastSeenDepth[nums[node]] = len(prefix)

            if prevDepth != 0:
                leftBoundary = sorted(leftBoundary + [prevDepth])[-2:]

            length = prefix[-1] - prefix[leftBoundary[0]]
            nodes = len(prefix) - leftBoundary[0]
            if length > maxLength or (length == maxLength and nodes < minNodes):
                maxLength = length
                minNodes = nodes

            for nxt, w in graph[node]:
                if nxt == parent:
                    continue
                prefix.append(prefix[-1] + w)
                dfs(nxt, node, leftBoundary)
                prefix.pop()

            lastSeenDepth[nums[node]] = prevDepth

        dfs(0, -1, [0, 0])
        return [maxLength, minNodes]
