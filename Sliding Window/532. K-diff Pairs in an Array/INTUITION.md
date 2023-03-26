# Intuition

這題要我們要找distinct pairs且pair的差為k
由於是要找pair, 所以排序並不影響pair

因此我們可以先排個序，這樣我們在找差為k的pair就簡單多了

排序後我們可以用雙指針`l`, `r`代表一對pair
右指針持續往右移動，一但`l`跟`r`的差大於**k**, 那我們就移動`l`縮小差值

一但找到符合條件的pair, 亦即符合`l != r`且`nums[r]-nums[l] == k`的pair後，我們就記錄下來

由於我們要找的是distinct pair, 所以我們把找到的pair加到hashset裡，最後hashset的size就是答案


# Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n(n-1)/2)$$ maximum number pairs