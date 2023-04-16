# Top-Down

## Intuition

```
target: Y Y Y Y Y Y Y Y Y
                        i

words:
    [
        X X {X} X X X
             k of words[j]
        X X {X} X X X
        X X {X} X X X
    ]
```

首先這題有提到說當你用了第`k`個index, 就不能再使用更之前的words[j][0, 1, ..., k-1]
這很明顯的提示說有無後效性, 代表這題適用dynamic programming

當我們考慮target[i]時:
- 我們能使用的是所有words[i]的第`k`個字母, 這代表我們要用個hashmap紀錄第k-th column所能使用的words[i][k]

```py
m = len(words[0])
dictionary = [defaultdict(int) for _ in range(m)]

for i in range(len(words)):
    for j in range(m):
        dictionary[j][words[i][j]] += 1
```

這樣一來, top-down DFS就很清楚了
- 如果我們能成功組出`target`, 那就代表我們找到一種方法
  - `if i == n: return 1`
- 如果直到j個dictionary都用完都還組不完, 那就代表0種方法
  - if j == m: return 0
- 然後每個dictionary[j]我們可選可不選
  - 不選: res = dfs(i, j+1)%MOD
  - 選的話, 就看幾種方法然後再乘上我們能用的字母次數: res += dfs(i+1, j+1) * dictionary[j][target[i]]
    - 如果有`dictionary[j][target[i]]`個words[i][k]都等於target[i], 那就代表當前的方法有`dictionary[j][target[i]]`種選擇, 所以是乘法

```py
@lru_cache(None)
def dfs(i, j):
    if i == n: return 1
    if j == m: return 0

    res = dfs(i, j+1)%MOD
    if target[i] in dictionary[j]:
        res += dfs(i+1, j+1) * dictionary[j][target[i]]
    return res % MOD
```

# bottom-up

## Intuition

定義dp[i][j]: the number of ways to form target[:i] with first j dictionary

```
target: Y Y Y Y Y Y Y Y Y
                        i

words:
    [
        X X {X} X X X
             k of words[j]
        X X {X} X X X
        X X {X} X X X
    ]
```

對於target[i]:
- 如果我們用第k個column的words[j][k]
  - dp[i][k] = dp[i-1][k-1] * count[k][target[i]] if word[k] == target[i]
- 如果我們不用第k個column的word
  - dp[i][k] = dp[i-1][k]

這邊我們可以用1-indexed來避免dp[i-1][k-1]越界的問題

**base case**

dp[0][k]: 用前k個字符 (word[:k]) 來組成空字串 -> 1種方法
dp[i][0]: 用0個字符組成target[:i] -> 0種方法