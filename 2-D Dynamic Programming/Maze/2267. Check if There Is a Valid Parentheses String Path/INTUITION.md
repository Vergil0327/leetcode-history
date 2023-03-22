# topdown

## Intuition

對於走迷宮的題目，DFS還是比較直覺的解法
對於一個合法的parenthesis, 我們可以用`"(" = +1`, `")" = -1`然後以`balanced`來表示是否是合法parenthesis

DFS大致框架如下:

1. 首先我們可以往下跟往右走
2. 一但我們走出範圍, 那就返回`False`
3. 一但途中`balanced < 0`, 代表左括號數目小於右括號數目，那們之後再怎麼走都不會是合法parenthesis, 可以直接返回`False`
4. 唯一返回`True`的情況就是走到`(m-1, n-1)`時，加上grid[m-1][n-1]的括號後剛好`balanced == 0`
5. 可以簡單的判斷: `if grid[0][0] == ")" or grid[m-1][n-1] == "(": return False`

```py
def dfs(i, j, balanced: int):
    # base cases (2., 3.)
    if i >= m or j >= n: return False
    if balanced < 0: return False

    v = 1 if grid[i][j] == "(" else -1
    # 4.
    if i == m-1 and j == n-1: return balanced+v == 0

    # 1.
    if dfs(i+1, j, balanced+v): return True
    if dfs(i, j+1, balanced+v): return True

    return False
```

## iterative way

同理, 如果是iterative的方式的話
如果有想到上面的DFS, 那麼可以很直覺想到DFS除了用遞歸形式外
還可以用stack來進行

# bottom-up

## Intuition

那如果要用bottom-up形式的dp來解的話

概念還是一樣, 我們可以用`"(" = +1`, `")" = -1`個概念來用path sum來表示當前的parenthesis是不是合法

所以我們可以這麼定義dp
dp[i][j]: the integer representation of every parenthesis when we reach (i, j)

然後dp[i][j]只跟dp[i-1][j]跟dp[i][j-1]有關，所以狀態轉移如下:
```py
for i in range(m):
    for j in range(n):
        v = 1 if grid[i][j] == "(" else -1

        if i >= 1:
            for balanced in dp[i-1][j]:
                if balanced+v >= 0:
                    dp[i][j].add(balanced+v)
        if j >= 1:
            for balanced in dp[i][j-1]:
                if balanced+v >= 0:
                    dp[i][j].add(balanced+v)
return 0 in dp[m-1][n-1]
```

最終就查看dp[m-1][n-1]的集合中有沒有balanced的parenthesis

**Base case**

如果起點就是")", 那永遠不可能組成合法parenthesis
```py
if grid[0][0] == '(':
    # '(' = +1
    dp[0][0] = set([1])
else:
    return False
```