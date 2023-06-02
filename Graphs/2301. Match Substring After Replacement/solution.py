class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        graph = defaultdict(set)
        for u, v in mappings:
            graph[u].add(v)
        
        targets = set()
        n = len(sub)
        for i in range(len(s)-n+1):
            t = s[i:i+n]
            targets.add(t)

        def compare(s, t):
            if not s: return True
            if s[0] == t[0]:
                if compare(s[1:], t[1:]): return True
            for nxt in graph[s[0]]:
                if nxt == t[0]:
                    if compare(s[1:], t[1:]): return True
            return False

        for t in targets:
            # prune same characters
            i = 0
            while i < n and sub[i] == t[i]:
                i += 1
            
            if compare(sub[i:], t[i:]): return True
        return False
