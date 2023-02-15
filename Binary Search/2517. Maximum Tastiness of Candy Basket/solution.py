# if maximum tastiness is mid, check if we can greedily pick k prices[i] which abs distance is >= mid in O(n)
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        if len(set(price)) < k: return 0

        price = sorted(list(set(price)))
        n = len(price)

        def check(prices, target):
            cnt = 1
            lastTaken = prices[0]
            for i in range(1, n):
                if prices[i]-lastTaken>=target:
                    cnt += 1
                    lastTaken = prices[i]
            return cnt >= k

        l, r = 0, max(price)-min(price)
        while l < r:
            mid = r - (r-l)//2
            if check(price, mid):
                l = mid
            else:
                r = mid-1
        return l

# Brute Force
class Solution_TLE:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)

        SET = set(price)
        if len(SET) < k: return 0
        price.sort()
        
        memo = {}
        def dfs(state, i):
            if len(state) == k:
                tastiness = inf
                for i in range(1, k):
                    tastiness = min(tastiness, state[i]-state[i-1])
                return tastiness
                
            if len(state) > k or i == n:
                return 0
            
            key = tuple(state + [i])
            if key in memo:
                return memo[key]
            
            tastiness = 0
            tastiness = max(tastiness, dfs(state, i+1))
            tastiness = max(tastiness, dfs(state + [price[i]], i+1))
            
            memo[key] = tastiness
            return memo[key]
        return dfs([], 0)
        