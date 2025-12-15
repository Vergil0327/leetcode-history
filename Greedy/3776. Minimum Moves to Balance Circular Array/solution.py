"""

1. if sum(balance) < 0: impossible to make all balance[i] >= 0
2. if no negative: just return 0

Note: You are guaranteed that at most 1 index has a negative balance initially.
從negative位置為出發點, 從左右兩方向開始出發即可

"""

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0: return -1
        if all(num >= 0 for num in balance): return 0
        
        n = len(balance)
        j = -1
        for i in range(n):
            if balance[i] < 0:
                j = i
                break

        step = res = 0
        while balance[j] < 0:
            step += 1
            left = balance[((j-step) + n) % n]
            right = balance[(j+step) % n]
            
            units = left + right
            res += min(-balance[j], units) * step
            balance[j] += units
            print(balance)
        return res
