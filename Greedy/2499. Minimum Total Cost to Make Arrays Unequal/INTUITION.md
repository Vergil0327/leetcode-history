### Greedy

有幾個key points需要知道:

1. 最佳策略是找出所有nums1[i] == nums2[i]的位置，然後相互swap

2. 任何需要交換位置的的`i`與`j`
他們相互的swap都可以想成`i`先跟`0`index交換，然後再跟任何適合的`j`交換 (`i->0->j`)。

    因此任何的交換所需要的最小cost都是index本身

3. 如果相互交換完後仍有nums1[i]需要交換，那就從最小index找適合的數來交換，並記錄到`toSwap`裡

4. 最後要注意的是，假設有個數他重複出現了`maxFreq`次，如果這個數超出我們能拿來交換的數的一半(`maxFreq>toSwap.length//2`)，那代表我們沒有足夠適合的數能拿來交換達到inequality