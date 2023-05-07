class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        colors = defaultdict(int)
        
        cnt = 0
        for idx, color in queries:
            prev = colors[idx]
            if color == prev:
                res.append(cnt)
                continue

            if prev != 0:
                if prev == colors[idx-1]:
                    cnt -= 1
                if prev == colors[idx+1]:
                    cnt -= 1
            
            colors[idx] = color            
            if color == colors[idx-1]:
                cnt += 1
            if color == colors[idx+1]:
                cnt += 1
            res.append(cnt)
        return res
