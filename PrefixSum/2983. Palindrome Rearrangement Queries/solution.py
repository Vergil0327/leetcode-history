import string

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)

        l, r = 0, n-1
        diff = [0]
        while l < r:
            diff.append(diff[-1] + int(s[l] != s[r]))
            l, r = l+1, r-1
        
        # [l:r)
        def checkDiffEqual(l, r):
            return diff[r]-diff[l] == 0

        presum = [Counter() for _ in range(n+1)]
        for i in range(1, n+1):
            for ch in string.ascii_lowercase:
                presum[i][ch] = presum[i-1][ch] + (1 if ch == s[i-1] else 0)
        
        # [l:r)
        def checkCountEqual(l, r):
            return presum[r]-presum[l] == presum[n-l] - presum[n-r]
        
        res = []
        for l1, r1, l2, r2 in queries:
            l2, r2 = n-1-r2, n-1-l2

            # convert into [l1,r1) and [l2,r2)
            r1, r2 = r1+1, r2+1

            ok = checkDiffEqual(0, min(l1,l2)) and checkDiffEqual(max(r1,r2), n//2)
            separate = True
            if r1 < l2:
                ok = ok and checkDiffEqual(r1, l2)
            elif r2 < l1:
                ok = ok and checkDiffEqual(r2, l1)
            else:
                separate = False

            if separate:
                ok = ok and checkCountEqual(l1, r1) and checkCountEqual(l2, r2)
            else:
                ok = ok and checkCountEqual(min(l1,l2), max(r1, r2))

                left = presum[r1]-presum[l1]
                right = presum[n-l2]-presum[n-r2]
                
                if l1 < l2:
                    need = presum[n-l1]-presum[n-l2]
                    ok = ok and (left >= need)
                    left -= need
                if l2 < l1:
                    need = presum[l1] - presum[l2]
                    ok = ok and (right >= need)
                    right -= need

                if r1 < r2:
                    need = presum[r2]-presum[r1]
                    ok = ok and right >= need
                    right -= need
                if r2 < r1:
                    need = presum[n-r2]-presum[n-r1]
                    ok = ok and left >= need
                    left -= need

                ok = ok and (left == right)
            res.append(ok)

        return res
