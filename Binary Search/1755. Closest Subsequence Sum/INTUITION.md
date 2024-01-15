# Intuition

順序沒有差異, 先排個序比較好看出大小
試著看看拆開正負號會不會比較好判斷

example 1.
[-7],[3,5,5]

subseq. sum, 每個元素可選或不選
好像不管怎樣都得必須花O(2^n) 其中 n <= 40

突破口在於我們可以分成兩半來取subset sum, 那這樣就是O(2^(n/2)) + O(2^n/2) = O(2^20) + O(2^20)
各是$10^6$級別 => 可接受

那我們目標變成從兩邊找出minimum`abs(subset_sum1 + subset_sum2 - goal)`
=> 如果單純暴力解法的話是O(subset.size^2)
=> 要優化線性解法只能binary search, 所以我們可以其中一邊排個序後, 遍歷一邊然後用binary search搜索另一邊, 達到O(subset.size * log(subset.size)), 約`10^6*log(10^6)`級別