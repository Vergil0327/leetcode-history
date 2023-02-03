from collections import defaultdict
from typing import List

# Brute Force, Backtracking
class BacktrackingSolution:
    def minTransfer(self, transactions: List[List[int]]) -> int:
        bill = defaultdict(int)
        for u, v, money in transactions:
            bill[u] -= money
            bill[v] += money

        account = []
        for money in bill.values():
            if money != 0:
                account.append(money)

        res = float("inf")
        def dfs(account, i, count):
            nonlocal res
            while i < len(account) and account[i] == 0:
                i += 1
            
            if i == len(account):
                res = min(res, count)
                return

            for j in range(i+1, len(account)):
                if account[j] * account[i] < 0:
                    account[j] += account[i]
                    dfs(account, i+1, count+1)
                    account[j] -= account[i]
        dfs(account, 0, 0)
        return res

class DpSolution:
    def minTransfer(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)
        for tx in transactions:
            balance[tx[0]] += tx[2]
            balance[tx[1]] -= tx[2]

        nums = []
        for num in balance.values():
            nums.append(num)

        n = len(nums)
        SUM = [0] * (1<<n) # use bitmask to represent balance state
        for state in range(1<<n):
            for i in range(n):
                if (state>>i)&1:
                    SUM[state] += nums[i]

        dp = [float("inf")] * (1<<n)
        dp[0] = 0

        for state in range(1, 1<<n):
            if SUM[state] != 0: continue
            dp[state] = bin(state).count("1")-1 # n個人僅需要n-1次交易清償債務

            # 遍歷 submask的模板為:
            submask = state
            while submask > 0:
                if SUM[submask] == 0:
                    dp[state] = min(dp[state], dp[submask] + dp[state-submask])
                submask = (submask-1)&state
        return dp[(1<<n) - 1]
