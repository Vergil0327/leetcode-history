class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = list(Counter(nums).values())
        n, m = len(counter), len(quantity)

        # dp[i][bitmask of cumstomers]: whether we can satisfy all the customers by using first i nums
        # 50 unique values at most and 10 customers as bitmask
        dp = [[False] * (2**10) for _ in range(51)]

        # shift counter to 1-indexed
        counter = [0] + counter
        
        # base case
        # dp[0][bitmask]
        dp[0][0] = True
        
        # dp[i][0]
        for i in range(1, n+1):
            dp[i][0] = True

        masksum = defaultdict(int)
        for mask in range(1<<m):
            for i in range(m):
                if (mask>>i)&1:
                    masksum[mask] += quantity[i]

        # dp[i][bitmask] = True if and only if
        # 1. count[i] satisfy a submask of bitmask
        # 2. use first i-1 nums to satisfy bitmask-submask -> dp[i-1][bitmask-submask] = True
        for i in range(1, n+1):
            for bitmask in range(1, 1<<m):
                if dp[i-1][bitmask]:
                  dp[i][bitmask] = True
                  continue

                # 遍歷bitmask subset的模板
                submask = bitmask
                while submask:
                    if not dp[i-1][bitmask-submask]:
                        submask = (submask-1)&bitmask
                        continue
                    
                    if self.check(counter[i], masksum[submask]):
                    # if self.canSatisfySubmask(counter[i], quantity, submask):
                        dp[i][bitmask] = True
                        break
                    submask = (submask-1)&bitmask

        return dp[n][(1<<m)-1]

    def canSatisfySubmask(self, count, quantity, submask):
        total = 0
        for i in range(len(quantity)):
            if (submask>>i)&1:
                total += quantity[i]
        return count >= total

    def check(self, count, masksum):
        return count >= masksum