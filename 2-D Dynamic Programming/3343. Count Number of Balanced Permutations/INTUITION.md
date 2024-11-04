# Intuition

### brute force: backtracking

```py
def countBalancedPermutations(self, num: str) -> int:
    n = len(num)
    mod = 10**9 + 7

    count = Counter(num)
    def dfs(i, balance):
        if i >= n: return int(balance == 0)

        total = 0
        for digit in count.keys():
            if count[digit] > 0:
                count[digit] -= 1
                total += dfs(i + 1, balance + int(digit)*pow(-1, i%2))
                count[digit] += 1

        return total % mod
    return dfs(0, 0)
```

但直接進行backtracking會超時, 對於這種求合法數有多少的, 肯定得往dynamic programming去想
我們目的是要將0-9分別分配到奇數、偶數位置, 並使得兩邊和相等, 也就是diff(或稱balance)為0

那首先定義我們的top-down dp:

dfs(digit, odd, even, balance): the number of distinct permutations of num using **0 ~ digit** digits and have **`odd`** digits in odd position, **`even`** digits in even position and total balance is **`balance`**

為了重新安排num[i], 首先我們先找出0-9個有多少個
```py
count = Counter(map(int, num))
```

那狀態轉移就是我們就從0到9, 一個個去分配這些digit的位置
遍歷個數範圍[0, count[digit]], 將當前digit分配`cnt`到odd position, `count[digit]-cnt`到even posistion

那假設當前我們選擇分配`x`個給odd position跟`y`個給even position, 其中`x+y = count[digit]`
那麼當前這個抉擇將有: `comb(odd, x) * comb(even, y)` 種方法

並且`balance`變化為: `balance += (x - y) * digit`

所以整體框架如下
```py
def dfs(digit, odd, even, balance):
    res = 0
    for cnt in range(0, count[digit]+1):
        evenCnt = count[digit]-cnt
        res += comb(odd, cnt) * comb(even, evenCnt) * dfs(digit+1, odd-cnt, even - evenCnt, balance + digit * (cnt - evenCnt))
    return res

return dfs(0, len(num) - len(num)//2, len(num)//2, 0)
```

base case:

只有當全部digit分配完, odd, even位置也都分配完, 並且balance為0時才是合法permutation:

```py
if digit >= 10:
    return int(odd == 0 and even == 0 and balance == 0)
```

## Optimization

since `2 <= num.length <= 80`, we can precompute `comb(m, n)`

```py
m = n = 81

comb = [[0]*n for _ in range(m)]

for i in range(m):
    comb[i][i] = comb[i][0] = 1
    for j in range(1, i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
```

# Complexity

time: O(10 * 10 * n * n * (9*n)) where max balance is n * 9
space: O(10 * n * n * (9*n))