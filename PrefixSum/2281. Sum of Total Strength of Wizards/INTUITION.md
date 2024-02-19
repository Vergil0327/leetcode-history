# Intuition


[X X X X X X X]
目標求出所有subarray的strength
strength = min(subarray) * sum(subarray)

看這數據量, n^2個subarray, 要在O(n)時間解出來, 那我們應該朝每個strength[i]的貢獻有多少 的角度來看
試著先想辦法決定其中一個要素, 如果nums[i]是subarray中的min的話, 有多少個subarray是這樣?

這代表從strength[i]開始邊界往左往右延伸, 都必須比他大
因此我們得找出strength[i]的nextSmaller以及prevSmaller

```
nextSmaller[i] = r
prevSmaller[i] = l

X X {X X X X} X X
  l      i    r
```

一但找到之後, 我們就知道以strength[i]為min的subarray有哪些了:
- 左邊界可以是[l+1,i]
- 右邊界可以是[i,r-1]

並且:
left = i-r
right = r-i
總共有left*right個subarray, 它們的min為nums[i]
難點卡在該如何求這些sum(subarray sum)

```
subarray sum = prefix_sum[右邊界] - prefix_sum[左邊界] =
    presum[i]-presum[l+1]
    presum[i+1]-presum[l+1]
    presum[i+2]-presum[l+1]
    ...
    presum[r]-presum[l+1]

    presum[i]-presum[l+2]
    presum[i+1]-presum[l+2]
    presum[i+2]-presum[l+2]
    ...
    presum[r]-presum[l+2]

    ...直到

    presum[i]-presum[i-1]
    presum[i+1]-presum[i-1]
    presum[i+2]-presum[i-1]
    ...
    presum[r]-presum[i-1]
```

左邊界`l`可以從l+1到i-1
仔細看會發現, 相當於有 left 個 (presum[i] + presum[i+1] + ... + presum[r])

然後分別對應減去presum[l+1], presum[l+2], ...
可以看到總共有right個 (presum[l+1], presum[l+2], ..., presum[i-1])

會發現(presum[i] + presum[i+1] + ... + presum[r]) 以及 (presum[l+1], presum[l+2], ..., presum[i-1])
其實也是prefix sum, 只是他們是prefix sum of prefix sum

因此我們預先處理這些數後, 就可以算出所求
整體框架為

```py
presum = list(accumulate(strength))
pre_presum = list(accumulate(presum, initial=0)) # 1-indexed
for i, v in enumerate(strength):
    l, r = prevSmaller[i], nextSmaller[i]
    left, right = i-l, r-i
    rightsum = pre_presum[r]-pre_presum[i]
    leftsum = pre_presum[i]-pre_presum[max(l, 0)] # prevSmaller[i]可能是-1 => 轉成1-indexed
    res += v * (left * rightsum - right * leftsum)
return res%1000_000_007
```