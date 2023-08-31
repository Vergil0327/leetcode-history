# Intuition

為了分成left mid right, 首先想到的是找出兩個split position

XXXXXX | X | X

brute force的話為O(n^3):
```py
res = 0
for split1 in range(1, n-1):
    left = nums[:split1]
    for split2 in range(split1+1, n):
        mid = nums[split1:split2]
        right = nums[split2:]
        if sum(left) <= sum(mid) <= sum(right):
            res += 1
return res
```

如果用prefix sum的話可以把時間降到O(n^2), 但看了下數據範圍, 仍會TLE

再繼續分析一下, 看能不能遍歷left_split的同時以比較高效的方式決定right_split
如果我們確定left_split在`i`位置:

且必須滿足presum[n]-presum[j] >= presum[j]-presum[i] >= presum[i] where prefix sum is 1-indexed
可以用binary search 找出`j`使得presum[j]-presum[i] >= presum[i] and search space is [i+1:n]

search space為[i+1,n]因為mid不可為empty
```py
l1, r1 = i+1, n
while l1 < r1:
    mid = l1 + (r1-l1)//2
    if presum[mid]-presum[i] >= left:
        r1 = mid
    else:
        l1 = mid+1
```

**此時`l1`為left-most valid index for right_split**

同理, 我們應當能透過binary search找出right_split的right-most valid index
由於`right`不可為empty, 所以search space為[i, n-1]

```py
l2, r2 = i, n-1
while l2 < r2:
    mid = r2 - (r2-l2)//2
    if presum[n]-presum[mid] >= presum[mid]-presum[i]:
        l2 = mid
    else:
        r2 = mid-1
```

**此時`l2`為right-most valid index for right-split**

因此對於`left_split = i`來說, 合法right_split為`l2-l1+1`
由於有可能發生無解的情況, 也就是`l2<l1`, 所以我們取個`res += max(0, l2-l+1)`

time: $O(n * 2logn)$

# Other Solution - Two Pointers

time: $O(n)$

```py
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        mod, l, r = 1000000007, 0, 0
        
        presum, res = list(accumulate(nums)), 0
        for i in range(n-2):
            # find left-most right_split
            if l <= i:
                l = i+1 # must non-empty for mid
            
            while l < n-1 and presum[l]-presum[i] < presum[i]: # mid >= left
                l += 1

            # find right-most right_split
            if r < l:
                r = l
            while r < n-1 and presum[n-1]-presum[r] >= presum[r]-presum[i]: # right >= mid
                r += 1
            res = (res + r-l)%mod
        return res
```