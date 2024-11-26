# Intuition

一開始直覺的想到brute force solution:
我們從反向出發, 三個小孩都從終點往回走, 並更新收穫到的果實數目

定義dp[r1][c1][r2][c2][r3][c3]: the maximum fruits when child1 at (r1, c1]), child2 at (r2, c2), child3 at (r3, c3)

那麼base case: dp[n-1][n-1][n-1][n-1][n-1][n-1] = fruits[n-1][n-1]

狀態轉移:

```py
cnt = sum(fruits[r][c] for r,c in set([(row1, col1), (row2, col2), (row3, col3)]))
dp[row1][col1][row2][col2][row3][col3] = max(dp[row1][col1][row2][col2][row3][col3], dp[r1][c1][r2][c2][r3][c3] + cnt)
```

最終答案就是dp[0][0][0][n-1][n-1][0]

```py
def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
    n = len(fruits)

    dirs1 = [[-1,-1],[-1,0],[0,-1]]
    dirs2 = [[-1,1],[-1,0],[-1,-1]]
    dirs3 = [[1,-1],[0,-1],[-1,-1]]

    dp = [[[[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    dp[n-1][n-1][n-1][n-1][n-1][n-1] = fruits[n-1][n-1]

    queue = deque([[n-1,n-1, n-1,n-1, n-1, n-1]])
    visited = set()
    for _ in range(n-1):
        while queue:
            for _ in range(len(queue)):
                r1, c1, r2, c2, r3, c3 = queue.popleft()
                if (r1, c1, r2, c2, r3, c3) in visited: continue
                visited.add((r1, c1, r2, c2, r3, c3))

                for dr1, dc1 in dirs1:
                    row1, col1 = r1+dr1, c1+dc1
                    if not (0 <= row1 < n and 0 <= col1 < n): continue
                    for dr2, dc2 in dirs2:
                        row2, col2 = r2+dr2, c2+dc2
                        if not (0 <= row2 < n and 0 <= col2 < n): continue
                        if (row2,col2) == (row1,col1): continue
                        for dr3, dc3 in dirs3:
                            row3, col3 = r3+dr3, c3+dc3
                            if not (0 <= row3 < n and 0 <= col3 < n): continue
                            if (row3,col3) == (row1,col1): continue
                            if (row3,col3) == (row2,col2): continue

                            cnt = fruits[row1][col1] + fruits[row2][col2] + fruits[row3][col3]
                            dp[row1][col1][row2][col2][row3][col3] = max(dp[row1][col1][row2][col2][row3][col3], dp[r1][c1][r2][c2][r3][c3] + cnt)
                            queue.append([row1, col1, row2, col2, row3, col3])
    return dp[0][0][0][n-1][n-1][0]
```

但可惜這樣會**TLE**

但仔細觀察條件, 每個小孩子都限制只能剛剛好走`n-1`步
會發現左上位置(0,0)的小孩他的路徑其實只有一條路能走 => 那就是對角線

那剩下兩個對角的小孩, 其實也根本不會互相有所交集
因此兩個對角小孩就各自在不超過對角線的情況下利用dynamic programming求最大值
最後三個小孩收集的果實加總起來即可

令dp為**the maximum number of fruits the children can collect**

那麼最終答案為: dp1 + dp2[n-1][n-2] + dp3[n-2][n-1], 其中

1. (0,0)小孩: dp1 = sum(fruits[i][i] for i in range(n))
2. (0,n-1)小孩: dp2[n-1][n-2]
3. (n-1,0)小孩: dp3[n-2][n-1]
4. 同個位置的果實只能採收一次, 所以:
    - (0,n-1)小孩的最後一個位置實質上為(n-1, n-2)
    - (n-1,0)小孩的最後一個位置實質上為(n-2, n-1)

狀態變化:

對於當前dp2[r][c]來說, 前個狀態為dp2[r-dr][c-dc]
因此: `dp2[r][c] = max(dp2[r][c], dp2[row][col] + fruits[r][c]) where n-1-r < col < n`

但這邊最需要注意的是: row, col的constraint
- 由於我們r範圍[1,n], 因此row肯定合法
- 但關於這個col:
    - 第一個位置, 只能是n-1
    - 第二個位置, 可以是n-1, n-2
    - 所以col的範圍必須限制在: `n-1-r < col < n`, 超出這範圍都是不合法的前驅狀態, 該小孩根本走不到那位置

```py
dirs2 = [[1,-1],[1,0],[1,1]]
dp2 = [[0]*n for _ in range(n)]
dp2[0][n-1] = fruits[0][n-1]
for r in range(1, n):
    for c in range(r+1, n):
        for dr, dc in dirs2:
            row, col = r-dr, c-dc
            if n-1-r < col < n:
                dp2[r][c] = max(dp2[r][c], dp2[row][col] + fruits[r][c])
```

同理:
對於起點為(n-1,0)的小孩, 該狀態變化為:

`dp3[r][c] = max(dp3[r][c], dp3[row][col] + fruits[r][c]) where n-1-c < row < n`


```py
dirs3 = [[-1,1],[0,1],[1,1]]
dp3 = [[0]*n for _ in range(n)]
dp3[n-1][0] = fruits[n-1][0]
for c in range(1, n):
    for r in range(c+1, n):
        for dr, dc in dirs3:
            row, col = r-dr, c-dc
            if n-1-c < row < n:
                dp3[r][c] = max(dp3[r][c], dp3[row][col] + fruits[r][c])
```

# Complexity

time: O(n^2)
space: O(n^2)