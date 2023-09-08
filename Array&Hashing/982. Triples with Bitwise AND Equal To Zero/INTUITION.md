# Intuition

相當直覺, 由於我們要找triplet `(i,j,k)`
我們先用hashmap紀錄`nums[i]&nums[j]`的數目

之後在遍歷`nums[i]`對`pair for pair in hashmap.keys()`做**AND**操作
如果三者**AND**完之後為0, 那就`res += hashmap[pair]`

time: O(n*n + n * 2^16) where 0 <= nums[i] < 2^16. we can have 2^16 tuples in hashmap at most.