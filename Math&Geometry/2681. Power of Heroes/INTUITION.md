# Intuition

由於我們要找min跟max, 很直覺的想到可以先排個序
這樣我們可以很快的確定一段subarray的max或min:
- 如果我們定nums[i]為max, 那就往前遍歷找nums[j]作為min的subarray
- 如果我們定nums[i]為min, 那就往後遍歷找nums[j]作為max的subarray

如此一來可以很直覺地寫出$O(n^2)$的brute force solution:

對於最小值為nums[j], 最大值為nums[i]的subarray
我們就看這兩個數之間有多少個數, 每個數可選可不選
所以以nums[j]為**min**, nums[i]為**max**的subarray共有`2^(i-j-1)`種
因此我們往前遍歷nums[j]作為min時, 每個subarray貢獻:
`nums[i]**2 * nums[j] * (2**(i-j-1)) % mod`

```py
mod = 10**9+7
n = len(nums)
nums.sort()
    
res = 0
for i in range(n):
    total = nums[i]**2 * nums[i] % mod
    for j in range(i):
        total += nums[i]**2 * nums[j] * (2**(i-j-1)) % mod

    res = (res + total)%mod

return res
```

所以我們的目標就是優化複雜度, 我們可以仔細看一下內層循環:

```py
res += nums[i]**2 * nums[i] % mod # 單獨一個的狀況, [nums[i]]

total = 0
for j in range(i):
    total += nums[i]**2 * nums[j] * (2**(i-j-1)) % mod

res = (res + total)%mod
```

我們每次都需要往前遍歷加總全部, 可以很明顯看出這其實很像prefix sum
我們當第`i`輪結束後, 下一輪就多加入一個nums[i]作為nums[j]
相當於每個固定nums[j]=min, nums[i]=max的subarray中間都多了一個數
也就是都多了2種可能的subarray, 每個subarray都從 `2**(i-j-1)` -> `2**(i-j-1+1)`

所以當前的內層循環的結果可以寫成先前的結果乘上2, 然後再加上上輪的nums[i]
`presum = presum * 2 + nums[i]`

所以我們可以遍歷`i`的同時, 紀錄/更新`presum`

```py
res = presum = 0
for i in range(1, n+1):
    res += nums[i]**2 * nums[i] % mod # 單獨一個的狀況, [nums[i]]

    # for j in range(i):
    #     res += nums[i]**2 * nums[j] * (2**(i-j-1)) % mod
    
    res += nums[i]**2 * presum % mod
    presum = presum * 2 + nums[i]
```

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(n)$$