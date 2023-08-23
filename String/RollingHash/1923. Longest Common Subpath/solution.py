class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        mod = 10**11 + 7
        paths.sort(key=lambda x: len(x))
        powmod = [pow(n, i, mod) for i in range(len(paths[0]))]

        def checkLCS(mid):
            candidates = set()

            # rolling hash
            res = 0
            for i in range(mid):
                res += paths[0][i] * powmod[mid-i-1] # precompute pow(n, mid-i-1, mod)
                res %= mod
            candidates.add(res)
            for i in range(mid, len(paths[0])):
                res -= paths[0][i-mid] * powmod[mid-1] # pow(n, mid-1, mod)
                res *= n
                res += paths[0][i]
                res = (res + mod)%mod
                candidates.add(res)

            for i in range(1, len(paths)):
                nxt = set()

                # rolling hash
                res = 0
                for j in range(len(paths[i])):
                    if j < mid:
                        res += paths[i][j] * powmod[mid-j-1] # pow(n, mid-j-1, mod)
                    else:
                        res -= paths[i][j-mid] * powmod[mid-1] # pow(n, mid-1, mod)
                        res *= n
                        res += paths[i][j]
                    res = (res + mod)%mod
                    if j >= mid-1 and res in candidates:
                        nxt.add(res)
                    
                if not nxt: return False
                candidates = nxt

            return True

        l, r = 0, len(paths[0])
        while l < r:
            mid = r - (r-l)//2
            if checkLCS(mid):
                l = mid
            else:
                r = mid-1
        return l
