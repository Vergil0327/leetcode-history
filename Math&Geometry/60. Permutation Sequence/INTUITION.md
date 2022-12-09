### Brute Force

我們可以透過dfs找出全排列，但這樣就會是N!的時間複雜度，顯然效率是很低的

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        cnt = 0
        def dfs(state, visited):
            nonlocal cnt
            if len(state) == n:
                cnt += 1
                if cnt == k:
                    res.append(state)
                    return True
                return False

            for i in range(1, n+1):
                if i in visited: continue
                visited.add(i)
                if dfs(state+str(i), visited): return True
                visited.remove(i)
            return False
        dfs("", set())
        return res[0]
```

### Math

由於排列順序是固定的，因此我們可以透過k與(n-1)!的差先找出第一位數

固定第一位數後，剩下的排列組合為(n-1)!
順序則是由小到大，最多1-9([1,2,3,4,5,6,7,8,9])
那麼透過`ceil(k/permutation)-1`可以找出我們使用第幾個順序的digit

ex. n=4, k=4 -> ceil(4/4!)-1 = ceil(4/24)-1 = 1-1 = 0 (使用0-th index的digit)

在確定第一個digit後，將使用過的digit從選項中移除後，並更新`k`

以此反覆操作找出下一位digit，直到找出所有位數後即為答案