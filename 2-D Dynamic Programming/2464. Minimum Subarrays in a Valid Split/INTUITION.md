# Intuition

see example 1

nums = [2,6,3,4,3]

for nums[i]:
X X X [X X I] 
[2,6 | 3,4,3] valid split and dp[1] = 1

X X [X X X I] 
[2 | 6,3,4,3] valid split width dp[0] = inf because [2] is not a valid split

we can define dp[i] as:
**dp[i] : the minimum number of subarrays that we can obtain valid splits in nums[:i]**

for each nums[i], we find a valid j such that nums[j:i] is a valid split and we can transfer dp[i] = dp[j-1] + 1 where j from i to 0

*p.s. j can also be i and nums[j:i] represent as a single nums[i]*

then the answer is `dp[n]` because we want answer when considering nums[:n]

**Base Case**

dp[0] = 0, for empty nums array, the minimum number of subarrays that we can obtain valid splits valid split is **zero**