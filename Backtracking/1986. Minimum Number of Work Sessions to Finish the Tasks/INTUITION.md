# Intuition

看到最多只能`sessionTime`, 並且可以任務的執行順序我們並不在意
首先想到的是看能不能用binary search by value找出minimum number of work sessions

那我們在binary search的pattern下需要的就是那個check helper func該如何實作
```py
l, r = 1, max(tasks)
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

我們helper func `check`要做的是:
`找出 the minimum session time for `mid` work sesstions considering all the tasks`

那要求的就是該如何分配tasks[i]到各個work sessions使得整體需要的session time最短
到這邊看起來有點像是背包分配問題
work session是背包, 而task要分配到各個背包, 最後判斷能不能讓每個背包最多不超過session times
想了想發現check func沒那麼好做

而且到這邊看來, 這題其實是要將任務分配到各個subset使得max(sum(subset))最小
那看來這題是個dp問題, 而且還是個NP-hard問題, 要遍歷所有subset找出最佳解

所以這邊我們定義 dp[assign_state]: minimum number of work session to finish current assignment state for tasks
其中assign_state用bitmask表示, 表示i-th bit表示i-th task有沒有被選來分配到任務中, 如下所示

```
tasks: X O X O X X
       0 1 0 1 0 0
```

所以對於每個dp[assign_state] = min(dp[subset of assign_state] + dp[assign_state - subset])
至於要如何遍歷一個bitmask的subset的話, 有個template就是:

```py
def find_submask(m):
    for bitmask in range(1, 1<<m):
        submask = bitmask
        while submask:
            print(submask)
            submask = (submask-1)&bitmask
```

所以就變成
```py
for state in range(1<<n):
    subset = state
    while subset:
        dp[state] = min(dp[subset] + dp[state-subset])
        subset = (subset-1)&state
```
那最終答案就是看所有任務都分配完後的session time: dp[(1<<n)-1]
另外這個模板的time complexity為: O(3^n)

那**base case**是什麼?
對於所有任務分配, 只要這個subset的總時間 <= sessionTime, 代表我們可以需要1個work session
所以base case就是
```py
for state in range(1<<n):
    time = 0
    for i in range(n):
        if (state>>i)&1:
            time += tasks[i]
    if time <= sessionTime:
        dp[state] = 1
```

# Other Solution - backtracking

*more efficient*

```py
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = res = len(tasks)
        workSess = []

        # pruning branches, 儘早觸發`if workSess[j] + tasks[i] <= sessionTime`
        tasks.sort(reverse=True)
        
        def dfs(i):
            nonlocal res
            # prune branches
            if len(workSess) >= res: return

            if i == n: # 分配完所有tasks
                res = min(res, len(workSess))
                return

            # backtracking
            # 遍歷看有沒有work sesstion還能分配tasks[i]
            for j in range(len(workSess)):
                if workSess[j] + tasks[i] <= sessionTime:
                    workSess[j] += tasks[i]
                    dfs(i+1)
                    workSess[j] -= tasks[i]

            # backtracking
            # 不分配tasks[i]到任何一個既有work session
            workSess.append(tasks[i])
            dfs(i+1)
            workSess.pop()
        dfs(0)
        return res
```