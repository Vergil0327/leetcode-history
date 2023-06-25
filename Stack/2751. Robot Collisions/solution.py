class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        arr = sorted([[pos, i] for i, pos in enumerate(positions)])
        stack = [] # store moving right robots
        for _, i in arr:
            # moving right robots
            if directions[i] == "R":
                stack.append(i)
                continue

            # moving left robots, start collision
            while stack and healths[i] > 0: # having moving right robots
                if healths[stack[-1]] < healths[i]:
                    healths[stack.pop()] = 0
                    healths[i] -= 1
                elif healths[stack[-1]] > healths[i]:
                    healths[stack[-1]] -= 1
                    healths[i] = 0
                else:
                    healths[stack.pop()] = 0
                    healths[i] = 0
        return [h for h in healths if h > 0]

from sortedcontainers import SortedSet
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(directions)
        
        left, right = SortedSet(), SortedSet()
        for i in range(n):
            if directions[i] == "L":
                left.add((positions[i], healths[i], i))
            else:
                right.add((positions[i], healths[i], i))

        res = [0]*n
        while left:
            p, h, idx = left[0]
            i = right.bisect_right((p, -1, -1))-1
            if i >= 0:
                if right[i][1] == h:
                    right.pop(i)
                    left.pop(0)
                elif right[i][1] > h:
                    left.pop(0)
                    el = right.pop(i)
                    right.add((el[0], el[1]-1, el[2]))
                else:
                    el = left.pop(0)
                    left.add((el[0], el[1]-1, el[2]))
                    right.pop(i)
            else:
                res[idx] = h
                left.pop(0)
        for _, h, idx in right:
            res[idx] = h
            
        return [v for v in res if v > 0]
                    