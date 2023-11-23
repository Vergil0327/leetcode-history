# Intuition 1

triplet => 試著想如果我們遍歷中間index `i`, 那就:
- 往下找一個nums[j]使得 j < i in both nums1 and nums2
- 往上找一個nums[k]使得 k > i in both nums1 and nums2
如果往下能找到`x`種可能, 往上能找到`y`種可能, 那麼以`i`為中心就有`x*y`種good triplets
但該如何找x跟y?

從敘述可知, 其實我們並不關心值的大小, nums[i]僅相當於是每個元素的id而已
所以我們其實可以把nums1的id重新mapping成由小到大排序的狀態, 然後nums2再依據nums1也再mapping過一次

ex. nums1 = [2,0,1,3], nums2 = [0,1,2,3]

轉換成: nums1 = [0,1,2,3], nums2 = [1,2,0,3]

那這樣的好處是, 對於nums1[i]來說, [1,n-1]這範圍都是possible good triplet center
再來我們現在僅需關注nums2
會發現我們可以直接用值得大小來判斷有多少smallerBeforeSelf跟largerAfterSelf
對於當前nums2[i]來說, 他所能組成的good triplets = smallerBeforeSelf[i] * largerAfterSelf[i]

ex. nums2 =    [1,2,0,3]
 smallerBefore  0 1 0 3
 largerAfter    2 1 1 0
 good           0 1 0 0 => total = 1 good triplet

而count smaller than self其實就是 leetcode 315
求出smallerBeforeSelf之後
smallerAfter[i] = nums2[i] - smallerBeforeSelf[i]
那麼在i後面的位置還有:n-i-1個, 而smallerAfter[i]也有了
所以largerAfter[i] = n-i-1 - smallerAfter[i]
所以good triplets = sum(smallerAfter[i] * largerAfter)

# Intuition 2

如果我們要求的是smallerAfter的話
如果對於nums2[i]來說, 前面i-1個數如果是有序的話, 那就能用binary search找出smallerAfter[i]
因此, 我們可以用SortedList來做

就遍歷nums2[i]時順便看前面`i-1`個元素有多少個比nums2[i]小
```py
smallerBeforeSelf[i] = SortedList.bisect_left(nums2[i])
```