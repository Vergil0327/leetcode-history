# Intuition

很直覺能想到用top-down DP的方式去搜索每種可能subarray
定義dfs(i, j, AND): the minimum values of all subarray

就用take or skip策略:
每當我們accumulate AND value等於andValues[j]時, 我們可以選擇take or skip
如果要以nums[i]作為last element的話, 那values就`+= nums[i]`這樣去計算

base case也很直覺:
1. j == len(andValues) and i == len(nums): return 0
2. j == len(andValues) but i < len(nums): invalid => return inf
3. i < len(nums): invalid => return inf

```py
def dfs(i, j, AND):
    if j == m:
        if i == n: return 0
        return inf
    if i == n: return inf
    cur = nums[i] & AND if AND != -1 else nums[i]

    res = dfs(i+1, j, cur) # skip
    if cur == andValues[j]:
        res = min(res, dfs(i+1, j+1, -1) + nums[i]) # take
    return res
```


time: O(n * m * 17)

仔細看andValues[i] <= 10000 約 2^17
而AND操作只會將每個bit從1翻成0, 單向操作, 不會有0翻轉成1
那代表最多只會將17個bit的1翻成0, 就17個操作