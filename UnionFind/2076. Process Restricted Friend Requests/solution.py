class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def findRestriction(u, v):
            pu, pv = find(u), find(v)
            friends = defaultdict(set)
            for person in range(n):
                p = find(person)
                if p == pu:
                    friends[pu].add(person)
                if p == pv:
                    friends[pv].add(person)

            for x, y in restrictions:
                if x in friends[pu] and y in friends[pv]: return True
                if x in friends[pv] and y in friends[pu]: return True
            
            return False
            
        
        res = [True]*len(requests)
        for i, (u, v) in enumerate(requests):
            pu, pv = find(u), find(v)
            if pu == pv: continue

            if findRestriction(u, v):
                res[i] = False
                continue # found restriction

            if pu <= pv:
                parent[pv] = pu
            else:
                parent[pu] = pv
        return res
