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
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        m = defaultdict(list)
        for num in nums:
            m[num%k].append(num)

        arr = []
        for nums in m.values():
            arr += sorted(nums)

        n = len(arr)

        cache = {}
        def dfs(i, prevIdx):
            if i == n: return 1

            if (i, prevIdx) in cache: return cache[(i, prevIdx)]

            # skip
            cache[(i, prevIdx)] = dfs(i+1, prevIdx)
            # take
            isUgly = arr[i] - arr[prevIdx] == k
            if not isUgly:
                cache[(i, prevIdx)] += dfs(i+1, i)
            return cache[(i, prevIdx)]

        return dfs(0, n-1)-1
```