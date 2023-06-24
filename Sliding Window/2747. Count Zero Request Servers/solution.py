class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        size = len(logs)
        logs.sort(key=lambda x:x[1])
        
        m = len(queries)
        res = [0] * m
        l = r = 0
        window = defaultdict(int)
        for q, idx in sorted([(q, i) for i, q in enumerate(queries)]):
            start, end = q-x, q
            
            while r < size and logs[r][1] <= end:
                window[logs[r][0]] += 1
                r += 1
                
            while l < size and logs[l][1] < start:
                window[logs[l][0]] -= 1
                if window[logs[l][0]] == 0:
                    del window[logs[l][0]]
                l += 1

            res[idx] = n-len(window)
        return res