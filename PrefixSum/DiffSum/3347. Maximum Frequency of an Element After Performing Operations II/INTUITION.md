# Intuition

這題直覺會想到:

1. 我們先用difference array以O(n)時間找出整個值域範圍[min(nums)-k, max(nums)+k], 每個nums[i]進行操作後的frequency
2. 再來我們只要diff[num]扣掉occurrence[num]後就知道利用了多少操作, `diff[num]-occurrence[num]`, 由於最多只能操作`numOperations`這麼多次, 所以最終每個值的max frequency只能是:
   - `occurrence[num] + min(numOperations, diff[num]-occurrence[num])`
3. 遍歷整個值域找出全局最高frequency即可
```py
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mn = min(nums)
        mx = max(nums)
        diff = defaultdict(int)
        for num in nums:
            diff[num-k] += 1
            diff[num+k+1] -= 1
        
        for i in range(mn-k, mx+k+1):
            diff[i] += diff[i-1]

        count = Counter(nums)
        res = 0
        for i in range(mn, mx+1):
            res = max(res, count[i] + min(numOperations, diff[i]-count[i]))
        return res
```

但透過constraint會發現值域很大:
- nums[i] <= 10^9
- k <= 10^9

所以我們得改一下, 不遍歷整個值域, 僅遍歷`[nums[i]-k, nums[i], nums[i]+k] for num in nums`

有點像是sweepline, 這幾個位置才是關鍵造成diffrence array變化的位置以及有可能產生max frequency的位置

因此最後那段改成:

```py
positions = set()
for num in nums:
    positions.add(num-k)
    positions.add(num)
    positions.add(num+k+1)
    
res = freq = 0
for num in sorted(positions):
    freq += diff[num]

    res = max(res, occurrence[num] + min(numOperations, freq-occurrence[num]))
return res
```

# Complexity

- time:O(n)
- space: O(n)