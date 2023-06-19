# Intuition

求minimum -> greedy, binary search, BFS, DP, backtracking ...

一開始想到binary search, 如果我們要用binary search去猜這個最小值, search space為[min(cookies), sum(cookies)]
我們能不能有個helper function check來判斷這個thresmold `mid`是不是可行解?
=> 如果我們在總合不超過`mid`的情況下持續將cookies分給同個kid, 最後看需要多少kids的話?
但這樣有個問題, 由於cookies[i]可以任意分配, 如何分配會影響答案
例如 Example 1, 最佳解是(8,8,15) (10,20), 並沒有一個greedy分配的方式

既然如何分配會影響, 那看來必須要用DP來嘗試所有組合求最小值
但觀察會發現這問題是個NP問題, 不把全部可能性暴力搜索完的話找不到最佳解, 也沒有好的memorization可用, 所以我們就backtracking配合剪枝`if max(state) >= self.res: return`

# Optimization

- 排序, 可以提早觸發 `if max(state) >= self.res: return`
- 最重要的優化是加上`flag`
  - 對於分配的角度來說, 所有手頭上沒有任何cookie的小孩都是一樣的分配選擇
  - 如果現在有三個小孩他們的state[kid]都等於0, 那麼手上這個cookies[i]給kid0, kid1, kid2, ...都是一樣的
  - 所以一但我們將手上cookies[i]分配給某個一無所有的kid後, 就沒有必要再嘗試將手上的cookies[i]分配給另外一個一無所有的kid (因為不管分配給誰, 從分配的角度上來看都是一樣的分配)
    ```py
    flag = 0
    for kid in range(k):
        if state[kid] == 0:
            if flag == 1: continue
            flag = 1
    ```

# Other Method

Binary Search + Backtracking

利用binary search來剪枝

```py
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cookies.sort()

        self.res = inf
        state = [0]*k

        def dfs(i, limit):
            if i == n: return True

            flag = 0
            for kid in range(k):
                if state[kid] + cookies[i] > limit: continue
                if state[kid] == 0:
                    if flag == 1: continue
                    flag = 1

                state[kid] += cookies[i]
                if dfs(i+1, limit): return True
                state[kid] -= cookies[i]
            return False

        l, r = 0, sum(cookies)
        while l < r:
            for i in range(k):
                state[i] = 0 # reset state

            mid = l + (r-l)//2
            if dfs(0, mid):
                r = mid
            else:
                l = mid+1
        return l
```