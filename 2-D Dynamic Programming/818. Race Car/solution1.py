class Solution:
    def racecar(self, target: int) -> int:
        res = 0
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        while queue:
            for _ in range(len(queue)):
                distance, spd = queue.popleft()
                if distance < 0: continue # meaningless to start from distance < 0, must take more steps than start from begining
                if distance == target: return res

                if (nxt := (distance+spd, spd*2)) not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
                if (nxt := (distance, (1 if spd > 0 else -1)*-1)) not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
            res += 1
        return res