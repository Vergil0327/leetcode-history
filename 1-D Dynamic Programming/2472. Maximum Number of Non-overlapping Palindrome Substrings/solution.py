
# O(n^2), Runtime: 5519 ms, faster than 8.33%
class SolutionBruteForce:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = [] # [l, r] means valid palindrome s[l:r] both inclusive
        for i in range(n):
            l = r = i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 >=k:
                    intervals.append([l, r])
                l, r = l-1, r+1
                
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 >=k:
                    intervals.append([l, r])
                l, r = l-1, r+1
        
        # now the problem become "Find Maximum Number of Non-overlapping Interval"
        
        # Greedy
        # if l in [l, r] larger than previous r', it's valid count
        # if l in [l, r] is smaller than prevoius r' and r is also smaller than r', we can replace previous one
        # -> which means we can update previous r' to r
        res = []
        intervals.sort()
        for l, r in intervals:
            if not res or l > res[-1][1]:
                res.append([l, r])
            elif r < res[-1][1]:
                res[-1][1] = r
        
        return len(res)
