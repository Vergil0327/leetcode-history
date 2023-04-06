# Intuition

first, since we can change arr1[i] with any arr2[j],
we can sort arr2 first and remove duplicates, then we can use binary search to find the best choice for arr1[i] if we want to change arr1[i].

the best choise for changing arr1[i] is to find first arr2[j] which arr2[j] > arr1[i] because arr1 must be strictly increasing.

thus, we can find arr2[j] by this:
```py
j = bisect.bisect_right(arr2, prev)
if j < m:
    dp[i].add((arr2[j], operation+1))
        # we found valid arr2[j] here
```

for each arr1[i] we must check previous value:
- if arr1[i] > previous value: we can use arr1[i] directly and continue next round
- but we can always try to change arr1[i] if there exists a valid arr2[j]
  - because sometimes if arr1[i] is not only greater than arr1[i-1] but also greater than arr1[i+1], arr1[i+2], ..., it's better to change arr1[i] with a valid arr2[j]

thus, for each round, we can choose to change arr1[i] or not
we can store these 2 strategies in current dp[i] state and dp[i] state is:

dp[i]: the current valid state for i-th round and the state definition is (previous value, operation). i.e. dp[i] = {(previous value, operation)}

so, the state transfer is:

```py
for i in range(n):
    if i == 0:
        # we can use arr1[0] directly
        dp[i].add((arr1[i], 0))
        # we can use arr2[0] by operation
        dp[i].add((arr2[0], 1))
        continue
    
    for prev, operation in dp[i-1]:
        # if arr1[i] is valid, we can directly use it
        if arr1[i] > prev:
            dp[i].add((arr1[i], operation))
        
        # try to change arr1[i] with a valid arr2[j]
        j = bisect.bisect_right(arr2, prev)
        if j < m:
            dp[i].add((arr2[j], operation+1))
```

and we can find the final answer in dp[n-1] state:
```py
res = inf
for _, op in dp[n-1]:
    res = min(res, op)
return res if res != inf else -1
```

but this will cause TLE because our dp[i] state might store multiple states with same key but duplicate values, ex.

dp[i] = { {3, 5}, (3, 6), (3, 7), (3, 8), ... }

there are multiple states which previous value is 3 but oprations are different (5, 6, 7, 8).
since we want to find minimum operations, we only need to store minimum operation in our dp[i].
therefore, we can use **Hashmap** to prune states and only store best state amoung these states:

```py
# curr[current_choosing_value, arr1[i] or arr2[j]]: minimum oprations
# if there exists same key but different value, we only store one minimum value
curr = defaultdict(lambda: inf)
for prev, operation in dp[i-1]:
    if arr1[i] > prev:
        curr[arr1[i]] = min(curr[arr1[i]], operation)
        # dp[i].add((arr1[i], operation))
    
    j = bisect.bisect_right(arr2, prev)
    if j < m:
        curr[arr2[j]] = min(curr[arr2[j]], operation+1)
        # dp[i].add((arr2[j], operation+1))
```

# Optimized

但其實上面觀察一下可發現，我們可以不需要有個dp array
每一輪狀態只跟前一輪有關，所以我們僅需兩個hashmap紀錄 {[current choosing value]: operation} 即可

```py
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1:0}
        arr2 = sorted(set(arr2))

        for num in arr1:
            nextDP = collections.defaultdict(lambda: float('inf'))
            for prev in dp:
                if num > prev:
                    nextDP[num] = min(nextDP[num], dp[prev])

                j = bisect.bisect_right(arr2,prev)
                if j < len(arr2):
                    nextDP[arr2[j]] = min(nextDP[arr2[j]], dp[prev]+1)
            dp = nextDP
        if dp:
            return min(dp.values())
        return -1
```