# Intuition

首先, 如果string是palindrome, 代表他只有0個或1個字母出現奇數次 (擺在palindrome中間)

再來一個tree的path有三種情況:
1. 左leaf node到root => u -> root
2. 右leaf node到root => v -> root
3. 左leaf node到右leaf node => u -> v = u->root->v

我們可以利用parent數組進行post-order dfs來得到從leaf node到root的各個字母的奇偶性(parity)
由於總共就26小寫英文字母, 我們可以用26-bitmask來儲存每個字母的奇偶性
ex.
001 => "a"出現奇數次
010 => "b"出現奇數次

```py
def dfs(node):
    if node <= 0: return 0
    ch = ord(s[node]) - ord("a")
    return dfs(parent[node]) ^ (1<<ch)
```

在得到當前node -> root這條path裡每個字母的奇偶性後, parity = dfs(node)
並用個dp來紀錄當前的字母奇偶性有幾條path

再來我們查看每個字母作為中間的話能不能跟另一條path構造成palindrome:

如果想以a作為palindrome的中間部分, 那另一條path的奇偶性必須是parity ^ (1<<0)
ex. 當前`parity = 101`,  如果要以a作為中間, 另一條必須`100`這樣才能構成一條除了a以外其他字母都出現偶數次的path
如果想以b作為palindrome的中間部分, 那另一條path的奇偶性必須是parity ^ (1<<1)
如果想以c作為palindrome的中間部分, 那另一條path的奇偶性必須是parity ^ (1<<2)

所以對於當前的parity來說, 我們就查看每個字母作為middle of palindrome時, 有沒有其他path能跟他共同構建成一個palindrome
這時就查看dp然後更新`res`, `res += [parity ^ (1<<i)] where i from 0 to 25` 

另外, 如果有另一條path跟自己本身一樣的話, 一樣能構造出palindrome
ex. path1 = 101, path2 = 101 => path1 + path2 -> 每個字母都變偶數次, 可構建出palindrome
所以`res`還必須加上`dp[parity]`, `dp += dp[parity]`

等到查看玩當前這條path能貢獻的palindrome後, 記得再把這條path加上去, 更新dp
`dp[parities] += 1`