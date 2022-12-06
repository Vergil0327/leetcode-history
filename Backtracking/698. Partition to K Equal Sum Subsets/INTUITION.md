我們直接看TLE的寫法有什麼可以改進的地方

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k

        nums.sort(reverse=True)
        if nums[0] > target: return False
        visited = [False] * len(nums)
        
        def dfs(state, visited, cnt, start):
            if cnt == k: return True
            if state == target:
                return dfs(0, visited, cnt+1, 0)

            for i in range(start, len(nums)):
                if visited[i]: continue
                if state+nums[i]>target: continue
                
                visited[i] = True
                if dfs(state+nums[i], visited, cnt, i+1): return True
                visited[i] = False
            return False
        return dfs(0, visited, 0, 0)
```

可以保留的地方有:

1. 提早判斷是否可以拆分成k個
```python
if total % k != 0: return False
```

2. 如果最大值超過target，那不可能拆分成k個
```python
target = total // k
nums.sort(reverse=True)
if nums[0] > target: return False
```

可以改進的地方有:

當我們發現當下拆分無法成功時，例如{1,4} & {2,3}這組合失敗了
那當我們backtracking回到起始時，會嘗試從{2,3}開始遍歷可能性，然後就會重複計算{2,3} & {1,4}
但其實我們已經知道{1,4} & {2,3}這組合是無法成功的了，所以這邊應該藉由memorization把結果記下

這邊由於 `nums.length <= 16`，所以我們可以用16個bit的**bitmask**來代替array或hashmap來記錄`visited`，
同時bitmast是hashable的，所以可以藉由bitmask把結果記錄下來 (其實就是top-down + memorization)

我們的 `memo` 就可以用bitmask當key，backtracking結果為value來避免重複的計算

```python
memo[bitmask] = canPartition
```

因此本質上這題其實是Top-down + Memorization