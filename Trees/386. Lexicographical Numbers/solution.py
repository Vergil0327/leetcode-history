class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(num, n):
            if num <= n:
                res.append(num)
                for i in range(10):
                    dfs(num*10+i, n)

        for i in range(1, 10):
            dfs(i, n)
        return res