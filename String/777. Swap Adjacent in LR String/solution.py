class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)

        counter1 = Counter(end)
        counter2 = Counter(start)
        if counter1 != counter2: return False

        j = 0
        for i in range(n):
            if end[i] == "L":
                while j < n and start[j] == "X":
                    j += 1

                if not (j < n and start[j] == end[i] and j >= i):
                    return False
                j += 1
                
                    
            elif end[i] == "R":
                while j < n and start[j] == "X":
                    j += 1

                if not (j < n and start[j] == end[i] and j <= i):
                    return False
                j += 1

        return True
