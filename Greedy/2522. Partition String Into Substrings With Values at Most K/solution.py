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