# Mirror Generation
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]

        code = [0]
        for i in range(n):
            mirror = [bit | (1<<i) for bit in reversed(code.copy())]
            code = code + mirror
        return code

# Backtracking TLE
class Solution_TLE:
    def grayCode(self, n: int) -> List[int]:
        def diffOneBit(a, b):
            test = a^b
            cnt = 0
            while test:
                cnt += 1
                test &= test-1
                if cnt > 1: return False
            return True

        res = None
        visited = set([0])
        def dfs(state, bit):
            nonlocal res

            if len(state) == 2**n:
                res = state.copy()
                return True

            for i in range(n):
                OR = bit | (1<<i)
                if OR not in visited and diffOneBit(bit, OR):
                    visited.add(OR)
                    if dfs(state + [OR], OR): return True
                    visited.remove(OR)

                XOR = bit ^ (1<<i)
                if XOR not in visited and diffOneBit(bit, XOR):
                    visited.add(XOR)
                    if dfs(state + [XOR], XOR): return True
                    visited.remove(XOR)
            return False
        dfs([0], 0)
        return res