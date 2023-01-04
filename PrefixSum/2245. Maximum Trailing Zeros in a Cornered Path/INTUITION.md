# Intuition

首先能很直覺想到的是，要得到trailing zeros，只有含有質因數`2`跟`5`才能組成一個`0`
因此我們要關注的是，每個數含有多少個質因數`2`與`5`
trailing zeros 的個數則為: `min(# of 2, # of 5)`

因此我們可以把整個grid處理成，每個cell含有多少`[# of 2, # of 5]`

再來由於只能轉彎一次，因此對於每個cell來說只能當一次轉折點，我們可以考慮每個cell當轉折點的情況下能產生多少個trailing zeros，產生的trailing zeros則為整個路徑的`min(# of 2, # of 5)`

由於我們有四個方向可選，因此對於每個轉折點來說
1. 可以從上方走到grid[r][c]，然後往左走到底
2. 可以從上方走到grid[r][c]，然後往右走到底
3. 可以從下方走到grid[r][c]，然後往左走到底
4. 可以從下方走到grid[r][c]，然後往右走到底

四種可能取最多能產生多少trailing zeros即為該點的最佳
遍歷整個grid取最大即為答案

由於要找的是一路上的`2`跟`5`的個數和，因此我們可以提前處理prefixSum by row跟prefixSum by col來儲存資訊

再根據**排容原理**, presumRow 跟 presumCol會重複計算grid[r][c]兩次，記得把grid[r][c]扣掉一次即可得到每個cell作為轉折點時能得到的最多trailing zeros是多少

# Complexity

- time complexity

$$O(ROWS * COLS * log(grid[row][col]))$$

- space complexity

$$O(ROWS * COLS)$$