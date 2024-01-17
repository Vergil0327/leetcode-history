class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        left_cost = [inf for _ in range(n)]
        right_cost = [inf for _ in range(n)]

        for i in range(n):
            if s[i] == "1":
                left_cost[i] = min((left_cost[i-1] if i-1 >= 0 else 0)+2, i+1)
            else:
                left_cost[i] = (left_cost[i-1] if i-1 >= 0 else 0)

        for i in range(n-1, -1, -1):
            if s[i] == "1":
                right_cost[i] = min((right_cost[i+1] if i+1 < n else 0)+2, n-i)
            else:
                right_cost[i] = (right_cost[i+1] if i+1 < n else 0)
            
        res = min(right_cost[0], left_cost[n-1])
        for i in range(n-1):
            res = min(res, left_cost[i]+right_cost[i+1])
        
        return res
