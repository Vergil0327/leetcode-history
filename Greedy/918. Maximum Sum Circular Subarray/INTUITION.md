# Intuition

follow-up of [53. Maximum Subarray](../53.%20Maximum%20Subarray/)

對於一個陣列(或稱數組)，要求最大subarray和可以利用Kadane's algorithm
Kadane Algo的想法是如果當前的subarray和小於0的話，那他等於沒有貢獻，扣除掉他後繼續往後找最大subarray和，也就是持續維持一個 current max sum 並在其中取最大的

那對於一個環形數組來說，我們可以反過來想，最大的subarray和也可能是落在頭尾相連的subarray裡

對於頭尾相連的subarray而言，`例如. array = XX____XXXXX`，相當於是在裡面找一個最小的subarray sum扣掉

因此我們在這兩種情況取最大即可: `max(max_subarray_sum, total-min_subarray_sum)`

唯一要注意的edge case是`當整個數組全都為負數`的時候

ex. nums = [-1,-2,-3,-4]

當全部數值都為負時，由於

`max(max_subarray_sum, total-min_subarray_sum)` = max(negative value, total-total) = 0

因此我們會錯誤地返回0，但實際上應該返回整個數組裡最大的元素

因此我們特別處理edge case，當最大subarray和小於0時，代表全部數值皆為負數，我們直接返回max_subarray_sum即可

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(1)$$