# Intuition

brute force:
```py
def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)

    res = inf
    for num2 in itertools.permutations(nums2, n):
        tot = 0
        for i in range(n):
            tot += nums1[i]^num2[i]
        res = min(res, tot)
    return res
```

但這樣會TLE, 由於:
- n == nums1.length
- n == nums2.length
- 1 <= n <= 14

所以我們可以嘗試所有subset of nums2來跟nums1得出XOR sum, 並用bitmask DP來以空間換取時間
求出minimum XOR sum

我們定義def dfs(i, state): return the minimum XOR sum for nums1[:i] with pick state is `state`

我們可以用bitmask來表示我們nums2選取的狀態

ex. if state = 0100, it means we've already pick nums2[2]
ex. if state = 0111, it means we've already pick nums2[0],nums2[1],nums2[2]

```py
@cache
def dfs(i, state):
    if i >= n: return 0
    
    res = inf
    for j in range(n):
        if (state>>j)&1 == 1: continue
        res = min(res, dfs(i+1, state|(1<<j)) + (nums1[i]^nums2[j]))
    return res
```

*note. 這邊有個小細節要注意是`(nums1[i]^nums2[j])`必須加括號*

> `dfs(i+1, state|(1<<j)) + (nums1[i]^nums2[j])` **!=** `dfs(i+1, state|(1<<j)) + nums1[i]^nums2[j]`