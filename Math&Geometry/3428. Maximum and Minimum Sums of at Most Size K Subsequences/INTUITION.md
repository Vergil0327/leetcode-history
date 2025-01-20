# Intuition

subseq. 與順序無關 => 我們可以先對nums進行排序
那這樣我們如果由左往右遍歷, 對於nums[:i](inclusive)來說, nums[i]會是maximum element

然後我們可以從nums[:i)裡, 也就是前i-1個裡挑出{0,1,2,...,k-1}個元素組成subsequence

> 同理, nums[i]作為maximum element, 的個數會相當於nums[n-i-1]作為minimum element的個數, 相當於從nums[i:]裡挑出{0,1,2,...,k-1}個元素與nums[n-i-1]組成subseq.

所以整理一下:

1. For each index i:
    - nums[i] represents maximum element considering nums[:i]
    - nums[n-i-1] represents minimum elements considering nums[n-i-1:]
2. 對於nums[i]跟nums[n-i-1]來說, 組成的sequence長度至多為k, 所以可能的組合數為遍歷長度range(0, k), 然後考察當前nums[:i](及nums[n-i-1:])內可以挑出多少合法sequence組合

所以# of subseq. = math.comb(i, t) for t in range(0, k) if i >= t

因此綜合上述兩點, 整個框架為:

```py
mod = 10**9 + 7

nums.sort()
n = len(nums)

res = 0
for i in range(n):
    numberOfSubsequences = 0
    for t in range(k):
        if i >= t:
            numberOfSubsequences += math.comb(i, t)
            numberOfSubsequences %= mod
    res += (nums[i] + nums[n-i-1]) * numberOfSubsequences
    res %= mod
return res
```

time: O(nk * k) (ps. O(min(k, n-k)) for comb(n, k))

這邊我們可以事先計算comb[i][t], 來降低時間複雜度

```py
m = n = 71
comb = [[0]*n for _ in range(m)]

for i in range(m):
    comb[i][i] = comb[i][0] = 1
    for j in range(1, i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
```

# Complexity

time: O(nk)
space: O(nk)