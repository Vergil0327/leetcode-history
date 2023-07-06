# Intuition

找permutation使得nums[i]+nums[i+1]為平方數

由於`nums.length <= 12`, 首先想到的是用DFS+memorization並配合bitmask來搜索所有可能的permutation

參數可以用個二進制的bitmask來表示選取的state, 並且我們還需要前一個選取的數才能判斷相加是不是平方數:

`dfs(state, prev): the number of valid permutations`

但從example 2可發現, [2,2,2] 雖然有三種選取方法, 但其實是同一種permutation

所以我們可以先對nums排序
想成如果當前我們選擇nums[i]的話, 那麼下個挑選就**不可以**與前次挑選相等

下次所有與前次挑選的數相等的所有nums[i]都必須跳過

high level來看的話如下所示:
```py
res = 0
for i in range(n):
    if i > 0 and nums[i] == nums[i-1]: continue
    dfs(1<<i, nums[i])
return res
```

同樣的, 我們的dfs也一樣:
- 如果nums[i]已經選了, 那就continue. (可從bitmast state得知)
- 再來再用一個變數prevPick來紀錄. 如果當前我們選擇nums[i]的話, 那麼下個挑選就**不可以**與前次挑選相等.
  - 也就是如果nums[i] == prevPick, 那也continue
```py
@lru_cache(None)
def dfs(state, prev):
    if state == finalState:
        return 1

    cnt = 0
    prevPick = -1
    for i in range(n):
        if (state>>i)&1: continue
        if nums[i] == prevPick: continue
        prevPick = nums[i]

        squareRoot = sqrt(prev+nums[i])
        if squareRoot == int(squareRoot) and squareRoot**2 == (prev+nums[i]):
            cnt += dfs(state | (1<<i), nums[i])

    return cnt
```

那dfs的base condition就是當所有數都挑完時, 也就是`state == 1111...111 == (1<<n)-1`時, 選擇方法數為1

```py
if state == (1<<n)-1: return 1
```