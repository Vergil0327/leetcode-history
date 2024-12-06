# Intuition

要找到四邊都是`1`的正方形, 首先先想到可以利用prefix sum

- prefix row sum
- prefix col sum

這樣我們就能利用`length == prefix_sum[i][j+length] - prefix_sum[i][j]`來判斷是否是合法的全`1`邊

那這樣就簡單了, 我們只要遍歷起始點(i,j)然後再由大到小遍歷當前邊長
就能找出最大合法矩形, 當前elements數目為: `length*length`

再來就遍歷完每個合法(i,j)找出全局最大合法矩形即可


time: O(n^3)
space: O(n^2)