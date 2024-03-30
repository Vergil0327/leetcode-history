# Intuition

首先看到constraint: nums[i] <= 10^9 < 2^32
一開始想到的是binary search + sliding window

search space是[1, n+1]

```py
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l if l != n+1 else -1
```

那check也很簡單, 我們就用fixed length sliding window掃過一遍
```py
def check(length):
    bits = [0] * 32
    l = r = cur = 0
    while r < n:
        for i in range(32):
            if (nums[r]>>i)&1:
                bits[i] += 1
                if bits[i] == 1:
                    cur += pow(2, i)
        r += 1

        while l < r and r-l > length:
            for i in range(32):
                if (nums[l]>>i)&1:
                    if bits[i] == 1:
                        cur -= pow(2, i)
                    bits[i] -= 1
            l += 1

        if r-l == length and cur >= k: return True
    return False
```

但卻TLE, 這時仔細看一下會發現
其實我們用O(32n) sliding window掃過一遍即可

首先預先處理一下可能會用到的`pow(2, i) for i in range(32)`
```py
power = [pow(2, i) for i in range(32)]
```

再來就sliding window, 我們維護當前的OR值`cur`
一但當前`cur >= k`, 我們就能更新`res`並嘗試縮短window size
最終就能用O(32n)的時間掃過一遍並得出最小合法window length

```py    
bits = [0]*32

l = r = cur = 0
res = n+1
while r < n:
    for i in range(32):
        if (nums[r]>>i)&1:
            bits[i] += 1
            if bits[i] == 1:
                cur += power[i]
    r += 1

    while l < r and cur >= k:
        res = min(res, r-l)

        for i in range(32):
            if (nums[l]>>i)&1:
                if bits[i] == 1:
                    cur -= power[i]
                bits[i] -= 1
        l += 1

return -1 if res == n+1 else res
```