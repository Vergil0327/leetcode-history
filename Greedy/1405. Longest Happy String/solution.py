class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, [-a, "a"])
        if b > 0:
            heapq.heappush(pq, [-b, "b"])
        if c > 0:
            heapq.heappush(pq, [-c, "c"])

        s = ""
        while pq:
            cnt, ch = heapq.heappop(pq)
            if len(s) > 1 and s[-1] == ch and s[-2] == ch:
                if pq:
                    cnt2, ch2 = heapq.heappop(pq)
                    heapq.heappush(pq, [cnt, ch])
                    s += ch2
                    if (nxt := cnt2+1) < 0:
                        heapq.heappush(pq, [nxt, ch2])
            else:
                s += ch
                if (nxt := cnt+1) < 0:
                    heapq.heappush(pq, [nxt, ch])
        
        return s