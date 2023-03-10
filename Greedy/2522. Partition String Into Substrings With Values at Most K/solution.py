class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        l, r = 0, 0
        cnt = 0
        while r < len(s):
            r += 1
            
            if int(s[l:r]) > k: return -1
            while r < len(s) and int(s[l:r+1]) <= k:
                r += 1
            cnt += 1
            l = r
        return cnt




class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)

        cnt = 0
        num = 0
        for i in range(n):
            nxt = num*10 + int(s[i])
            if nxt <= k:
                num = nxt
            else:
                num = int(s[i])
                if num > k: return -1
                cnt += 1
        return cnt+1
