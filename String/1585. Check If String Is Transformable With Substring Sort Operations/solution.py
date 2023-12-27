class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)
        pos = [deque() for _ in range(10)]
        for i in range(n):
            pos[int(s[i])].append(i)

        for i in range(n):
            digit = int(t[i])
            if not pos[digit]: return False
            
            idx = pos[digit][0]
            for d in range(digit):
                if pos[d] and pos[d][0] < idx: return False
            
            pos[digit].popleft()
        return True