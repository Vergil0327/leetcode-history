class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)

        # O(26n)
        counters = [defaultdict(int) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(26):
                counters[i][j] = counters[i-1][j]
            counters[i][ord(s[i-1])-ord("a")] += 1

        res = []
        for l, r, k in queries:
            remain = 0
            counter = Counter()
            for i in range(26):
                counter[i] = counters[r+1][i]-counters[l][i]
                
                remain += counter[i]%2

            res.append(remain//2 <= k)
        return res