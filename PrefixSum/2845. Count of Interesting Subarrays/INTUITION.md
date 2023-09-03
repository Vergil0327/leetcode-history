# Intuition

subarray一般來說會先想到two pointers或是prefix sum
概念都是我們可以用兩個pointers來定義一個subarray

而這題就是經典的prefix + hashmap題目

因為我們只關注nums[i]%modulo後有沒有等於k, 我們要知道subarray裡取餘後為k的數目
所以首先先將nums[i]轉化成被modulo的餘數等不等於k, 變成一個0/1 array

再來我們在計算prefix sum的時我們希望:
- (prefix_sum[i] - prefix_sum[j])%modulo == k
如果我們有`x`個presum[j], 我們就知道對於右邊界為`i`來說, 我們可以找到`x`個左邊界`j`使得取餘後為`k`

所以我們就用一個hashmap紀錄每個presum有多少個, {presum: count}

記得base case: hashmap[0] = 1, 這樣當prefix[i]%modulo == k時才能正確計算到