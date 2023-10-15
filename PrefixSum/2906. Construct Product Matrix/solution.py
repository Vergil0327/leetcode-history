class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        vals = [v for row in grid for v in row]
        
        length = len(vals)
        prefix = [1]*length
        for i in range(length):
            prefix[i] = (prefix[i-1] if i-1>=0 else 1) * vals[i] % mod

        suffix = [1] * length
        for i in range(length-1, -1, -1):
            suffix[i] = (suffix[i+1] if i+1 < length else 1) * vals[i] % mod

        res = []
        rows = []
        for i in range(length):
            p = prefix[i-1] if i-1 >= 0 else 1
            s = suffix[i+1] if i+1 < length else 1
            rows.append(p*s%mod)
            if len(rows) == n:
                res.append(rows)
                rows = []

        return res