# LIS + Greedy (Patient Sort)

## Intuition

我們要求的其實就是每個位置的LIS，因此我們需要維護一個LIS序列，然後在該序列中查找每個obstacle的LIS長度，與Leetcode 300. LIS不同的是:

- 這題只要 `>=` `obstacles[i-1]` 就可以加上 `obstacles[i]`

因此對於我們維護的LIS序列，`obstacles[i]`插入的位置為bisect_right()，而longest obstacle course就是到目前位置的LIS長度，也就是`i+1`

ex. LIS = [1,2,3], obastacles[i] = 3
這時`obastacles[i]`可以直接加在目前的LIS之後形成[1,2,3,3], ，longest obstacle course為4

ex. LIS = [1,2,3,3], obastacles[i] = 2
這時`obstacles[i]`插入位置為`index=2`, 形成 LIS=[1,2,2, ...]，longest obstacle course 為3 ([1,2,2])

## Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n)$$