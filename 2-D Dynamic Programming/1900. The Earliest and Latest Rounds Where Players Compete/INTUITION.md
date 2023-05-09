# Intuition

`2 <= n <= 28`, n is quite small -> less than 32 -> we can use bitmask as win/lose state

X X A X B X X X X

- when A > B:
  - dp[A][B] = dp[B][A]
  - firstPlayer < secondPlayer, 避免相同情況重複計算

- when (A+B)/2 > (n+1)/2
  - 當A, B兩個選手都在中間偏右的區間時, 他的情況跟相對稱的中間偏左是一樣的. 我們統一移到偏左區間處理
  - `XXX A' XXXX B' XX A XXXX B XXX`
  - dp[A'][B'] = dp[n+1-B][n+1-A]
  - 判斷方式是否偏右的例子
    ```
    1 2 3 4
    middle = (4+1)/2 = 2.5
    (3+4)/2 = 3.5
    ```

dp[n][A][B]: the minimum/maximum rounds for A and B survive to last round considering n players survive totally where A and B are firstPlayer's and secondPlayer's index respectively

- Case 1: A, B在中軸兩側
  - XXXXX A XXX B' XX MID XX B XXX A' XXXXX
  - _____   ___    _________
  -  x個     y個        z個 
  - (A, B)對決(A',B')
  - 我們全部可能性DFS搜索一遍, 看x, y, z 分別剩下多少選手
  - 狀態轉移
  ```
  dp[n][A][B] = dp[n/2][x+1][x+1+y+z+1] + 1
  # 考慮奇數偶數性質, n/2改為 (n+1)//2 or ceil(n/2)
  ```
- Case 2: A, B在同一側
  - XXXXX A XXX B XX MID XX B' XXX A' XXXXX
  - _____   ___
  -  x個     y個
  - (A, B)對決(A',B')
  - 狀態轉移
  ```
  dp[n][A][B] = dp[n/2][x+1][x+1+y+1] + 1
  ```

# Complexity

- time complexity

We have $O(n^2*log(n))$ states totally
O(n) for both A and B and log(n) -> dfs(n, A, B)

and we have (n^2) complexity for double-loop in each state

so we have $O(n^4 * log(n))$

- space complexity

$$O(n^2*log(n))$$

Actually, more detailed analysis shows that log factor can be removed, because

if n = 64, then our recursion will be
1. have O(64*64) states for n' = 64
2. then we have O(32*32) states for n' = 32
3. O(16*16) for n' = 16
4. and so on.

thus, time complexity is `n^2 * (n//2)^2 * (n//4)^2 = O(n^4)`
and space complexity is O(n^2).