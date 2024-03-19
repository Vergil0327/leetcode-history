class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pos = [-1]*26
        pq = [[-freq, ch] for ch, freq in Counter(tasks).items()]
        heapq.heapify(pq)
        i = 0
        while pq:
            tmp = []
            found = False
            while pq:
                w, t = heapq.heappop(pq)
                ch = ord(t) - ord("A")
                if not found and (pos[ch] < 0 or i-pos[ch] > n):
                    found = True
                    w += 1
                    pos[ch] = i
                    i += 1
                    if w < 0:
                        heapq.heappush(tmp, [w, t])
                else:
                    heapq.heappush(tmp, [w, t])
            if not found:
                i += 1
            pq = tmp
        return i
