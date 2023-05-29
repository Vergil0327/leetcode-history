# Intuition

這題很明顯就是在跟你說用BFS往四周走
把所有價格落在pricing區間的item都給撿起來
走過的格子我們可以標記成牆（`0`)來避免重複訪問

那麼每個item我們都依照條件優先排序:
1. 距離由小到大
2. 價格由小到大
3. row由小到大
4. column由小到大

排序後最後取出至多k個item即可

# Complexity

- time complexity
$$O(m*n + klogk)$$
- space complexity
$$O(m*n)$$