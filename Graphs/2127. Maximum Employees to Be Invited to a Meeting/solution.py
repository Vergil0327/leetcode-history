class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for fav in favorite:
            indegree[fav] += 1

        visited = [False] * n
        listSize = [1] * n
        queue = deque() # [person, # of persons sits in long rectangle table (in linear)]
        for person, deg in enumerate(indegree):
            if deg == 0:
                visited[person] = True
                queue.append(person)
        
        while queue:
            for _ in range(len(queue)):
                person = queue.popleft()

                fav = favorite[person]
                
                indegree[fav] -= 1
                if indegree[fav] == 0:
                    visited[fav] = True
                    queue.append(fav)
                listSize[fav] = listSize[person]+1
                
        cycle = 0
        twoList = 0
        for i in range(n):
            if visited[i]: continue

            # iterate through cycle
            person = i
            cnt = 0
            while not visited[person]:
                visited[person] = True
                cnt += 1
                person = favorite[person]

            if cnt >= 3:
                cycle = max(cycle, cnt)
            elif cnt == 2: # two list
                twoList += listSize[i]+listSize[favorite[i]]

        return max(cycle, twoList)
