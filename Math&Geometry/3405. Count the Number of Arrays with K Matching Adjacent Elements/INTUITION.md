# Intuition

直覺想到:

```py
@cache
def dfs(i, kk, cur):
    if i >= n:
        return kk == k

    res = 0
    for el in range(1, m+1):
        if el == cur:
            if kk < k:
                res += dfs(i+1, kk+1, cur)
        else:
            res += dfs(i+1, kk, el)
    return res%1_000_000_007
return dfs(0, 0, 0)
```

但由於範圍限制:
- 1 <= n <= 10^5
- 1 <= m <= 10^5
- 0 <= k <= n - 1

肯定會超時

從constraint來看, 這題可能要往O(n)的方向去想

要建構一個size `n`的數, 每個數值範圍[1,m]

首先, 第一個數有`m`種選擇, 後續可選擇看是要:
1. 滿足條件`arr[i - 1] == arr[i]`: 1種選擇
2. 不打算滿足條件: m-1種選擇

整體是n size, 所以剩下的`n-1`個位置要選出恰好`k`個位置滿足`arr[i-1] == arr[i]`: comb(n-1, k)

那其餘的`n-1-k`位置就必須是滿足`arr[i-1]!=arr[i]`這條件, 代表每個位置有`m-1`種選擇

因此, 我們就把所有可能性加總起來即可:

```py
# m種可能首位字母, 剩下n-1位置選出k個位置, 每個位置只有一種可能, 剩下n-1-k個位置, 每個位置有m-1種可能選擇
answer = m * comb(n-1, k) * pow(m-1, n-1-k, mod) % mod
```
