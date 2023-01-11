class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        canRemoved = k
        for c in num:
            while canRemoved > 0 and stack and stack[-1] > c:
                stack.pop()
                canRemoved -= 1
            stack.append(c)
        
        while canRemoved:
            stack.pop()
            canRemoved -= 1
        
        res = "".join(stack)
        
        # remove leading zeros
        i = 0
        while i < len(res) and res[i] == "0":
            i += 1
        res = res[i:]

        return res if res else "0"