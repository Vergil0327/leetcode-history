# Intuition

首先先不考慮有duplicate的情況下，當整個array rotate後我們關注nums[0]這個值
以這個作為定位點來看可以發現:
1. 當任意nums[mid] >= nums[0]時，代表nums[mid]處於rotate後的左半邊
2. 反之，當nums[mid] < nums[0]時，代表nums[mid]處於右半邊

所以我們可以透過binary search:
- 當mid在左半邊區間時，右半邊的值比較小，因此我們就移動左邊界往右
- 反之當mid在右半邊區間時，我們就移動右邊界往左

但如果我們的nums數組中有重複的值的話會發生什麼情況?
例如 nums = [4,4,4,5,6,7,0,1,4,4,4]
              mid             mid

當首尾都是一樣的值時，我們上面的二分搜尋判斷會誤判，這時nums[mid] >= nums[0]時，可能在左半邊也可能在右半邊

既然首尾值相同時會誤判，那我們就提前移除掉這種情況就好
(註:只要首尾不相同，就算左半邊開頭都是重複的值也不影響二分搜索的判斷)

當首尾的值相同時，我們就持續地把後面相同的數給移除掉，移到nums至少為1，避免[4,4,4,4,4]這種情況直接移除成空數組

```
while len(nums)>1 and nums[0] == nums[-1]:
    nums.pop()
```

提前處理完後，整個問題就又變回[Leetcode 153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)了

時間複雜度在Worst Case會是$O(n)$