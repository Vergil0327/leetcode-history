class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        MAP = defaultdict(lambda: defaultdict(lambda: inf))
        for i in range(len(original)):
            MAP[original[i]][changed[i]] = min(MAP[original[i]][changed[i]], cost[i])

        @cache # cache 26*26 results
        def dijkstra(s, t):
            if s == t: return 0

            pq = [[0, s]]
            seen = set()
            while pq:
                c, ch = heapq.heappop(pq)
                if ch in seen: continue
                seen.add(ch)
                if ch == t: return c

                for nxt in MAP[ch]:
                    if nxt in seen: continue
                    heapq.heappush(pq, [c+MAP[ch][nxt], nxt])
            return inf
        
        n = len(source)
        res = 0
        for i in range(n):
            c = dijkstra(source[i], target[i])
            if c == inf: return -1
            res += c
        return res