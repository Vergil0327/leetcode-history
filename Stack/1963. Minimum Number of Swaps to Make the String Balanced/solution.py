# Stack
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for c in s:
            if c == "]" and stack and stack[-1] =="[":
                stack.pop()
                continue
            stack.append(c)
        
        n = len(stack)
        pairs = n//2
        return pairs//2 + pairs%2

# Space Optimized
class Solution:
    def minSwaps(self, s: str) -> int:
        currStackSize = 0
        for c in s:
            if c == "[":
                currStackSize += 1
            else:
                if currStackSize > 0: # has more than 1 "["
                    currStackSize -= 1
        
        pairs = currStackSize
        return pairs//2 + pairs%2