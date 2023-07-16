class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        parent[firstPerson] = 0
        res = set([0,firstPerson])

        meetings.sort(key=lambda x:x[2])
        i = 0
        while i < len(meetings):
            currRound = set()
            j = i
            while j < len(meetings) and meetings[j][2] == meetings[i][2]:
                x, y, _ = meetings[j]
                px, py = find(x), find(y)
                currRound.add(x)
                currRound.add(y)
                if px != py: # union to smaller parent
                    if px <= py:
                        parent[py] = px
                    else:
                        parent[px] = py
                j += 1

            # reset union-find if they don't know the secret
            for x in currRound:
                px = find(x)
                if px == 0:
                    res.add(x)
                else:
                    parent[x] = x

            i = j-1
            i += 1
        return res