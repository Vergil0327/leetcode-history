class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        counter1 = Counter(start)
        counter2 = Counter(target)
        if counter1 != counter2: return False

        j = 0
        for i in range(n):
            if target[i] == "L":
                while j < n and start[j] == "_":
                    j += 1

                if (j < n and start[j] == target[i] and j >= i):
                    j += 1
                else:
                    return False
                                    
            elif target[i] == "R":
                while j < n and start[j] == "_":
                    j += 1

                if j < n and start[j] == target[i] and j <= i:
                    j += 1
                else:
                    return False

        return True
