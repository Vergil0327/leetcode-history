class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n < 2: return False
        
        # spirally outward
        i = 2
        while i < n and distance[i] > distance[i-2]:
            i += 1
        if i == n: return False

        diff = abs(distance[i-2]-(distance[i-4] if i-4 >= 0 else 0))
        if distance[i] >= diff: # next i+1 edge should be less than distance distance[i-1] - distance[i-3]
            distance[i-1] = distance[i-1] - (distance[i-3] if i-3 >= 0 else 0)
            
            i += 1
            while i < n and distance[i] < distance[i-2]:
                i += 1
            if i == n: return False
            
            return True
        else:
            while i < n and distance[i] < distance[i-2]:
                i += 1
            if i == n: return False
            return True

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n < 2: return False
        
        # spirally outward
        i = 2
        while i < n and distance[i] > distance[i-2]:
            i += 1
        if i == n: return False

        diff = abs(distance[i-2]-(distance[i-4] if i-4 >= 0 else 0))

        # type II case
        if distance[i] >= diff: # next i+1 edge should be less than distance distance[i-1] - distance[i-3]
            distance[i-1] = distance[i-1] - (distance[i-3] if i-3 >= 0 else 0)
            i += 1

        # type I spirally move inward
        while i < n and distance[i] < distance[i-2]:
            i += 1
        if i == n: return False
        
        return True