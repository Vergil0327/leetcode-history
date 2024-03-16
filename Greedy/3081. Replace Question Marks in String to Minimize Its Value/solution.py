class Solution:
    def minimizeStringValue(self, s: str) -> str:
        count = Counter(s)
        pq = []
        for c in string.ascii_lowercase:
            heapq.heappush(pq, (count[c], c))
        
        replacement = []
        for c in s:
            if c == "?":
                count, ch = heapq.heappop(pq)
                replacement.append(ch)
                heapq.heappush(pq, (count + 1, ch))

        replacement.sort(reverse=True)
        res = ""
        for c in s:
            if c == "?":
                res += replacement.pop()
            else:
                res += c
        return res