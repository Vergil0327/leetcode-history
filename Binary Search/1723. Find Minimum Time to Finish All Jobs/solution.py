# Bitmask DP - Python TLE
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        maxState = 1<<n

        # dp[first i people][jobAssignment]
        dp = [[inf]*maxState for _ in range(k+1)]
        dp[0][0] = 0

        workingTimes = [0] * maxState
        for jobState in range(maxState):
            time = 0
            state = jobState
            for j in range(n):
                if state&1:
                    time += jobs[j]
                state >>= 1
            workingTimes[jobState] = time

        for i in range(1, k+1):
            for jobState in range(maxState):
                substate = jobState
                while substate:
                    if dp[i-1][jobState-substate] == inf:
                        substate = (substate-1)&jobState
                        continue

                    dp[i][jobState] = min(dp[i][jobState], max(dp[i-1][jobState-substate], workingTimes[substate]))

                    substate = (substate-1)&jobState

        return dp[k][(1<<n)-1]
    
# Binary Search + DFS: TLE for Python
# DFS遍歷所有可能subset of job_state
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        maxState = 1<<n
        workingTimes = [0] * maxState
        for jobState in range(maxState):
            time = 0
            state = jobState
            for j in range(n):
                if state&1:
                    time += jobs[j]
                state >>= 1
            workingTimes[jobState] = time

        l, r = 1, sum(jobs)
        while l < r:
            mid = l + (r-l)//2

            self.memo = {}
            if self.dfs(mid, (1<<n)-1, 0, workingTimes, k):
                r = mid
            else:
                l = mid+1
        return l

    # threshold: 每個工人最多不超過 threshold 的時間
    # jobState: 必須全部job都分配完
    # workerCount: 目前已經分配給多少個worker
    def dfs(self, threshold, jobState, workerIdx, workingTimes, k):
        if jobState == 0: return True
        if workerIdx == k: return False # 人數用完還沒分配完，返回False

        if (jobState, workerIdx) in self.memo:
            return self.memo[(jobState, workerIdx)]

        substate = jobState
        while substate:
            if workingTimes[substate] <= threshold:
                if self.dfs(threshold, jobState-substate, workerIdx+1, workingTimes, k): return True
            substate = (substate-1)&jobState
        
        self.memo[(jobState, workerIdx)] = False
        return False
    
# Binary Search + Backtracking with highest pruning
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse= True) # prune branches, if we assign largest job ASAP, it'll be more possiblet to trigger over threshold condition and return False

        l, r = 1, sum(jobs)
        while l < r:
            mid = l + (r-l)//2

            workers = [0] * k
            if self.dfs(mid, workers, 0, jobs, k):
                r = mid
            else:
                l = mid+1
        return l
    
    def dfs(self, threshold, workers, jobIdx, jobs, k):
        if jobIdx == len(jobs): return True

        alreadyAssignToFreeTimeWorker = False
        for i in range(k):
            if workers[i]+jobs[jobIdx] > threshold: continue
            if workers[i] == 0:
                if alreadyAssignToFreeTimeWorker:
                    continue
                else:
                    alreadyAssignToFreeTimeWorker = True
            
            workers[i] += jobs[jobIdx]
            if self.dfs(threshold, workers, jobIdx+1, jobs, k): return True
            workers[i] -= jobs[jobIdx]
        return False