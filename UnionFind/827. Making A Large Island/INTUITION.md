# Intuition
1. 連通現有island
2. 查看每個`0`位置, 看四個方向連通後的area多少更新`res`
    => area = sum(find(key(row+1, col)), find(key(row-1, col)), find(key(row, col+1)), find(key(row, col-1))) + 1
=> 用union-find來幫助查詢
edge case.
  1. see example 3, res's default value should be max(rank)


# Complexity

- time complexity:

$$O(mn * α(mn))$$
, where we can see α(mn) as O(1)

- space complexity:
$$O(mn)$$