## Top-down + Memorization (Slow)

based on description, at every `i` position, we can choose maximum value as value in whole subarray with at most k length

thus, we just dfs every possibilities

for every `i` position, we can generate arr[i:j] subarray where j from 1 to k-1. and its sum of subarray is `max(arr[i:j]) * (j-i)`

we just choose optimal max value from every recursion to get answer

so the time complexity is `O(n*k^2)`

- recursion height is n
- got k branches at every recursion
- max(subarray) is `O(k)`

### Optimized Step

actually, we can reduce `O(nk^2)` to `O(nk)`

we don't need to recalculate `max(arr[i:j+1])` every single time
we can calculate partial maximum stepwisely