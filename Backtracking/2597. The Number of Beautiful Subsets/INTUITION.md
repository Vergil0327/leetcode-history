# Intuition

since the scale is small, `1 <= nums.length <= 20`

$2^{20}$ is about $10^6$ and it's acceptable.

thus, we can backtrack all subset by take-or-skip strategy

1. skip: `dfs(state(i+1))`
2. take only if nums[i]+k not in state and nums[i]-k not in state:
    - we can use hashmap or bitmask to store all the nums[i] we currently have

# Complexity

- time complexity
$$O(2^n)$$

# Optimized

[Smart Arrangement by @votrubac](https://leetcode.com/problems/the-number-of-beautiful-subsets/solutions/3314006/smart-arrangement-vs-bitmask-dfs/?orderBy=most_votes)

for smart arrangement solution:

first we can group nums[i] by its modulo

```py
m = defauldict(list)
for num in nums:
    m[num%k].append(num)
```

then we just do DFS like above but this time we can gain benefit from smart arrangement:

**just compare current nums[i] with previous pick**

1. construct nums back from arrangement in sorted order
```py
arr = []
for nums in m.values():
    arr += nums
```

2. do DFS like above. since valid answer is non-empty subset, final answer is `dfs(0, n-1)-1`

```py
def dfs(i, prevIdx):
    if i == n: return 1
    if i > n: return 0

    isUgly = arr[i] - arr[prevIdx] == k
    if (i, isUgly) in cache: return cache[(i, isUgly)]

    # skip
    cache[(i, isUgly)] = dfs(i+1, prevIdx)
    # take
    if not isUgly:
        cache[(i, isUgly)] += dfs(i+1, i)
    return cache[(i, isUgly)]

return dfs(0, n-1)-1
```


[also like a house rubber @lee215](https://leetcode.com/problems/the-number-of-beautiful-subsets/solutions/3314361/python-house-robber-o-nlogn/)

in a similar way, we still group nums[i] with its modulo with k

then we calculate by group:

```py
count = [Counter() for i in range(k)]
for a in A:
    count[a % k][a] += 1

res = 1
for i in range(k):
    # calculate...
```

for each group, just like smart arrangement, we sort first.

```py
prev, dp0, dp1 = 0, 1, 0
for a in sorted(count[i]):
    # then we have `v` possible subsets for `a`
    v = pow(2, count[i][a])
    # since we want non-empty, valid subsets are `v-1`

    # dp0: not pick a
    # dp1: pick a
    if a-prev == k:
        # if we don't pick a, dp0 = prev_dp0 + prev_dp1
        # if we pick a we can transfer from state which we didn't pick previous a
        # thus, dp0 = prev_dp0 * (v-1)
        dp0, dp1 = dp0+dp1, dp0 * (v-1)
    else:
        # if a is beautiful with previous a
        # dp1 can transfer from prev_dp0 and prev_dp1 and times possible subset of current a
        dp0, dp1 = dp0+dp1, (dp0+dp1) * (v-1)
    
    res *= (dp0+dp1)

return res-1 # must non-empty subset
```


```py
def beautifulSubsets(self, A: List[int], k: int) -> int:
    count = [Counter() for i in range(k)]
    for a in A:
        count[a % k][a] += 1
    res = 1
    for i in range(k):
        prev, dp0, dp1 = 0, 1, 0
        for a in sorted(count[i]):
            v = pow(2, count[i][a])
            if a-prev == k:
                dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
            else:
                dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
            prev = a
        res *= dp0 + dp1
    return res - 1
```