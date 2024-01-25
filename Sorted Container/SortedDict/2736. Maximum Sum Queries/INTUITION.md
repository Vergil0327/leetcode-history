# Intuition

對於這種multi-query的問題, 先看看排序有沒有幫助
每個`[x,y] = queries[i]`要求要 nums1[i] >= x and nums2[i] >= y

兩個排序不好處理, 我們先試著排序集中一個方向試試
我們對`zip(nums1, nums2)`以及queries在x上做排序後,
再來我們只要判斷y即可

排序後每個queires[i]來說, 如果我們x是由大到小排序的話
那麼對`nums=zip(nums1, nums2)`來說, 所有`>= x`的nums[j]都是合法可選的
而我們要的就是從所有>=x的nums[j]中, 在找出符合 >= y 的nums, 並求:
`max(nums[j][0] + nums[j][1]) where nums[j] = zip(nums1, nums2)`

所以我們可以nums跟queries都對x由大到小排序
那麼對於每個[x,y]=quries[i]來說, 我們可以用一個`j`pointer指向nums
將所有 `>= x` 的nums[j]都加入到集合中

由於我們還需要從這些集合中找出 `>= y`的合法nums[j], 所以需要一個資料結構來儲存 >= y 的 maximum value
這邊需要用到SortedDict, 並借用monotonic decreasing stack的概念
SortedDict用來存{num2: maximum value (= nums1[j] + nums2[j])}
所以當前加入的nums2[j]為key, nums1[j] + nums2[j]為value
我們必須先找到這個nums[j]在Sorted Dict裡的位置`k`:
- 如果k' < k and SortedDict[k']的值 >= value, 那就不用更新
- 如果k' < k and SortedDict[k']的值 < value, 那麼所有map裡的SortedDict[k']都要移除掉, 然後再加入SortedDict[k] = value

因為後續在求queires[i]的解時, 因為x已經排序, 所以我們只需要找`>= y`的合法maximum value
如果我們有 SortedDict[k-1] = v1, SortedDict[k] = v2 where v2 > v1
那麼如果有個queries[i]要找`y >= k-1`的maximum value時, 我們要的是v2而不是v1
所以我們要維護一個monotonic decreasing hashmap使得我們找出`>= y`這位置時的值就是我們要的maximum value

這樣我們後面再找queries[i]的解的時候, 就可以
t = SortedDict.bisect_left(y) # 找出 >= y的位置並取出maximum value
res[idx] = SortedDict.peekitem(t)[1]


time: O((n + q)logn + qlogq)
space: O(n)

[good solution](https://leetcode.com/problems/maximum-sum-queries/solutions/3624007/simple-map-solution-in-c/)