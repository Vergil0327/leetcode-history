class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0

        # find all valid integers first
        digits = set([str(k)])
        length = 1
        while length <= len(str(num)):
            nxt = digits.copy()
            for digit in digits:
                for d in range(10):
                    nxt.add(str(d) + digit)
            digits = nxt
            length += 1
        digits = set([int(digit) for digit in digits if int(digit) > 0])
            
        @cache
        def dfs(num):
            if num < 0: return inf
            if num == 0: return 0

            res = inf
            for digit in digits:
                if num >= digit:
                    print(num, digit)
                    res = min(res, dfs(num - digit) + 1)
            return res

        ans = dfs(num)
        return ans if ans < inf else -1
