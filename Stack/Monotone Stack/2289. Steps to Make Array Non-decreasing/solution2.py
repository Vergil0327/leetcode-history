class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)

        nextPos = [0] * n
        for i in range(n):
            nextPos[i] = i+1

        queue = deque() # removed interval [l, r]
        for i in range(n-1, 0, -1):
            if nums[i-1] > nums[i]:
                queue.append([i-1, i])

        removed = set()
        step = 0
        while queue:
            for _ in range(len(queue)):
                l, r = queue.popleft()

                if l in removed: continue
                removed.add(r)

                rr = nextPos[r]
                while rr < n and rr in removed:
                    rr = nextPos[rr]
                nextPos[r] = rr # update

                if rr < n and nums[l] > nums[rr]: # keep removing if we found valid nums[rr] for nums[l] to remove
                    queue.append([l, rr])
            step += 1
        return step