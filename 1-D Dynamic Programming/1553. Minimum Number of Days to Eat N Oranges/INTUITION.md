# Intuition

```
X X X X X X X
            i

if remaining%2 == 0:
    we can eat n//2
if remaining%3 == 0:
    we can eat 2 * n // 3
or we just eat 1
```

if we define `dp[i]: the minimum number of days to eat remaining i oranges`

iterate i from n to 0
- dp[i] = dp[i+1] + 1
- dp[i//2] = dp[i] + 1 if i%2 == 0 (1-indexed)
- dp[i//3] = dp[i] + 1 if i%3 == 0 (1-indexed)

用現在狀態更新未來狀態, 這樣最終答案就是dp[0]

**base case**

`dp[n] = 0`

但由於`1 <= n <= 2 * 10^9`, 這樣O(n)的時間會TLE
但這題也沒有什麼能greedy的寫法, 如果優先選第三種策略直接吃掉2*(n/3)也並不絕對是正解
所以這時可能要往top-down dp方式並想並透過剪枝來大幅降低時間複雜度
而最吃時間的其實就是`dfs(i) = dfs(i-1)+1`這個branch, 我們可能要想怎麼對這個選項下手

這三個策略來看, i//2跟i//3永遠是最好的捷徑
11 -> 10 -> 5 -> 4 -> 2 -> ...
11 -> 10 -> 9 -> 8 -> 4 -> ...
對於只吃1個來說, 我們永遠是為了一次吃掉n/2或是一次吃掉2*(n/3)而進行
而不會一直一個一個吃把整個n個吃完, 所以我們表達是可以改一下

- 我們把`dfs = dfs(i-1)+1`這個選項排除
- 對於`dfs = dfs(i//2)+1 if i%2==0`來說, 如果此時`i%2 != 0`, 代表我們要一個一個吃, 吃`i%2`次.
    - `dfs = i%2 + dfs(i//2) + 1`
- 對於`dfs = dfs(i//3)+1 if i%3==0`來說也一樣, 如果`i%3!=0`, 代表我們要花`i%3`次`-1`操作來使得我們可以一次吃掉2/3
    - `dfs = i%3 + dfs(i//3) + 1`

**base case**

由於要考慮對2跟對3做除法以及求餘數
所以base case就考慮剩下1,2,3個時的次數

```py
if i == 1: return 1
if i == 2: return 2
if i == 3: return 2
```

time: O(logn) approximately