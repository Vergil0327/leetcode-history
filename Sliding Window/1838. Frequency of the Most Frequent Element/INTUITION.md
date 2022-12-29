# Sort + PrefixSum

## Intuition

首先我們的 `target` 一定是一個較大的數，然後在`k`次操作內將其他較小的數補成跟 `target` 一樣

因此我們可以對`nums`先做排序
然後移動雙指針`l`, `r`

每當`r`往前走，在[l,r)這段區間內，如果要形成max frequency的話，那一定是每個數值都補成跟[l,r)這區間內最大的數一樣，因此:
- 當 `maxNum * (r-l) - sum([l,r)) <= k 時`，右指針`r`就能繼續往前
- 反之則移動左指針`l`

所以這題可以透過**Sliding Window**的方式來做，並透過**Sorting**來快速定位區間內的最大值，也就是`nums[r]`

那既然我們每次移動Sliding Window時都會需要知道區間和，因此我們可以事先計算**Prefix Sum**來幫助我們

所以最後核心程式碼為:
```python
l, r = 0, 0
maxFreq = 0
while r < n:
    num = nums[r]
    r += 1

    while num*(r-l) - (presum[r]-presum[l]) > k:
        l += 1
    # 從while跳出來後，此時[r,l)必定可以在k次操作內將每個數補成一樣
    maxFreq = max(maxFreq, r-l)
```

## Complexity

- time complexity
$$O(nlogn)$$

- space complexity

$$O(n)$$

# Binary Search

## Intuition

想法跟上面很像
一樣先Sorting跟求出Prefix Sum

再來我們遍歷`nums`，算出以`nums[i]`作為目標，在k次操作內所能得到區間有多大
概念如下:
```
nums.sort()
ans = 0
for i, num in enumerate(nums):
    target = num
    ans = max(ans, check_by_binary_search(target))
```

而我們的check函式則為：

當`nums`為 XXXXX {mid XXXX index}

我們選一個`mid`來看[mid,index]這段區間能不能在k次操作後成立
也就是:
- 當`presum[index+1]-presum[mid]+k >= (index-mid+1) * nums[index]`, 代表`k`次操作可以符合要求，我們可以再繼續往左移動`mid`
- 反之則右移 `mid`

我們可發現一樣是在控制一個[mid,index]的window

```
def check(index):
    l, r = 0, index
    while l < r:
        mid = l + (r-l)//2
        if presum[index+1] - presum[mid] + k < (index-mid+1) * nums[index]:
            l = mid+1
        else:
            r = mid
    return index-l+1
```