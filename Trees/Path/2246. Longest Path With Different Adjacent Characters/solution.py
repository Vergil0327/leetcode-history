class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if not parent: return 0

        n = len(s)
        children = [[] for _ in range(n)]
        for i in range(n):
            if parent[i] != -1:
                children[parent[i]].append(i)
        
        longest = 1
        def dfs(node):
            nonlocal longest
            if not children[node]:
                return 1

            pathLens = []
            for child in children[node]:
                pathLen = dfs(child)
                if s[child] != s[node]:
                    pathLens.append(pathLen)

            pathLens.sort(reverse=True)
            longest = max(longest, sum(pathLens[:2])+1)

            return pathLens[0] + 1 if pathLens else 1
        dfs(0)
        
        return longest

# 2023/02/17
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(list)
        for child, p in enumerate(parent):
            if p != -1:
                children[p].append(child)

        res = 0
        def dfs(node, parent):
            nonlocal res
            
            maxPath = secondPath = 0
            for child in children[node]:
                if child == parent: continue

                path = dfs(child, node)
                if s[node] == s[child]: continue
                if path > maxPath:
                    secondPath = maxPath
                    maxPath = path
                elif path > secondPath:
                    secondPath = path
            
            pathWithNode = maxPath + secondPath + 1
            res = max(res, pathWithNode)
            return maxPath + 1 # max path + self

        dfs(0, -1)
        return res