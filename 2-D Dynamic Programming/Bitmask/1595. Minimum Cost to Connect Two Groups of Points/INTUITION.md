# Intuition

首先看到這個數據規模: **1 <= size1, size2 <= 12**
馬上先聯想到可以用bitmask來表示選擇狀態, 再來根據題意, 目的是將每個group1, group2的點都相連接

那我們就試著用dfs來分配:

0. let size1, size2 = m, n
1. 我們遍歷group1裡的i-th element, where 0 <= i < m
2. 對於i-th element, 我們將它分配到j-th element in group2, 同時用bitmask來紀錄group2的哪些元素已經被連接過
3. base case: 等到決定完全部m個group1's element, 我們看哪些group2的元素還沒被選過, 將這些連接到cost最低的group1's element
4. 因此我們還額外需要預先處理一個minCostForGroup2

```py
minCost = [inf]*n
for i in range(n):
    for j in range(m):
        minCost[i] = min(minCost[i], cost[j][i])

def dfs(i, state):
    if i == m:
        return sum(minCost[j] for j in range(n) if (state>>j)&1 == 0)

    res = inf
    for j in range(n):
        res = min(res, dfs(i+1, state | (1<<j)) + cost[i][j]) 
    return res
```

時間複雜度為O(m * 2^n * n)


bottom-up比較反直覺, 但只要定義正確也是一樣

- i-th element in group1連接未被選過的group2 element: `dp[i][state] = min(dp[i][state], dp[i-1][state-substate] + cost2[i][substate])`

- i-th element in group1連接已連接的group2 element: 
  - `dp[i][state] = min(dp[i][state], dp[i-1][state] + min([cost[i][j] for j in range(n) if (state>>j)&1 == 0], default=inf))`
  - 但其實也可以無腦的遍歷全部即可, 因為即使這邊選到的j-th element之前已連接過, 也是上面遍歷subset裡的某個case, 並不影響最終結果: `dp[i][state] = min(dp[i][state], dp[i-1][state] + min(cost[i][j] for j in range(n)))`

```py
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        cost = [[0]*m] + cost

        dp = [[inf]*(1<<n) for _ in range(m+1)]
        dp[0][0] = 0

        cost2 = [[0]*(1<<n) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for state in range(1<<n):
                cost2[i][state] = sum(cost[i][j] for j in range(n) if (state>>j)&1)

        for i in range(1, m+1):
            for state in range(1<<n):
                substate = state
                while substate > 0:
                    dp[i][state] = min(dp[i][state], dp[i-1][state-substate] + cost2[i][substate])
                    substate = (substate-1)&state

                minPath = min([cost[i][j] for j in range(n) if (state>>j)&1 == 0], default=inf)
                dp[i][state] = min(dp[i][state], dp[i-1][state] + minPath)
        return dp[m][(1<<n)-1]
```

```py
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        cost = [[0]*m] + cost

        dp = [[inf]*(1<<n) for _ in range(m+1)]
        dp[0][0] = 0

        cost2 = [[0]*(1<<n) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for state in range(1<<n):
                cost2[i][state] = sum(cost[i][j] for j in range(n) if (state>>j)&1)

        for i in range(1, m+1):
            for state in range(1<<n):
                substate = state
                while substate > 0:
                    dp[i][state] = min(dp[i][state], dp[i-1][state-substate] + cost2[i][substate])
                    substate = (substate-1)&state

                minPath = min(cost[i][j] for j in range(n))
                dp[i][state] = min(dp[i][state], dp[i-1][state] + minPath)
        return dp[m][(1<<n)-1]
```