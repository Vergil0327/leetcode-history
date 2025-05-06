# Intuition

we want the sum of the array products for all valid magical sequences `seq` where `seq` is valid if:

1. seq.length = m
2. 0 <= seq[i] < nums.length
3. 2^seq[0] + 2^seq[1] + ... + 2^seq[m-1] has `k` set bits

see constraint: `1 <= k <= m <= 30`

this reminds me that we can use **bitmask** to represent bits state, and easily write this down:

```py
# just simulate process, brute force solution
def dfs(size, bits):
    if size >= m:
        return 1 if bits.bit_count() == k else 0

    res = 0
    for j in range(len(nums)):
        res = (res + (dfs(size+1, bits + (1<<j)) * nums[j] % 1_000_000_007)) % 1_000_000_007
    return res
```

unfortunately, this will TLE at test case `m=8, k=8, nums=[4475,37658,51018,12424,65157,27914,31161,25310,97672,53516,26018,1860,47220,27702,77234,6951,22039,9184,64449,45837,58613,53764,24216,73423,68676,15003]`

the setbits will becomes something like `1000000000000000000010101` after multiple addition, cause memorization fail

因此再來要換個思路

sequence總共有`M`個位置, 我們一個個考慮nums[i]看要取幾個放進seq裡, 可能性為`comb(M - occupied, count) for count in range(remain_seq_size)`
那麼該`nums[i]`對array product的貢獻度為: 可能的combination再乘上`pow(nums[i], count, 1_000_000_007)`

那麼對於當前我們取的數目`count`, 由於二進制加法的關係, 每兩位就會進位, 所以我們這邊要記錄進位的數目`carry`, 這會影響到下個位數是不是`setbits`
而當前的`(count+carry)%2`即可知道當前的nums[i]是不是`k`個setbits的其中之一

綜合以上所述, 我們能寫出個大概框架為:

`dfs(size, k, i, carry)`: the sum of array product when seq.size is `size` and remain `k` setbits undetermined with `carry` number of carry considering nums[:i]

```py
MOD = 10**9 + 7
def dfs(size, k, i, carry):    
    res = 0
    for cnt in range(remain+1):
        prod = math.comb(remain, cnt) * pow(nums[i], cnt, MOD) % MOD
        cur = carry+cnt
        res += prod * dfs(size+cnt, k-(cur%2), i+1, cur//2)
    return res%MOD
```

base case:

1. `if size == M: return 1 if k==carry.bit_count() else 0`
   - consider valid condition first. order matters
2. `if i >= len(nums): return 0`
   - already consider all the nums[i] and size is still invalid => return 0
3. `if size > M or k<0 or remain+carry.bit_count() < k: return 0` where `remain = M-size`
   - all the other invalid condition