# Recursion

## Intuition

the keypoint is the maximum score Alice can get is `current score + rest of score - Bob's maximum score`, therefore:

if Alice choose first one in this round, she get `sum(stones[:i])` scores and rest of stones are `sum(stones[i+1:])`, and Bob's score is take from rest of `sum(stones[i+1:])` optimally, then we get

Alice's Score = `sum(stones[:i]) - sum(stones[i+1:]) - take(i+1)`

since Alice can choose to take first `one`, `two` or `three` stones each round, Alice can choose maximum from these three options.
thus, we can get recursion by definition:

```
AliceScore1 = sum(stones[:i+1]) + sum(stones[:i+1]) - take(i+1)
  choose one in current round   +  rest scores      - Bob's

AliceScore2 = sum(stones[:i+2]) + sum(stones[:i+2]) - take(i+2)
        choose two in current round + rest scores - Bob's

AliceScore3 = sum(stones[:i+3]) + sum(stones[:i+3]) - take(i+3)
        choose three in current round + rest scores - Bob's

and we choose best strategy from these three options above
Alice's Maximum Score = max(AliceScore1, AliceScore2, AliceScore3)
```

## Approach

- we can precompute `prefix sum` for calculate score in `O(1)`
- get recursion by definition and use memorization to avoid repeated computation
- compare alice score with bob to see who's winner or tie

## Complexity

- Time Complexity
$$O(n)$$

*if without memorization: O(3^n), each recursion has 3 branches and recursion tree height is n*

- Space Complexity
$$O(n)$$

# Bottom-Up DP

## Intuition

當Alice取1~3個石頭，Bob變成從剩下的石頭中取最大值

我們定義dp[i]為，目前有`i`個石頭被取走後所能拿到的最大分數

因此dp[0]為當`0`個石頭被取走時，我們能獲得的最大分數

case dp[0]:

每次可以取走1-3個石頭，分三種情況討論
1. 這輪取走1個

當輪獲得分數為`stones[1]`，剩下分數為`sum(stones[2:n])`，對手能取得的最大分數為`dp[1]`

*為什麼對手是dp[1]? 因為dp[1]的定義為取走1個石頭後所能獲得的最大分數*

2. 這輪取走2個

當輪獲得分數為`stones[1:2]`，剩下分數為`sum(stones[3:n])`，對手能取得的最大分數為`dp[2]`

3. 這輪取走3個

當輪獲得分數為`stones[1:3]`，剩下分數為`sum(stones[4:n])`，對手能取得的最大分數為`dp[3]`

因此這三種決策中取最佳即為`dp[0]`

#### DP Transfer Funcion

因此我們的dp state transfer function為:

```
k代表這輪取幾個石頭，k從1到3
dp[i] = max(
  dp[i],
  sum(stones[i:i+k]) + sum(stones[i+k:n]) - dp[i+k]
)
```

#### Update DP

從回歸式可發現我們在計算dp[i]的時候必須先知道dp[i+k]，所以我們必須從dp[n]算回dp[0]，因此狀態轉移方程的循環會是:
```python
for i in range(n, -1, -1): # from taken n piles to taken 0
    for k in range(1, 4): # take 1, 2 or 3 piles of stones
        # update dp
```

#### Base Case

因為我們會從dp[n]計算回dp[0]，這邊要注意
- `dp[i+k]`越界時不需計算，直接break
- 當dp[i+k]為dp[n]時，這是我們的base case

因為dp[n]為取走n個石頭後的最大分數，因此`dp[n]=0`
因為`dp[n]`為base case，已經單獨賦值了，所以我們外層循環從`n-1`開始即可

```python
for i in range(n-1, -1, -1): # from taken n-1 piles to taken 0
    for k in range(1, 4):
        # update dp
```

#### Results

所以最後我們只要比較dp[0]與sum(stones)-dp[0]的大小即可知道誰贏誰輸
1. dp[0] > sum(stones)-dp[0] (Alice > Bob): Alice贏
2. dp[0] < sum(stones)-dp[0] (Alice < Bob): Bob贏
3. dp[0] = sum(stones)-dp[0] (Alice = Bob): 平手

## Approach

- 我們可以預先計算前綴和(Prefix Sum)，來快速計算分數
- 定義`dp = [-inf] * (n+1)`，初始值為`-inf`且長度為`n`（因為最多可取走n個石頭)
- base case `dp[n]=0`
- dp[i] = `max(alice's current max score + rest score - next round bob's max score)` = `max(dp[i], (presum[i+k]-presum[i]) + (presum[n]-presum[i+k]) - dp[i+k])`
- 比較兩者分數

## Complexity

- Time Complexity
$$O(n)$$

- Space Complexity
$$O(n)$$