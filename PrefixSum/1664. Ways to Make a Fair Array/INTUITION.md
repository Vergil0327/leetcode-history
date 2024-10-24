# Intuition

刪除i-th 元素後, even位置變odd, odd位置變成even
所以我們準備odd index跟even index的prefix_sum, 然後遍歷一遍當前要刪除的index位置比較

- odd_sum有沒有跟even_sum相等即可, 其中
    - odd_sum = prefix_sum_odd[i-1] + (prefix_sum_even[n]-prefix_sum_even[i])
    - even_sum = prefix_sum_even[i-1] + (prefix_sum_odd[n]-prefix_sum_odd[i])

# Complexity

time: O(n)
space: O(n)