# Intuition

整個過程是topological sort, 目的要盡量讓score[node]較大的擺在越靠後的位置去處理, 這樣得到的分數才會高
一開始想到那就用priority queue, 盡量優先選分數較低的先處理, 高分留在後面這樣`multiplier`較大

但會在這個測試失敗: n=5, edges=[[1,2],[0,3],[1,4],[2,3],[1,3]], score=[50913,47946,97391,27488,69147], expected=897632
代表這個greedy並不適用

既然greedy行不通, 那只能往dynamic programming去思考所有可能了

看到限制: 1 <= n == score.length <= 22, 值很小 => 可能是dp+bitmask? (2^22 = 4194304)

所以思維要轉換一下, 我們用bitmask來代表topoligical sort已經移除掉的節點`node`

所以dp狀態轉移方程為: `dp[new_state] = max(dp[new_state], dp[current_state] + score[node] * position)`

主框架為:

```py
total_states = 1<<n
dp = [-1]*total_states

# base case
dp[0] = 0

for state in range(total_states):
    if dp[state] == -1: continue # invalid current state

    position = state.bit_count() + 1
    for node in range(n):
        if (state>>node)&1: continue # already removed

        if /* valid condition */:
            new_state = state | (1<<node)
            dp[new_state] = max(dp[new_state], dp[state] + score[node] * position)

return dp[total_states-1]
```

那這邊的`/* valid condition */`條件就是: **當前節點的前置節點必須已經移除**

所以我們先前處理每個節點的所需前置節點記錄在`parent[node]`裡:

```py
parent = [0] * n
for u, v in edges:
    parent[v] |= (1<<u)
```

那這樣這個`/* valid condition */`就能表示成: `(state & parent[node]) == parent[node]`

那最終答案就是當全部節點都移除後的最大max score: `dp[total_states-1]`

# Complexity

time: $O(2^n)$
space: $O(2^n)$