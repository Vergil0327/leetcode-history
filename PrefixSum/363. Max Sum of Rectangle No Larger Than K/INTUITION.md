# Intuition

固定row_i作為當前上界，然後遍歷 M * N 找出矩形和，也就是prefix sum

對於每一個row_j來說，我們可以得到每個column的值

`我們目標是找到 prefixSum[j] - prefixSum[i] <= k，並且越接近k越好`

我們在row_j裡疊加的`currSum += column[i]`就是prefixSum[j]
因此我們往前找一個prefixSum[i]使得 prefixSum[i] >= prefixSum[j] + k
也就是當我們持續維護一個有序`prefixSums`的array時，可以用binary search透過 currSum+k找出prefixSum[i]

一但找到一個合法的prefixSum[i](也就是idx != len(`prefixSums`)時)，即可更新:
`res = max(res, currSum - prefixSum[i])`

並持續把當前的currSum(也就是prefixSum[j])加入到`prefixSums` array裡

有個要特別注意的點是，`prefixSums`裡面必須事先加入`0`
因為prefixSum[j]-prefixSum[i]中的prefixSum[i]可以是零，代表此時的矩形和就是從i到j全包含在內.

ex. prefixSums = [1,2,3]，如果沒有在前面加個零，我們便考慮不到[1,2,3]總和為6這情況

# Complexity

- time complexity:

$$O(M * M * N * N * logN)$$ or $$O(N * N * M * M * logM)$$

- space complexity:

$$O(n)$$

# Follow Up

當 M > N時，我們可以透過轉置當前matrix使得時間複雜度變為$O(N * N * M * M * logM)$
當log裡的值越大，可以替我們省越多的時間