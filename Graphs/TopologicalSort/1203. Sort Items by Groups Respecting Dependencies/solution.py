class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # define each groups's items' order by topological sort
        ## define undefined group first. define any item where its group[item] = -1 in its own group
        groupItems = defaultdict(list)

        nonusedGroupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = nonusedGroupId
                nonusedGroupId += 1
            groupItems[group[i]].append(i)

        ## define item's order for each group
        graph = defaultdict(set)
        indeg = [0] * n
        for i in range(n):
            for j in beforeItems[i]:
                graph[j].add(i)
                indeg[i] += 1

        queue = deque()
        for item, deg in enumerate(indeg):
            if deg == 0:
                queue.append(item)

        sortedGroupItems = [[] for _ in range(nonusedGroupId)]        
        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()

                sortedGroupItems[group[item]].append(item)

                for nxt in graph[item]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        queue.append(nxt)

        graph = defaultdict(set)
        indeg = [0] * len(sortedGroupItems)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]: continue
                if group[i] in graph[group[j]]: continue
                graph[group[j]].add(group[i])
                indeg[group[i]] += 1

        queue = deque()
        for gid, deg in enumerate(indeg):
            if deg == 0:
                queue.append(gid)

        sortedGroups = []
        while queue:
            for _ in range(len(queue)):
                group = queue.popleft()
                sortedGroups.append(sortedGroupItems[group])

                for nxt in graph[group]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        queue.append(nxt)
        
        # construct res by order of topological sort
        res = []
        for sortedGroup in sortedGroups:
            for item in sortedGroup:
                res.append(item)
        return res if len(res) == n else []