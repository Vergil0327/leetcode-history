# Intuition

一開始很快想到了這是個背包問題，我們遍歷前i個人，然後看每個帽子戴的狀態來更新，會類似像這樣

```
for i in range(10):
    for hat_state in range(1<<40):
        for j in range(40):
            if (hat_state>>j)&j == 1: continue
            dp[i+1][hat_state+(1<<j)] += dp[i][hat_state]
```

但2^40這是個不切實際的數字，不管是要遍歷或是記憶體需求都很大，因此我們不該選擇帽子作為選擇狀態

我們看到人數 `n` 最多就十人，這個用bitmask表示就合理多了
所以我們可以用bitmask的`0`, `1`來表示這個人選了帽子沒

我們可以這樣定義DP:

`dp[i][people_state]: the ways to choose hat for first i hat when choosing state is people_state`

那這樣最終答案就是所有帽子都可選，並且所有人都有選：
`dp[40][(1<<n)-1]`

狀態轉移就會是:

注意我們是用現在的狀態更新未來的狀態: dp[i+1][state] += dp[i][state']
`base case是 dp[0][0] = 1`

然後我們預先處理一下每個帽子能被哪些人選，然後儲存在`hat2people`裡
再來有兩種想法:
然後如果對於當前第`i`頂帽子來說，`person`可以選來戴
1. 如果當前這個people_state裡的`person`已經戴了帽子，那我們跳過。如果還沒，我們就讓他戴第`i`頂帽子，那麼狀態更新就是

`dp[hat+1][people_state + (1<<person)] += dp[hat][people_state]`

```py
dp[0][0] = 1 # base case
for hat in range(40):
    for people_state in range(1<<n):
        dp[hat+1][people_state] = dp[hat][people_state]

    for people_state in range(1<<n):
        for person in hat2people[hat]:
            if ((people_state>>person)&1) == 1: continue # person has taken hat
            dp[hat+1][people_state + (1<<person)] += dp[hat][people_state]
            dp[hat+1][people_state + (1<<person)] %= MOD
```

2. 那如果當前這個people_state裡的`person`已經戴帽子，那我們跳過。如果還沒，那麼我們選他戴的是第`i`頂帽子，那麼狀態更新就是

`dp[hat+1][people_state] += dp[hat][people_state^(1<<person)]`

```py
dp[0][0] = 1 # base case
for hat in range(40):
    for people_state in range(1<<n):
        dp[hat+1][people_state] = dp[hat][people_state]
        for person in hat2people[hat]:
            if ((people_state>>person)&1) == 0: continue # person has NOT taken hat
            dp[hat+1][people_state] += dp[hat][people_state^(1<<person)]
            dp[hat+1][people_state] %= MOD
```

兩種方式都可以，但重要的差異在於對於`dp[hat+1][people_state]`來說，他至少有`dp[hat][people_state]`這麼多種方式

所以我們得確保`dp[hat+1]`的所有people_state都有更新到

第一種方式由於我們是更新`dp[hat+1][people_state + (1<<person)]`
因此有可能會漏掉dp[hat+1][people_state]，所以我們在那之前遍歷全部賦值一遍

第二種方式更新的是`dp[hat+1][people_state]`，所以就不用遍歷一遍，記得賦值就好

# Complexity

- time complexity
$$O(40 * 2^n * n)$$

- space complexity
$$O(40 * 2^n)$$