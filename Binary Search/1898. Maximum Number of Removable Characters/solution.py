class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def checkSubseq(s):
            j = 0
            for ch in s:
                if ch == p[j]:
                    j += 1
                if j == len(p): return True
            return False

        n = len(s)
        l, r = 0, len(removable)
        while l < r:
            mid = r - (r-l)//2
            # The elements in removable are distinct.
            SET = set(removable[:mid])
            newS = ""
            for i in range(n):
                if i in SET: continue
                newS += s[i]
                
            if checkSubseq(newS):
                l = mid
            else:
                r = mid-1
        return l