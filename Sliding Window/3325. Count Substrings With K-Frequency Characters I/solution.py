class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        count = [0]*26

        l = r = valid = 0
        while r < n:
            key = ord(s[r])-ord("a")
            count[key] += 1
            if count[key] == k:
                valid += 1
            r += 1

            while l < r and valid > 0:
                res += n-(r-1)

                key = ord(s[l])-ord("a")
                if count[key] == k:
                    valid -= 1
                count[key] -= 1
                l += 1

        return res
