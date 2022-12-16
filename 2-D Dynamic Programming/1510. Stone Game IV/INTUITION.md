# Top-Down DP (Recursion + Memorization)

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
透過遞歸模擬Alice與Bob兩人交互取石，並嘗試所有選項，一但有任一個策略Alice能獲勝則返回`True`
如果嘗試所有策略後仍無法獲勝，則返回`False`

**Alice每次可取走多少:**

每次可取走`square number`，對於`n` 來說最大的`square number`為 `int(sqrt(n))` 的平方
因此Alice每回合可取走`1`到 `int(sqrt(n))的平方`個石頭

**Bob能取多少:**
如果定義Alice這回合為`play(n)`，那麼下回合(Bob回合)可定義為`play(n-square_number)`

**Alice勝利條件:**

1. 迫使Bob輪到他回合的時候，沒有石頭可取，也就是`n-square number == 0`的時候
2. Bob輸的時候，根據定義，也就是 `not play(n-square_number) == False` 的時候Alice贏

## Approach

DFS遞歸嘗試所有可能性，並記憶每次結果避免重複計算

## Complexity
- Time complexity:
$$O(n*sqrt(n))$$

觀察我們的decision tree，每次有`sqrt(n)`種可能，decision tree的高度為`n`
因此時間複雜度為`sqrt(n) 的 n次方 = sqrt(n) ^ n`

但由於我們每次的計算都會運用cache起來，每種可能只會計算一次
所以時間複雜度會降為`O(sqrt(n) * n)`，也可寫作`O(n^1.5)`

- Space complexity:
$$O(n)$$ (height of decision tree)

# Bottom-Up

## Intuition

dp[i] comes from dp[i-1], dp[i-2*2], dp[i-3*3], ...

therefore,

```python
for i in range(1, n+1):
    for j in range(1, int(sqrt(i))+1):
        # update DP state
```

**base case:**

- if there is 0 stone, lose: `dp[0] = 0`
- if there is only 1 stone, win: `dp[1] = 1`

**state transfer:**

we can define opponent's result as `dp[i-j*j]`,

if dp[i-j*j] == 0, means opponent lose and we win.
if dp[i-j*j] == 1, means opponent win and we lose.

## Complexity

same as top-down method