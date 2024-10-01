def z_function(s):
    n = len(s)
    l = r = 0
    z = [0]*n

    for i in range(1, n):
        if i < r:
            z[i] = min(r-i, z[i-l])
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i] > r:
            l = i
            r = i+z[i]
    return z

class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)
        z1 = z_function(pattern + s)
        z2 = z_function(pattern[::-1] + s[::-1])
        for i in range(n - m + 1):
            if z1[m + i] + 1 + z2[n - i] >= m:
                return i
        return -1