# Intuition

核心思想是Longest Increasing Subsequence (LIS)

```
subseq = X X X X X
                 j
subseq = X X X X X X X X X X
                 j
```
nums[i]-nums[subseq[j]] >= i-subseq[j]
=> nums[i]-i >= nums[subseq[j]]-subseq[j]
=> arr[i] >= arr[j]
we ant balanced subsequence in arr where arr[i] >= arr[j]

=> construct arr[i] = nums[i]-i

dp[i]: the maximum sum of balanced subsequence ending at i
dp[i] = max(nums[i] + dp[j]) where nums[i]-i >= nums[j] - j

it would be like:
```py
for i in range(n):
    for j in range(i):
        if arr[i] >= arr[j]:
            dp[i] = max(dp[i], dp[j]+ nums[i])
```

=> Longest Increasing Subsequence (LIS)
=> we can use binary search to find dp[j] in O(logn). (Greedy Approach)

```py
LIS = SortedDict() # index: balanced subseq. sum
for i in range(n):
    if arr[i] <= 0: # only make sum smaller
        res = max(res, nums[i])
    else:
        idx = nums[i]-i
        _sum = nums[i]
        j = LIS.bisect_right(idx)-1
        if j >= 0:
            _sum = max(_sum, LIS[j] + _sum)

        # remove right element with smaller sum
        while j+1 < len(subseq) and subseq.peekitem(j+1)[1] < _sum:
            subseq.popitem(j+1)

        LIS[j] = _sum
        res = max(res, _sum)
return res
```
    