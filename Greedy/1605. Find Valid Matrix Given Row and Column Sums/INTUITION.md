# Intuition

row00 + row01 + ... + row0n = rowSum[0]
row10 + row11 + ... + row1n = rowSum[1]

row00 + row10 + ... + rown0 = colSum[0]
row01 + row11 + ... + rown1 = colSum[1]

one valid answer for matrix[i][j] is `min(rowSum[0], colSum[0])`.

since it's ok that every cells can be zero, and we just want **One** valid answer
=> we can greedily put min(`rowSum[i]`, `colSum[j]`) into `mat[i][j]`, then, we'll get a matrix which every `rowSum'` and `colSum'` will not exceed `rowSum[i]` and `colSum[j]`

therefore, we can use dfs to traverse every cell and put `min(rowSum[0], colSum[0])` in `mat[i][j]`

# Optimization

- rowSum[i] == colSum[j]:
once `rowSum[i] == colSum[j]`, and we'll put min(rowSum[i], colSum[j]) in mati[i][j], then `rowSum[i] == colSum[j] == 0`, which means rest of rows[i+1 ... n-1]  and cols[j+1 ... n-1] will be `0`.

thus, once rowSum[i] == colSum[j], we can directly move to mat[i+1][j+1] cell and keep greedily place `min(rowSum[0], colSum[0])` in mat[i][j]

- rowSum[i] < colSum[j]:

we'll place `min(rowSum[0], colSum[0])` in mat[i][j] and rowSum[i] will be 0.
then, rest of rows[i+1, ... n-1] will be 0

thus we can directly move to mat[i+1][j]

- rowSum[i] > colSum[j]:

mat[i][j] = `min(rowSum[0], colSum[0])` and colSum[j] will be zero.
then rest of column at i row will be 0 too.

thus, we can directly move to mat[i][j+1]