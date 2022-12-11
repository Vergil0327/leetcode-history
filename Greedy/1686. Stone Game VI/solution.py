class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        values = []
        for i in range(n):
            priority = A[i]+B[i]
            values.append([priority, A[i], B[i]])
        values.sort(reverse=True)
        
        isAliceTurn = True
        alice, bob = 0, 0
        for i, value in enumerate(values):
            _, valA, valB = value
            if isAliceTurn:
                alice += valA
            else:
                bob += valB
            isAliceTurn = not isAliceTurn
        
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0