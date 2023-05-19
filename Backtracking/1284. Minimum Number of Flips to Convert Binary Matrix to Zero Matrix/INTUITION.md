# Intuition

each cell could choose to flip or not flip.
since m*n = 9 at most, all the possible combinations are 2^9 = 512

might be capable of backtracking

since each cell we can choose flip or not flip, our backtracking should be like this:
we choose minimum number of flips among these two strategies `min(flip, not-flip)`

```py
def backtracking(r, c):
    if c == n:
        return backtracking(r+1, 0)
    
    if r == m:
        return 0 if check(mat) else inf

    # not flip mat[i][j]
    res = backtracking(r, c+1)

    # flip mat[i][j]
    flips(r, c)
    res = min(res, backtracking(r, c+1)+1)
    flips(r, c) # backtracking

    return res
```

and flips just a helper function to change mat[i][j] and its neighbor
```py
dirs = [[0,1],[1,0],[0,-1],[-1,0]]
def flips(r, c):
    mat[r][c] = 1-mat[r][c]
    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if 0 <= row < m and 0 <= col < n:
            mat[row][col] = 1-mat[row][col]
```

and our base case is straightforward.
after we consider all the cells, i.e. `r == m`, we check if we can get a binary zero matrix.
once we successfully get a binary zero matrix, we return 0 as our base case, or we return `inf`

# Complexity

- time complexity
$$O(2^{(m*n)} * m*n)$$

- space complexity
$$O(2^{(m*n)})$$