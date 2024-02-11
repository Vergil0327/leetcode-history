class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
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

        z = z_function(word)
        t = 1
        n = len(word)
        while k*t < n:
            # if word[k*t:] == word[:n-k*t]:
            #     return t
            if z[k*t] >= n-k*t:
                return t

            t += 1

        return t
