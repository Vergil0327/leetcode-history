class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrerequisites = [set() for _ in range(numCourses)]

        # topological sort template
        G = defaultdict(list)
        indegrees = [0] * numCourses
        for u, v in prerequisites:
            indegrees[v] += 1
            G[u].append(v)
            isPrerequisites[v].add(u)

        queue = deque()
        for node, deg in enumerate(indegrees):
            if deg == 0:
                queue.append(node)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for nxt in G[node]:
                    indegrees[nxt] -= 1
                    isPrerequisites[nxt] |= isPrerequisites[node] # gather information. union its prerequisite's prerequisite
                    if indegrees[nxt] == 0:
                        queue.append(nxt)
        res = []
        for u, v in queries:
            if u in isPrerequisites[v]:
                res.append(True)
            else:
                res.append(False)
        return res