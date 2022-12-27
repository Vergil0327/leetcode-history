# Intuition

首先最核心的思想是:

由於整個排序後的數列僅rotate了一次，我們可以用`nums[0]`作為定位點，我們能發現:

- 當nums[mid] >= nums[0]時，nums[mid]處於左半邊數列
- 反之則在右半邊數列

同理，我們也能藉此判斷:
- 當target >= nums[0]時，target處於左半邊數列
- 反之則在右半邊數列

**Case 1 - `target` 跟 `nums[mid]`處在同個區間**

因此，當 `target` 跟 `nums[mid]`處在同個區間時，那我們可以正常的binary search
- 同在左區間，`target>=nums[0]`和`nums[mid]>=0`判斷皆為True
- 同在右區間，`target>=nums[0]`和`nums[mid]>=0`判斷皆為False

**Case 2 - `target` 跟 `nums[mid]`處在不同區間**

當`target`與`nums[mid]`在不同區間，那們我們就藉由判斷`target`在哪邊區間來縮小Search Space
- 當`target` >= nums[0]，代表`target`在左區間，因此我們縮小右邊界
- 反之則在右區間，我們可以縮小左邊界

**Duplicate Number的影響?**

Special Case:

當數列的頭尾相等時，我們的
`if (nums[mid] >= nums[0]) == (target >= nums[0])`
這行判斷會出錯

ex.
nums = [1,1,1,2,3,4,5,0,0,0,1,1,1]
          M                 T
mid和target其實在不同邊，但判斷會都在左邊

既然這情形會導致判斷出錯，那我們就泯除這項條件即可，也就是:
在確認`nums`至少含有一個數的情況下，將尾部與nums[0]相等的數全部移除

*註: len(nums)>1，是確保當數值全部相同時，我們不會把全部數值都移除*

# Complexity

- time complexity

$O(N)$ worst case, $O(log⁡N)O$ best case, where N is the length of the input array.

- space complexity

$$O(1)$$