# Intuition

score = max(sum(nums1), sum(nums2))
we can swap nums1[left:right] with nums2[left:right] where both left and right are inclusive index

看到subarray sum => 先往prefix sum想試試

1-indexed prefix sum:

我們可以交換這兩段
presum1[right+1]-presum1[left]
presum2[right+1]-presum2[left]

交換的話, 原本score變成:
```
score = max(
    presum1[n] - (presum1[right+1]-presum1[left]) + (presum2[right+1]-presum2[left])
    presum2[n] - (presum2[right+1]-presum2[left]) + (presum1[right+1]-presum1[left])
)
    # 試著把index整理在一起看看有沒有幫助
      = max(
    presum1[n] - (presum1[right+1]-presum2[right+1]) + (presum1[left]-presum2[left])
    presum2[n] + (presum1[right+1]-presum2[right+1]) - (presum1[left]-presum2[left])
)
```

令diff[i] = presum1[i] - presum2[i]

     = max(
    v1 = presum1[n] - (diff[right+1]-diff[left])
    v2 = presum2[n] + (diff[right+1]-diff[left])
)

diff[right+1] - diff[left] < 0 => v1變大

diff[right+1] - diff[left] > 0 => v2變大

找出min(diff[i]) - max(diff[j]) where i > j 然後看v1有沒有大於不進行操作的max(presum1[n], presum2[n])

找出max(diff[i]) - min(diff[j]) where i > j 然後看v2有沒有大於不進行操作的max(presum1[n], presum2[n])

那這樣我們只要分別求出
- rightMax[i]: the maximum diff[i] considering diff[i:n-1]
- rightMin[i]: the mininum diff[i] considering diff[i:n-1]
- leftMax[i]: the maximum diff[i] considering diff[0:i]
- leftMin[i]: the minimum diff[i] considering diff[0:i]

首先看v1有沒有可能更大:
```py
for i in range(n):
    # v1 = presum1[n] - (diff[right+1]-diff[left])
    score = max(score, presum1[n] - (rightMin[i+1]-leftMax[i]))
```

然後看v2有沒有可能更大
```py
for i in range(n):
    # v2 = presum2[n] + (diff[right+1]-diff[left])
    score = max(score, presum2[n] + (rightMax[i+1]-leftMin[i]))
```

時間複雜度: $O(n)$

空間複雜度: $O(n)$

# Optimized

- score1 = presum1 - min(diff[right]-diff[left])
- score2 = presum2 + max(diff[right]-diff[left])

我們目標是要找出:
可利用kadane algorithm找出maximum subarray sum
=> presum2 + max(diff[right]-diff[left]) = presum2 + kadane(nums1-nums2)

而score1的min(diff[right]-diff[left])其實只是差個負號的kadane

```py
def kadane(A, B):
    res = cur = 0
    for i in range(len(A)):
        cur = max(0, cur + A[i] - B[i])
        res = max(res, cur)
    return res

return max(presum2[-1] + kadane(nums1, nums2), presum1[-1] + kadane(nums2, nums1))
```