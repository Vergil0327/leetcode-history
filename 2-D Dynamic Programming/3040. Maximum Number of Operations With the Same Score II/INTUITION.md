# Intuition

直覺想到用dfs模擬三種可能並配合memorization變成top-down dp來解

define: dfs(l, r, score): the maximum times of operation when index is `l` and `r` and all operation score must be `score`

set initial score = 0
1. if l+1 <= r and (score == 0 or score == nums[l]+nums[l+1]):
   - res = max(res, dfs(l+2, r, nums[l]+nums[l+1])+1)
2. if r-2 >= l and (score == 0 or score == nums[r]+nums[r-1]):
   - res = max(res, dfs(l, r-2, nums[r]+nums[r-1])+1)
3. if l < r and (score == 0 or score == nums[l]+nums[r]):
   - res = max(res, dfs(l+1, r-1, nums[l]+nums[r])+1)

那這樣recursion的base case就是`l`必須小於`r` => `if l >= r: return 0`

第一個操作決定了後續的score, 因此score只可能有三種可能:
1. nums[0]+nums[1]
2. nums[-1]+nums[-2]
3. nums[0]+nums[-1]

那`l`, `r`可能是[0,n-1]

因此整體時間複雜度為O(3 * n^2) = O(n^2)
