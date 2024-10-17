# Intuition

觀察一下會發現
我們目標是從左往右遍歷num[i], 然後跟nums[i+1:]中, **大於num[i]**的**最大且最靠後**的數替換極為答案

所以我們一開始先將`num[i]`跟index `i`放數到max heap裡
然後遍歷過程中, 從max heap裡淘汰掉位置小於等於`i`的元素
如果這時max heap裡存在一個大於num[i]的元素, 那該元素就是我們要swap的目標

# Complexity

time: O(nlogn)
space: O(n)