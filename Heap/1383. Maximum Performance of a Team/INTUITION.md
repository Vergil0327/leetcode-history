# Intuition

當有兩個條件時，試著想說能不能先處理好一個條件然後再遍歷另一條件
這邊能看見當我們將efficiency[i]由大到小排序時，由於是取`min()`，因此當前的efficiency[i]就會是最小的efficiency，不用再回頭遍歷找出最小efficiency，這樣我們就處理完一個條件了

再來由於是取最多前`k`個最快的和，我們可以透過維護一個size為`k`的`min heap`，每當size > k時便把速度最慢的彈出，這樣我們就可以一直維護一個前`k`大的和了

持續取`max(currSpeedSum * currMinEfficiency)`即可找出答案

# Complexity

- time complexity
$$O(nlogn + nlogk)$$

- space complexity

$$O(n)$$
