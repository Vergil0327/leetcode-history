# Intuition

對於分割成K份求極值，首先想到的是Dynamic Programming
我們這樣定義DP:
dp[i][k]: the minimum operations for s[:i] with k partitions

X X X X X X [X X X]
             j   i

然後我們考慮第i個s[i]:
我們往前找一個j然後來看s[j:i]是不是palindrome
- 如果是, 那麼s[j:i]就能接在s[:j-1]後面並且不需要有任何操作
  - dp[i][k] = min(dp[i][k], dp[j-1][k-1])
- 如果不是, 我們就看我們需要多少次操作使得s[j:i]變成palindrome
  - 對於一個palindrome, 我們可以用two pointers來查看需要更換幾次
  - dp[i][k] = min(dp[i][k], dp[j-1][k-1] + calculateOperation(s[j:i]))

所以整個框架會是
```py
def isPal(l, r) -> int:
    swap = 0
    while l < r:
        if s[l] != s[r]:
            swap += 1
        l, r = l+1, r-1
    return swap

for i in range(1, n+1):
    for k in range(1, K+1):
        for j in range(i, k-1, -1): # 至少要能分成k份, 所以j只需要往前找到k即可 (1-indexed)
            swap = isPal(j, i)
            if swap == 0: # already palindrome
                dp[i][k] = min(dp[i][k], dp[j-1][k-1])
            else:
                dp[i][k] = min(dp[i][k], dp[j-1][k-1] + swap)
```

而這邊有個能優化的地方是, 由於isPal會被重複呼叫許多次
我們可以配合memorization來提高效率
python的話很簡單, 上面加個decorator `@lru_cache` 或 `@cache` 即可

那最終答案就是dp[n][K], 考慮n個字符並且分成K份
然後別忘了base case (因為我們dp[i][k]從dp[1][1]開始, 我們會需要dp[0][0])

`dp[0][0] = 0`
0個字符分成0份 -> 0個操作

`dp[0][k] = inf`
0個字符要分成k份 -> 不合法的操作, 維持default value **inf**

由於要找minimum operations, 我們dp[n][k]的預設值設為**inf**
