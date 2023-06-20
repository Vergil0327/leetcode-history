# Diff Array
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == "1": return False
        
        diff = [0] * (n+1)

        # base case
        diff[0+minJump] += 1
        diff[0+maxJump+1] += -1

        canReach = 0
        for i in range(1, n):
            canReach += diff[i]

            if s[i] == "1": continue
            if canReach == 0: continue

            if i+minJump <= n:
                diff[i+minJump] += 1 # mark starting point of reachable interval
            if i+maxJump+1 <= n:
                diff[i+maxJump+1] -= 1 # mark ending point of reachable interval
        
        return canReach > 0
    
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        diff = [0] * (n+maxJump+1)
        
        diff[minJump] += 1
        diff[maxJump+1] -= 1

        for i in range(1, n):
            diff[i] += diff[i-1]
            
            if s[i] == "1": continue # can't jump on it
            if diff[i] == 0: continue # can't reach

            # mark reach interval
            diff[i+minJump] += 1
            diff[i+maxJump+1] -= 1

        return diff[n-1] > 0 and s[n-1] == "0"