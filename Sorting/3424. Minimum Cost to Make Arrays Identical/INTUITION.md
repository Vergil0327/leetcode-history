# Intuition

1. +/- x: cost x
2. Split arr into any number of contiguous subarrays and rearrange these subarrays in any order: 這句話真正意思是我們花`k` cost, 將arr切分成任意subarrays然後重新排列. 這代表我們僅需一次`k` cost然後將arr[i]放置到離它最接近的brr[j]位置.
所以我們可以把arr跟brr進行排序, 而這次rearrange僅需`k` cost, 然後再次計算所需的operation 2

time: O(nlogn)
space: O(1)