class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        
        res = 0
        totStates = 1<<n
        def checkContradiction(good, bad):
            for i in range(n):
                for j in range(n):
                    if i in good:
                        if (statements[i][j] == 1 and j in bad) or (statements[i][j] == 0 and j in good):
                            return False
            return True
        
        for state in range(totStates):
            good, bad = set(), set()
            for i in range(n):
                if (state>>i)&1:
                    good.add(i)
                else:
                    bad.add(i)

            if checkContradiction(good, bad):
                res = max(res, len(good))
        return res

