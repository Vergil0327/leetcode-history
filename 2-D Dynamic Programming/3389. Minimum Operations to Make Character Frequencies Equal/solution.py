class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch)-ord("a")] += 1
        
        @cache
        def dfs(ch, target, deletion):
            if ch == 26: return 0

            cnt = freq[ch]
            
            if cnt > target:
                delete = cnt-target
                return dfs(ch+1, target, delete) + delete # op.2: deletion
            elif cnt < target:
                need = target-cnt

                # op.1: insertion
                res = dfs(ch+1, target, 0) + need

                # op.2: delete to 0
                res = min(res, dfs(ch+1, target, cnt) + cnt)
                
                # op.3: change ch-1 deletion to ch
                res = min(res, dfs(ch+1, target, 0) + (need-min(deletion, need)))
                return res
            else: # already equals target
                return dfs(ch+1, target, 0)

        return min(dfs(0, t, 0) for t in range(max(freq)+1))
