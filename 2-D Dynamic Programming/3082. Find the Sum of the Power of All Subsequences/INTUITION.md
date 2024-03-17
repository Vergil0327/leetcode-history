# Intuition

這題的突破口是, 我們肯定知道該如何找出所有subseq, 那麼該如何在找的過程中同時計算他們的power並加總起來?
這就有DP的味道了
我們就關注我們找到的那個subseq
一但找到一個sum=k的subseq, 那他可以貢獻多少power?
整個nums裡面扣掉該subseq後, 剩下的元素每個都可選可不選, 所以該subseq共可以貢獻2^(n-subseq.size)

因此我們可以先用dfs找subseq的框架: take or skip來找出所有sbusequence, 並記錄他們的sum跟size
一但找到sum==k的subseq, 再依據size就能計算出他貢獻的power

因此框架如下:

```py
def dfs(i, total, size):
    x = dfs(i+1, total, size) # skip
    y = dfs(i+1, total+nums[i], size+1) # take nums[i]
    return (x+y) % mod
```

那base case呢?
- 我們要找的是total==k的subseq, 所以:
    - if total == k: return pow(2, n-size, mod)
- if i >= n or total > k, 那麼絕不可能找到我們要的subseq, 直接返回0