# Intuition

first, I come up with dp solution

dp[i]: the maximum sum of a non-empty subsequence of that array nums[:i] such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

- we can append nums[i] to seq[:j] where i > j and i-j <= k
- or we can start subseq with nums[i] standalone
thus:
```py
def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    
    dp = [-inf] * n
    for i in range(n):
        dp[i] = max(dp[i], nums[i])
        for j in range(i-1, i-k-1, -1):
            dp[i] = max(dp[i], dp[j] + nums[i] if dp[j] != -inf else nums[i])
    return max(dp)
```

but we'll get TLE in O(n^2) time complexity

let's see nested loop, it's a k-size window
```
for j in range(i-1, i-k-1, -1):
    dp[i] = max(dp[i], dp[j] + nums[i] if dp[j] != -inf else nums[i])
```

if we know max(dp[i-k:i-1]), we can update dp[i] = max(dp[i-k:i-1]) + nums[i]
=> maintain a k-1 size window and we want find max(window) in O(1) time complexity
=> use maxHeap

therefore, we can maintain a k-1 size maxHeap to store previous k dp results
1. first pop out invalid dp result in k-1 size maxHeap
```py
while maxHeap and maxHeap[0][1] < i-k:
    heapq.heappop(maxHeap)
```
2. try to update dp with maxHeap
    - `dp[i] = max(dp[i], dp[i] + (-maxHeap[0][0]))`
3. add current dp value to maxHeap.
    - `heapq.heappush(maxHeap, [-dp[i], i])`
