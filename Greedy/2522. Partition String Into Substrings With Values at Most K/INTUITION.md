# Intuition

這邊首先想到的是我們應該是可以Greedy的去做切分

因為我們要的是`minimum partition`，我們可以用two pointers來找出每一個partition，讓每個partition都盡可能地貼近`k`

而且我們可以觀察到，由於我們右指針越往右，位數越多的話區間的值一定越大，不會有如果切分少，因而讓後面的partition所代表的值反而越小的可能

因此我們就Greedy的去盡可能切分即可

唯一要住一的是如果單一位數(也就是個位數)就小於`k`的話，那就沒有解，返回 `-1`

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$