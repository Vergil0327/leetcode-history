# Intuition

- Type 1: Triplet (i, j, k) if nums1[i]＾2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.

- Type 2: Triplet (i, j, k) if nums2[i]＾2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.

看到這兩種type, 首先想到的是(i, j, k)三個index不好處理
看有沒有辦法遍歷一個index然後再決定另外兩個

以type1為例, 這題很明顯地告訴你:

我們可以遍歷nums1[i] 然後再依序遍歷nums2[k] 這樣三個要找的也就呼之欲出了

我們只要用個hashmap紀錄我們遍歷過的nums2[k],
這樣當我們遍歷當前的nums2[k]時, 即可知道在`k`之前有多少個符合的`j`其中`nums2[j] = nums1[i]*nums1[i]//nums2[k]`
我們把個數加上`res`即可

type2也是同理, 我們先遍歷nums2[i]決定`i`, 然後再遍歷nums1[k]
這樣我們就能確定出`nums1[j] = nums2[i]*nums2[i]//nums1[k]`
再來一樣用hashmap找出有多少個符合的nums1[j]即可