# Intuition

首先最初的想法是讓`getIntervals()`能夠以O(1)時間查詢
因此我們直接一維護一個`intervals`數組來儲存`getIntervals()`的答案

所以這題想法是我們維護一個有序數組，透過二分搜尋找出插入位置並插入單點[value, value]
然後再以O(n)時間merge intervals

另外要注意的是我們不需要加入已存在的區間，也就是我們不需要插入重複的數到`intervals`數組裡
因此另外用一個hashset來避免duplicate的情況

# Complexity

- time complexity

addNum: $$O(n)$$
getIntervals: $$O(1)$$

- space complexity

$$O(n)$$

# Further

那既然可以用binary search維護有序數組，並用Hashset避免duplicate
我們也可以直接用 python 的 SortedSet (類似Java的TreeSet)

這樣就會以`O(logn)`時間進行`addNum()`
並以`O(n)`時間構造出`intervals`