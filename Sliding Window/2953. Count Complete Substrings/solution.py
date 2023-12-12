class Solution:
    def countCompleteSubstrings(self, w: str, k: int) -> int:
        def calc(s):
            res = 0
            n = len(s)
            for x in range(1, 27):
                if x * k > n: break
                length = x * k
                cnt = Counter(s[:length])
                freq = Counter(cnt.values())
                
                if freq[k] == x: res += 1
                
                for idx in range(n - length):
                    freq[cnt[s[idx]]] -= 1
                    cnt[s[idx]] -= 1
                    freq[cnt[s[idx]]] += 1

                    freq[cnt[s[idx+length]]] -= 1
                    cnt[s[idx+length]] += 1
                    freq[cnt[s[idx+length]]] += 1

                    if freq[k] == x: res += 1
            return res
        
        n = len(w)
        l = res = 0
        for r in range(1, n):
            if abs(ord(w[r]) - ord(w[r-1])) > 2:
                res += calc(w[l:r])
                l = r
        res += calc(w[l:])
        return res
