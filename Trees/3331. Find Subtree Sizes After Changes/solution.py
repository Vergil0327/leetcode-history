class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        newParent = parent.copy()
        n = len(parent)

        for node in range(1, n):
            p = parent[node]
            while p > -1 and s[p] != s[node]:
                p = parent[p]
            if p > -1:
                newParent[node] = p

        children = defaultdict(list)
        for child, p in enumerate(newParent):
            if child > -1:
                children[p].append(child)
        
        res = [0] * n
        def count(node):
            cnt = 1
            for nxt in children[node]:
                cnt += count(nxt)
            res[node] = cnt
            return cnt
        count(0)
        return res
