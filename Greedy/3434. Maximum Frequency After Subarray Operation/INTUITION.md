# Intuition

[k k k k {X X X k k k X X X X} k k k k k k k]

我們要找的是一段最大subarray sum
使得兩側k數目跟中間{X X X , ..., X X X} X數目相加最大

由於:
- 1 <= nums[i] <= 50
- 1 <= k <= 50

所以我們遍歷所有可能要轉換的目標`target`, 範圍1~50, 並計算其最大可能subarray count

如果:
1. nums[i] == target: 多一個nums[i]轉成k, subarray count + 1
2. nums[i] == k: 一個k被轉換掉, subarray count - 1
3. 其餘的不會被轉換成k, 不影響subarray count

所以我們可以有個helper function來計算maximum subarray count
由於我們有將nums[i]==k的情況考慮進來, 所以這邊計算的**maximum subarray count**其實是extra gain
計算出我們能**額外**獲得的maximum subarray count to k

```py
def kadane(t):
    max_count = count = 0
    for num in nums:
        if num == t:
            count += 1
        elif num == k:
            count -= 1
        count = max(0, count)
        max_count = max(max_count, count)
    return max_count
```

那這樣我們遍歷所有可能target, 即可得出max subarray count
最終答案就是`max subarray count + nums.count(k)`
```py
res = 0
for target in range(1, 51):
    if target == k: continue
    res = max(res, kadane(target))
return res + nums.count(k)
```