# BFS
class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if target > jug1 + jug2: return False

        # make jug1 > jug2
        if jug1 < jug2:
            jug1, jug2 = jug2, jug1

        queue = deque([(0,0)]) # initial state of [jug1, jug2]
        
        visited = set([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if x == target or y == target or x+y == target:
                return True

            nxtState = set()
            nxtState.add((jug1, y)) # fill jug1
            nxtState.add((x, jug2)) # fill jug2
            nxtState.add((0, y))    # empty jug1
            nxtState.add((x, 0))    # empty jug2

            # pour jug2 to jug1
            if x+y < jug1:
                nxtState.add(((x+y), 0))
            else:
                nxtState.add( (jug1, y-(jug1-x)) )

            # pour jug1 to jug2
            if x+y < jug2:
                nxtState.add((0, x+y))
            else:
                nxtState.add((jug1-(jug2-y), jug2))
            
            # BFS
            for state in nxtState:
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
            
        return False

# Math
class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if jug1 == target or jug2 == target or jug1+jug2 == target: return True
        if target > jug1+jug2: return False

        def GCD(a, b):
            while b:
                a, b = b, a%b
            return a
        return target%GCD(jug1, jug2) == 0