class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.m = m = n.bit_length()
        # dp[i][node]: the 2^i-th ancestor of node
        self.dp = dp = [[-1]*n for _ in range(m+1)]
        for node in range(n):
            dp[0][node] = parent[node]

        for i in range(1, m+1):
            for node in range(n):
                p = dp[i-1][node]
                
                dp[i][node] = -1 if p == -1 else dp[i-1][p]


    # represent k as binary form
    # 2^a + 2^b + 2^c + ...
    # ...101010101...
    def getKthAncestor(self, node: int, k: int) -> int:
        m = self.m

        for i in range(m):
            if (k>>i)&1:
                node = self.dp[i][node]
                if node == -1: return -1
        
        return node
        