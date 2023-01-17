class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(n, curr):
            steps = 0
            n1, n2 = curr, curr+1
            while n1 <= n:
                if n2 <= n:
                    # 1, 2   -> 1
                    # 10, 20 -> 10~19
                    # 100, 200 -> skip 100 ~ 199 steps
                    steps += n2 - n1
                else:
                    # 1, 2
                    # 10, 20
                    # 100, n=147, 200 -> over n, only 147-100 steps can go
                    steps += (n+1)-n1
                n1 *= 10
                n2 *= 10
                
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = countSteps(n, curr)
            if steps <= k:
                # move 1, 10, 100 to 2, 20, 200
                curr += 1
                k -= steps
            else:
                # only can move 1 to 10
                # move 10 to 100 only make k -= 1
                curr *= 10
                k -= 1
        return curr
        