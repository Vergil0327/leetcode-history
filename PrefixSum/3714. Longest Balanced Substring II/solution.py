class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        
        # distinct 1
        ans1 = cur = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            ans1 = max(ans1, cur)

        presumA = [0]
        presumB = [0]
        presumC = [0]
        for i in range(n):
            presumA.append(presumA[-1] + int(s[i] == 'a'))
            presumB.append(presumB[-1] + int(s[i] == 'b'))
            presumC.append(presumC[-1] + int(s[i] == 'c'))
        
        # distinct 2
        # three possible combination: (a,b), (b,c), (a,c)
        ans2 = 0
        positionAB = {}
        positionAC = {}
        positionBC = {}
        for i in range(n+1):
            keyAB = (presumA[i] - presumB[i], presumC[i])
            if keyAB in positionAB:
                j = positionAB[keyAB]
                ans2 = max(ans2, i-j)
            if keyAB not in positionAB:
                positionAB[keyAB] = i
            
            keyAC = (presumA[i] - presumC[i], presumB[i])
            if keyAC in positionAC:
                j = positionAC[keyAC]
                ans2 = max(ans2, i-j)
            if keyAC not in positionAC:
                positionAC[keyAC] = i
            
            keyBC = (presumB[i] - presumC[i], presumA[i])
            if keyBC in positionBC:
                j = positionBC[keyBC]
                ans2 = max(ans2, i-j)
            if keyBC not in positionBC:
                positionBC[keyBC] = i

        # distinct 3
        leftmostIdx = {}
        ans3 = 0
        for i in range(n+1):
            key = (presumB[i] - presumA[i], presumC[i] - presumA[i])
            if key in leftmostIdx:
                j = leftmostIdx[key]
                ans3 = max(ans3, i - j)
            if key not in leftmostIdx:
                leftmostIdx[key] = i
        
        return max(ans1, ans2, ans3)