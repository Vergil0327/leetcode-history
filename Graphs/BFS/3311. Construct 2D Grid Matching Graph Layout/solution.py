class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1

        groups = defaultdict(list)
        for node in range(n):
            groups[indeg[node]].append(node)

        CORNER_DEG = min(groups.keys())
        SIDE_DEG = CORNER_DEG+1
        INSIDE_DEG = SIDE_DEG+1
        
        start_node = groups[CORNER_DEG][0]
        grid = [[start_node]]
        queue = deque([start_node])
        visited = set([start_node])

        if CORNER_DEG == 1: # only 1 row: [start_node, ...]
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for nxt in graph[node]:
                        if nxt in visited: continue
                        visited.add(nxt)
                        grid[0].append(nxt)
                        queue.append(nxt)
            return grid

        END_ROW = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                # check if we found the opposite corner node
                for nxt in graph[node]:
                    if nxt in visited: continue

                    if indeg[nxt] == CORNER_DEG:
                        visited.add(nxt)
                        END_ROW = True
                        grid.append([nxt])
                        break
                if END_ROW: break

                # keep append node in rows
                for nxt in graph[node]:
                    if indeg[nxt] == INSIDE_DEG: continue
                    if nxt in visited: continue
                    visited.add(nxt)
                    
                    queue.append(nxt)
                    grid.append([nxt])
                    break

            if END_ROW:
                break

        queue = deque(grid[i][0] for i in range(len(grid)))
        row = {}
        for r in range(len(grid)):
            row[grid[r][0]] = r
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for nxt in graph[node]:
                    if nxt in visited: continue
                    visited.add(nxt)

                    queue.append(nxt)
                    row[nxt] = row[node]
                    grid[row[node]].append(nxt)
        return grid
