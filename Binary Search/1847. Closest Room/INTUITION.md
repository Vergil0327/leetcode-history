# Intuition

如果queries依據minSize排序, 由小到大遍歷過程中能逐漸淘汰掉所有`rooms[i].size < queries[i].minSize`
如果rooms以size作為排序的話, 就能用two pointers來標示出哪些rooms被淘汰, 哪些還是candidates

再來要找`abs(queries[i].preferred - rooms[i].id)`最小的一個, 如果我們rooms以id作排序, 就能用binary search找出`rooms[i].roomId >= preferred`以及`rooms[i].roomId < preferred`的位置, 然後再看哪個離preferred更近.

由小到大會需要逐漸移除掉所有小於minSize的room, 一但移除某個`rooms[i]`, 排序的index都會改變, 很難維護兩個以不同屬性作為key做排序的rooms

那如果反過來queries[i].minSize由大到小來看的話?

把所有rooms[i].size >= current queries[i].minSize的都加入成candidates
然後將所有candidates依據roomId排序, 這樣就能用根據前面分析的那樣, 用binary search找出靠`preferred`最近的rooms[i].roomId

看起來可以透過O(klogn)找出所有答案

1. 所以首先將queries[i]依據minSize由大到小排序, 同時紀錄原本的index來更新`res[i]`. => O(klogk)
2. 然後由大到小遍歷queries[i]的過程中, 將所有`rooms[i].size >= queries[i].minSize`的room加入到candidates裡，並以roomId做排序. 可以用two pointers來做. => 以size排序rooms:O(nlogn), two-pointers將room加入sorted candidates:O(nlogn)
3. 然後最後再用binary search找出最接近queries[i]的room即可 => k * 2log(n)
