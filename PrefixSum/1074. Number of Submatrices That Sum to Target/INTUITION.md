# Intuition

首先想到2-D prefix sum
iterate top row and bottom row
then iterate col to calculate prefix matrix sum

since we want `presum_mat[i][j] - presum_mat[k][j] == target`, use prefix sum with hashmap
=> presum_mat[k][j] = presum_mat[i][j] - target

1. iterate and check if presum_mat[i][j] - target in our hashmap, if it is, res += count of `presum_mat[i][j] - target`
2. at the end of iteration, update hashmap with hashmap[presum_mat[i][j]] += 1

time complexity: 100 * 100 * 100 = 10^6 = O(row * row * col)

core concept:
```py
for top in range(m):
    for bot in range(i, m):
        seen = {0: 1}
        for j in range(n):
            cur = mat_sum[bot][j]-mat_sum[top-1][j]
            if cur-target in seen:
                res += cur[cur-target]
            seen[cur] = seen.get(cur, 0) + 1
```
