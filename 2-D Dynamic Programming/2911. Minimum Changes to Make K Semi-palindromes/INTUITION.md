# Intuition

這題蠻明顯的就是一個基本型的DP

```
X X X X X X X [X X X X X X]
               j         i
```

定義dp[i][k]: the changes considering first i letters when split into k substring
我們找一段s[j:i], 然後計算這段s[j:i]需要多少的changes
那麼狀態轉移就是:

```py
dp[i][k] = min(dp[i][k], dp[j-1][k-1] + calChanges(j, i))
```

所以我們很自然的外層就是兩個for-loop遍歷`i`跟`k`
由於我們不確定`j`的位置, 所以全都遍歷一遍更新dp[i][k]
那麼最後答案就是**dp[n][k]** (1-indexed)
```py
for i in range(1, n+1): # 1-indexed
    for kk in range(1, k+1):
        for j in range(i-1):
            dp[i][kk] = min(dp[i][kk], dp[j][kk-1]+changes[j][i-1])
```

**Base Case**

- dp[0][0] = 0
  - 0個letters, 0個substring => 0 changes

- dp[i][0] = dp[0][k] = inf => 都是不合理的

但這題難處就是, 當初沒看懂semi-palindrome的定義到底是啥

semi-palindrome

- 首先詭異的是看這敘述: **"a"**, "ab", and, "abca" are not semi-palindrome
  - 代表semi-palindrome**長度必須至少為2**
- A string with a length of len is considered a semi-palindrome if there exists a positive integer d such that 1 <= d < len and len % d == 0, and if we take indices that have the same modulo by d, they form a palindrome. For example, "aa", "aba", "adbgad", and, "abab" are semi-palindrome
  - ex. **a**d**b**g**a**d => 當d為2同餘的letters組成: **aba**跟**dgd**, 皆為palindrome, 所以"adbgad"為semi-palindrome

所以自然地, 為了讓上面dp計算能以O(1)時間知道changes[j][i], 我們必須提前計算changes for s[j:i] to become semi-palindrome

想不到比較好的方式, 所以先試著用brute force計算changes[i][j]

由於semi-palindrome長度必須至少為2, 所以我們遍歷可能長度`2 <= length <= n`, 以及起始與結束位置`i`, `j`

```py
n = len(s)
changes = [[inf]*n for _ in range(n)]
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i+length-1
        # ...
```

根據定義, semi-palindrome為`1 <= d < length`被d同餘為0的所組成
因此`d`必須是length的factor, 所以我們可以提前計算所有length的factors

```py
factors = [[1] for _ in range(n+1)]
for d in range(2, n):
    for v in range(d+d, n+1, d):
        factors[v].append(d)
```

因此綜合上述可得changes[[i][j] = changes for s[j:i] (both inclusive):
```py
changes = [[inf]*n for _ in range(n)]
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i+length-1
        for d in factors[length]:

            # [{"X" X X} {"X" X X} {"X" X X} {"X" X X}] length = 12
            #  i+0           ...            i+0+length-3
            #    i+1                            i+1+length-3
            # 這邊我們找出每個同餘的subseq., 並計算他的changes
            cnt = 0
            for offset in range(d):
                l, r = i+offset, i+offset+length-d
                while l < r:
                    if s[l] != s[r]:
                        cnt += 1
                    l, r = l+d, r-d
            changes[i][j] = min(changes[i][j], cnt)
```

因此整個主幹為:
注意我們的changes[i][j] 中的`i`, `j`為**0-indexed**
記得把我們外層遍歷的1-indexed的`i`轉成0-indexed的`i'`求changes[j][i']
```py
dp = [[inf]*(k+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1): # 1-indexed
    for kk in range(1, k+1):
        for j in range(i-1): # j 0-indexed, it's invalid for length=1, therefore, j <= i-2
            dp[i][kk] = min(dp[i][kk], dp[j][kk-1]+changes[j][i-1])
    
return dp[n][k]
```