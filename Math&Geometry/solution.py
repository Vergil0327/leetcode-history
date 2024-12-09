isPrime = [False, False] + [True] * 100000
for f in range(2, int(sqrt(len(isPrime)))+1):
    if isPrime[f]:
        for j in range(f*f, len(isPrime), f):
            isPrime[j] = False

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if isPrime[n] or isPrime[m]: return -1
        
        s, t = str(n), str(m)
        
        pq = [[n, s]]
        visited = set()
        while pq:
            cst, s = heapq.heappop(pq)
            if s in visited: continue
            visited.add(s)
            if s == t: return cst

            for i in range(len(s)):
                pre, suf = s[:i], s[i+1:]
                d = int(s[i])
                if d < 9:
                    ss = pre + str(d+1) + suf
                    if ss not in visited and not isPrime[int(ss)]:
                        heapq.heappush(pq, [cst + int(ss), ss])
                if d > 0 and not (leadingZero := i==0 and d==1):
                    ss = pre + str(d-1) + suf
                    if ss not in visited and not isPrime[int(ss)]:
                        heapq.heappush(pq, [cst + int(ss), ss])
        return -1