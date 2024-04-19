class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        connected = defaultdict(list)
        isConnected = [[False]*501 for _ in range(501)]
        for x, y in pairs:
            connected[x].append(y)
            connected[y].append(x)
            isConnected[x][y] = True
            isConnected[y][x] = True

        nodes = list(sorted(connected.keys(), key=lambda x: len(connected[x])))

        n = len(nodes)
        children = defaultdict(list)

        flag = 1
        root = None
        for i in range(n):
            # find father of nodes[i]
            j = i+1
            while j < n and not isConnected[nodes[i]][nodes[j]]:
                j += 1
            if j < n:
                children[nodes[j]].append(nodes[i])
                if len(connected[nodes[i]]) == len(connected[nodes[j]]):
                    flag = 2
            else:
                if root is None:
                    root = nodes[i]
                else:
                    return 0

        visited = set()
        def dfs(node, depth):
            nonlocal flag

            if flag == 0: return -1
            if node in visited: # cycle
                flag = 0
                return -1

            visited.add(node)
            childCnt = 0
            for child in children[node]:
                childCnt += dfs(child, depth+1)

            if childCnt+depth != len(connected[node]):
                flag = 0
                return -1
            return childCnt+1
        dfs(root, 0)
        return flag