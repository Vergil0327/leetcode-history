def z_function(s):
    """
    z[i] is the length of the longest string that is, at the same time, a prefix of  s and a prefix of the suffix of s starting at i.

    If we compute z-function for p + s, then z[len(p) + i] would be the number of characters from s[i] that match the prefix of p .
    """

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
