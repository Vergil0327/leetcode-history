# Intuition

nums[p] * nums[r] == nums[q] * nums[s]

nums[p]/nums[q] == nums[s]/nums[r]

let `x` = nums[s]/nums[r], we can iterate `x` and find how many occurence of `x` in hashmap where we memorize ratio's occurrence

> as for `x`,  use GCD to divide numerator and denominator.

首先想到是利用prefix sum (或suffix sum)

```py
class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        
        # suffix sum
        suf_count = [Counter() for _ in range(n+2)]
        for r in range(n-1):
            for s in range(r+2, n):
                GCD = gcd(nums[r], nums[s])
                ratio = (nums[s]//GCD, nums[r]//GCD)
                suf_count[r][ratio] += 1
        for i in range(n-1, -1, -1):
            for key in suf_count[i+1]:
                suf_count[i][key] += suf_count[i+1][key]

        res = 0
        for p in range(n-1):
            for q in range(p+2, n):
                GCD = gcd(nums[p], nums[q])
                ratio = (nums[p]//GCD, nums[q]//GCD)

                res += suf_count[q+2][ratio]
        return res
```

但上面這樣會MLE, 實際上會發現我們只跟suf_count[q+2]有關
照理說只需要維護一個hashmap去計數即可

因此我們可以改成遍歷(r, s), 然後持續往右遍歷過程中去紀錄(p, q)的ratio occurrence

```py
for r in range(4, n-2):
    q = r-2
    for p in range(q-1):
        GCD = gcd(nums[p], nums[q])
        ratio = (nums[p]//GCD, nums[q]//GCD)
        count[ratio] += 1
    
    for s in range(r+2, n):
        GCD = gcd(nums[s], nums[r])
        ratio = (nums[s]//GCD, nums[r]//GCD)
        res += count[ratio]
```

time: O(n^2)
space: O(n^2) (n^2種組合)