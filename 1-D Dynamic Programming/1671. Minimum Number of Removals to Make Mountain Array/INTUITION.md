# Intuition

```
[X X X X X X] X
              i
```

`define dp[i]: the longest length of increasing subsequence considering nums[:i]`
*note. leetcode 300. longest increasing subsequence*

```py
if nums[i] > nums[j]: # nums[i] can append after nums[j]
    dp[i] = max(dp[i], dp[j]+1)
```

then, for i position, the minimum number of elements to remove is `(i+1)-dp[i]` for making nums[:i] increasing when choosing nums[i]

also, we can find longest decreasing subsequenc backwards
`define dp2[i]: the longest length of decreasing subsequence considering nums[i:]`

```py
if nums[j] < nums[i]: # nums[i] can append before nums[j]
    dp[i] = max(dp[i], dp[j]+1)
```

then, for i position, the minimum number of elements to remove is `n-i-dp2[i]` for making nums[i:] decreasing when choosing nums[i]

thus, `min((i+1-dp[i])+(n-i-dp2[i]))` where:
1. i from 1 to n-2 should be answer because of index i (0-indexed) with 0 < i < arr.length - 1
2. prefix_dp[i] > 1 since there must exist nums before nums[i] to make nums[0] < ... < nums[i]
3. suffix_dp[i] > 1 since there must exist nums after nums[i] to make nums[i] > ... > nums[n-1]

should be answer