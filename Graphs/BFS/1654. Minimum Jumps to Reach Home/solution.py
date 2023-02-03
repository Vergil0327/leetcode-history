class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        stops = set(forbidden)
        if x in stops: return -1

        visited = set([(0, False)])

        maxForbidden = -inf
        for v in forbidden:
            maxForbidden = max(maxForbidden, v)
            visited.add((v, True))
            visited.add((v, False))
        rightLimit = max(maxForbidden, x) # we don't need to go right if we're over limit
        
        jumps = 0
        queue = deque([(0, False)]) # x-position, 0 means previous is forward jump and True/False means previous is backward jump or not
        while queue:
            for _ in range(len(queue)):
                curr, didBackward = queue.popleft()
                if curr == x: return jumps

                if curr - b <= rightLimit and (curr+a, False) not in visited:
                    visited.add((curr+a, False))
                    queue.append((curr+a, False))

                if (curr-b, True) not in visited and not didBackward and curr-b>=0:
                    visited.add((curr-b, True))
                    queue.append((curr-b, True))
            jumps += 1

        return -1