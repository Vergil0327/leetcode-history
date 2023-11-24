class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        m = pow(k, n)
        self.res = ""

        def dfs(s, visited):
            if len(visited) == m:
                self.res = s
                return True

            prev = s[len(s) - n + 1 :]
            for d in range(k):
                pwd = prev + str(d)
                if pwd not in visited:
                    if dfs(s + str(d), visited | {pwd}):
                        return True

            return False

        pwd = "0" * n
        visited = set([pwd])
        dfs(pwd, visited)
        return self.res
