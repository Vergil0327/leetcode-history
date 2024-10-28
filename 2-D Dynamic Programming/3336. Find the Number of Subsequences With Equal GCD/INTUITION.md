# Intuition

看到subsequence, 想到我們可以用take-or-skip策略配合dfs來做決策
而每次決策我們都可以選擇nums[i]加到`seq1`或`seq2`, 並同時計算並記錄`gcd1`, `gcd2`
最後整個合法數目加總極為答案

base case
- 當整個`n`個nums[i]考慮完後,看最後gcd有沒有相等, `gcd1 == gcd2`
- 並且由於要求**non-empty**, 所以還必須符合`gcd1 > 0 and gcd2 > 0`

```py
@cache
def dfs(i, gcd1, gcd2):
    if i >= n: return int(gcd1 == gcd2 and gcd1 > 0 and gcd2 > 0)

    res = dfs(i+1, gcd1, gcd2) + dfs(i+1, gcd(gcd1, nums[i]), gcd2) + dfs(i+1, gcd1, gcd(gcd2, nums[i]))
    res %= mod
    return res
```

time: O(n * max(nums) * max(nums))