class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        n = len(nums)

        queue = deque([(start, 0)])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                x, step = queue.popleft()

                if x == goal: return step
                if x < 0 or x > 1000 or x in visited: continue
                visited.add(x)

                for i in range(n):
                    queue.append((x+nums[i], step+1))
                    queue.append((x-nums[i], step+1))
                    if nums[i] > 0:
                        queue.append((x^nums[i], step+1))
        return -1