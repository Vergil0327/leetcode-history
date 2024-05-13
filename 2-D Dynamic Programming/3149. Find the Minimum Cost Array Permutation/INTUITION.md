# Intuition

# Intuition

> score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|

The score function is cyclic, so we can always set perm[0] = 0 for the smallest lexical order.
=> **perm[0] - nums[perm[1]]**

那再來一開始想到的就是backtracking brute force
我們將[0,n-1]每個數的所有分配組合都試試:

```py
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        perm = [-1]*n
        perm[0] = 0

        def score(arr):
            return sum(abs(perm[i]-nums[perm[(i+1)%n]]) for i in range(n))

        self.curScore = inf
        self.res = [-1]*n
        def dfs(i, bitmask):
            if i == n:
                sc = score(perm)
                if sc < self.curScore:
                    self.res = perm.copy()
                    self.curScore = sc
                elif sc == self.curScore:
                    for j in range(n):
                        if perm[j] == self.res[j]: continue
                        if perm[j] < self.res[j]:
                            self.res = perm.copy()
                        break
                return

            for v in range(n):
                if (bitmask>>v) & 1: continue
                perm[i] = v
                dfs(i+1, bitmask | (1<<v))
                perm[i] = -1
        dfs(1, 1)
        return self.res
```

可惜backtracking會TLE, 那這樣可能要嘗試寫成可以memorization的形式試試

首先`score = |perm[i] - nums[perm[i+1]]| for i in range(n)`

我們用dfs+memo (top-down dp)去搜索每個可能性, 已知perm[0] = 0
所以我們從0開始往後開始建構, 並搜索出最低分數解

一開始從i=0, perm[i] = perm[0] = 0開始
再來我們遍歷所有可能嘗試建構permutations
當前建構的為perm[i+1], 同時我們紀錄前個選擇`prev`
當前score = abs(prev - nums[perm[i+1]]) where perm[i+1] in range(1, n)

```py
for v in range(1, n):
    if (bitmask>>v)&1: continue # already used
    sc = dfs(v, bitmask|(1<<v)) + abs(prev - nums[v])
```

所以min score的求法為:

```py
@cache
def dfs(prev, bitmask):
    if bitmask == final_state:
        return abs(prev-nums[0])

    # score = |perm[i] - nums[perm[i+1]]| for i in range(n)
    # use recursion to find every possibilities => |perm[i] - nums[perm[i+1]]| = |prev - nums[i]| for i in range(n) if (bitmask>>i)&1 == 0
    min_score = inf
    for v in range(1, n):
        if (bitmask>>v)&1: continue
        sc = dfs(v, bitmask|(1<<v)) + abs(prev - nums[v])
        if sc < min_score:
            min_score = sc

    return min_score
```

但由於我們答案要求的是最低分時的permutations, 所以我們得另外存下minimum score時的選擇

`dp: {[prev, bitmask]: permutation}` =. 當狀態為(prev, bitmask)時的permutaion為dp[prev, bitmask]

```py
def findPermutation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    final_state = (1<<n)-1

    dp = defaultdict(list) # {[prev, bitmask]: permutation}

    @cache
    def dfs(prev, bitmask):
        if bitmask == final_state:
            return abs(prev-nums[0])

        # score = |perm[i] - nums[perm[i+1]]| for i in range(n)
        # use recursion to find every possibilities => |perm[i] - nums[perm[i+1]]| = |prev - nums[i]| for i in range(n) if (bitmask>>i)&1 == 0
        min_score, num = inf, -1
        for v in range(1, n):
            if (bitmask>>v)&1: continue
            sc = dfs(v, bitmask|(1<<v)) + abs(prev - nums[v])
            if sc < min_score:
                min_score = sc
                num = v # 由於我們從小到大遍歷, 第一個min_score即為lexicographically smallest

        dp[prev, bitmask] = [num] + dp[num, bitmask | (1<<num)] # dp[prev, bitmask] = [current choice] + dp[next, next_bitmask]

        return min_score

    dfs(0, 1)
    return [0] + dp[0, 1]
```