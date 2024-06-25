# Intuition

直覺想到的解法是top-down dp
嘗試所有subarray, 找出最佳解

```py
n = len(nums)

@cache
def dfs(i):
    if i == n: return 0

    res = -inf
    cost = 0
    for j in range(i, n):
        cost += pow(-1, j-i) * nums[j]
        res = max(res, dfs(j+1) + cost)
    return res
return dfs(0)
```

可惜數據規模不允許O(n^2), 會TLE

但cost正負相間, 其實我們也不用每次都遍歷, 我們就狀態多紀錄當前的`sign`一個一個看就好, 並且只有兩個選擇

0. 定義dfs(i, sign): the maximum total cost of the subarray nums[:i] and current cost sign is `sign`
1. 在當前位置分出subarray: dfs(i+1, 1) + nums[i]*sign
2. 繼續將nums[i]接在subarray後面: dfs(i+1, -1 * sign) + nums[i]*sign
3. 兩者取大即可

```py
@cache
def dfs(i, sign):
    if i == n: return 0

    res = dfs(i+1, 1) # split
    res = max(res, dfs(i+1, -1 * sign)) # keep going
    return res + nums[i]*sign
return dfs(0, 1)
```

time: O(2n)
space: O(2n)

# Optimized space

```py
def maximumTotalCost(self, nums: List[int]) -> int:
    pos, neg = -inf, 0
    for num in nums:
        pos, neg = max(pos, neg) + num, pos - num
    return max(pos, neg)
```