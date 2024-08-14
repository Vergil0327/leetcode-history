# Intuition

直接模擬情境
首先我們把前k個都給挑出來, 這時有兩種情況

1. k == 0:
    - 再分成nums為空: 如果nums為空, 那就是前個操作不能取, 這時答案就是前個操作的當下最大的元素
    - nums不為空: 那就是前個操作**選擇放**跟**選擇取**兩種結果的topmost element取大
2. k != 0:
    - 那就勢必得透過取與放兩種操作來消耗掉剩餘`k`, 必定能有種排列是讓最大元素置頂, 所以就是removed elements中取最大的

3. edge case: 當nums.size < 2時, 這時如果`k`為奇數, 那麼nums最後必定為空, 返回-1

# Optimization

考慮k=0, k=1, n=1等edge cases後, 剩下就看前k-1個元素以及k-th element取大即可

```py
if k == 0: return nums[0] if nums else -1
if k == 1: return -1 if n == 1 else nums[1]
if n == 1: return -1 if k%2 else nums[0]

mx = max(nums[:min(k-1, n)]) # we can take k-1 elements and put largest one back to top
if k < n:
    return max(mx, nums[k]) # 最後一次操作選擇: max(放最大元素置頂, 取走k-th element後的topmost element)
return mx # 放置最大元素回去
```