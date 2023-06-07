class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        def isPal(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1
            return True
        if isPal(a) or isPal(b): return True
        
        # AAA[XXX]BBB
        l, r = 0, n-1
        while l < r and a[l] == b[r]:
            l, r = l+1, r-1
        if l >= r: return True
        if isPal(a[l:r+1]) or isPal(b[l:r+1]): return True # check middle part

        # BBB[XXX]AAA
        l, r = 0, n-1
        while l < r and b[l] == a[r]:
            l, r = l+1, r-1
        if l >= r: return True
        if isPal(a[l:r+1]) or isPal(b[l:r+1]): return True # check middle part

        return False