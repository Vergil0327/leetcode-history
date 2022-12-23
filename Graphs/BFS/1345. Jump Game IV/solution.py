class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        val2idx = defaultdict(list)
        for i, v in enumerate(arr):
            val2idx[v].append(i)

        queue = deque([0])
        visited = [0] * 50004
        visited[0] = 1
        steps = 0
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
                del val2idx[arr[curr]]

            steps += 1
        return -1