# Bitmask DP

## Intuition

看到數據範圍很小，對多不超過12，典型的狀態壓縮DP題
我們可以將job assignments的狀態表示成二進位，然後把問題想成背包問題

可以定義成 dp[i][job assignment state] = the minimum possible maximum working time of any assignment

當我們考慮完前面i-1個人後，考慮第i個人的狀態轉移為:

我們遍歷所有當前job_state的substate，這時的最大working time為`max(dp[i-1][job_state-substate], workingTime[substate])`

那們當前的dp[i][job_state]就是找出全部可能的最優解，對全部取`min`
`dp[i][job_state] = min(dp[i][job_state], max(dp[i-1][job_state-substate], workingTime[substate]))`

遍歷一個bitmask的所有submask的模板為:

```py
state = ...

substate = state
while substate:
    # do something to substate

    substate = (substate-1)&state
```
substate-1:作用相當於保證不重複
&state:作用相當於保證是state的子集合

而傳統背包問題的框架則為:

```
iterate people:
    iterate all the job_state:
        # update dp state
```

因此為
```py
for i in range(1, k+1):
    for jobState in range(maxState):
        substate = jobState
        while substate:
            # update dp state
            substate = (substate-1)&jobState
```

**base case**

dp[0][0] = 0
dp[0][0以外state] = inf -> 無法分配工作

## Complexity

- time complexity
$$O(k * 3^n)$$

## Optimized Solution

### Binary Search + DFS with Memorization (TLE for python)

我們可以嘗試去猜測`minimum possible maximum working time of any assignment`

search space為: `[1, sum(jobs)]`，最多就是全部分配給同一個工人

那這樣我們只要check當前這個threshold可不可行，只要有任一個可行解存在，那麼這個threshold就是可行解，然後繼續往小裡猜

核心程式碼為:

```py
l, r = 1, sum(jobs)
while l < r:
    mid = l + (r-l)//2

    self.memo = {}
    if self.dfs(mid, (1<<n)-1, 0, workingTimes, k):
        r = mid
    else:
        l = mid+1
return l
```

而我們判斷可不可行的方式就是去DFS看看，把所有工作的可能substate分配給第`workerIdx`人

那就一樣遍歷所有substate，去進行DFS，recursion depth最多就遞歸`k`層

```py
def dfs(self, threshold, jobState, workerIdx, workingTimes, k):
    substate = jobState
    while substate:
        if workingTimes[substate] <= threshold:
            if self.dfs(threshold, jobState-substate, workerIdx+1, workingTimes, k): return True
        substate = (substate-1)&jobState
```

**base case**

- job state能全部分配完, 111...111 -> 0000...0000，代表找到可行解，返回True
- 反之如果直到工人用完都沒找到，那就返回False

然後可以對jobState以及workerIdx進行memorization

### Binary search + Backtracking

再來第二種就是進行backtracking + pruning branches

binary search框架一樣，只是這次是一個個去看job，然後試著分配給n個worker

```py
l, r = 1, sum(jobs)
while l < r:
    mid = l + (r-l)//2

    workers = [0] * k
    if self.dfs(mid, workers, 0, jobs, k):
        r = mid
    else:
        l = mid+1
return l
```

dfs backtracking框架如下:

base case: 如果我們在threshold下將工作全部分配完(jobIdx = len(jobs))，代表找到可行解

backtracking主幹則為，嘗試分配給任一個人

```py
def dfs(self, threshold, workers, jobIdx, jobs, k):
    if jobIdx == len(jobs): return True

    for i in range(k):
            if workers[i]+jobs[jobIdx] > threshold: continue
            
            workers[i] += jobs[jobIdx]
            if self.dfs(threshold, workers, jobIdx+1, jobs, k): return True
            workers[i] -= jobs[jobIdx]
```

但這樣會TLE，但這樣的backtracking比起bitmask + memorization的好處是，會比較好剪枝

**Pruning Stategy**

1. 首先能做的是對jobs由大到小排序
> 這樣做的好處是，優先分配大的，越容易觸發`if workers[i]+jobs[jobIdx] > threshold: continue`這個條件

2. 第二種則是一個相當高效率的剪枝策略

> 對於每個空閑的工人來說，也就是當前workerTime為零的人，你分配給任意一個這樣的人來說結果都是一樣的

>如果有三個空閑的人，你分配給第一位如果失敗了，那你在分配給第二位跟第三位也一樣會失敗，因為指示分配的人調換了一下而已

>所以我們可以給個flag，如果我們之前已經分配給空閑的人過了後，那就跳過，如果還沒那就繼續，然後標記一下flag為True

>這樣的話如果有k個人，我們直接就減少了`k-1`個分支，是個相當高效的剪枝策略

這樣的策略能用在這類型的分配任務情況
