# Intuition

由於我們要確保continuous subarray裡的每個pair都符合差值小於等於2
所以我們用個有序容器`sl`來儲存nums[i]

儲存後我們僅需找出最小值與最大值來判斷是否符合`|nums[i]-max(sl)| <= 2 and |nums[i]-min(sl)| <= 2`
那這樣我們用個雙指針(sliding window)即可得知當前的consecutive array是否合法
如果不合法就持續移除左端點直到合法, 一但停止, 代表右端點為nums[i]的consecutive array有len(sl)個合法左端點
`res += len(sl)`

遍歷完後即可得到所有合法consecutive subarray數目

time: O(nlogn)
space: O(n)