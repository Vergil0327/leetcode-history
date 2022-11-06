
# if k > 1, it means we can swap any two letter's order in string, so we can just sort the string
# if k == 1, brute force every possible rotated string.

# O(n^2) for rotate with join operation
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(list(s)))

        arr = deque(s)
        
        k = len(arr)
        res = ""
        while k:
            curr = "".join(arr)
            if not res:
                res = curr
            elif curr < res:
                res = curr
            arr.append(arr.popleft())
            k-=1
        return res

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))

        # or one line to find minimum rotated string:
        # return min([s[i:]+s[:i] for i in range(len(s))])
        res = []
        for i in range(len(s)):
            rotatedStr = s[i:]+s[:i]
            res.append(rotatedStr)
        return min(res)