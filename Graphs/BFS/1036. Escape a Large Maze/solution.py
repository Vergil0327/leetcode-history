class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        walls = set()
        for b in blocked:
            walls.add(tuple(b))
        def check(src, dst):
            queue = deque([src])
            visited = set()
            dirs = [[-1, 0], [1,0], [0, 1], [0, -1]]
            n = 10**6

            worst = len(blocked) * len(blocked) / 2
            
            while queue:
                x, y = queue.popleft()
                
                if (x, y) in walls: continue
                if (x, y) in visited: continue
                visited.add((x, y))

                if len(visited) > worst or (x, y) == dst:
                    return True

                for dx, dy in dirs:
                    xx, yy = x+dx, y+dy
                    if xx < 0 or xx >= n or yy < 0 or yy >= n: continue
                    if (xx, yy) in walls: continue
                    if (xx, yy) in visited: continue
                    queue.append([xx, yy])

            return False

        return check(source, tuple(target)) and check(target, tuple(source))
