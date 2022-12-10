# Intuition

```
max(product) = max(left_half_sum[i] * right_half_sum[i]) where i can be any node as split point
```

since `right_half_sum = total_sum - left_half_sum`, equation above can be transformed into:

```
max(product) = max(left_half_sum[i] * (total_sum - left_half_sum)) where i can be any node as split point
```

thus, we can use **DFS** to find `total_sum` first,
then use postorder DFS to get every possible product and choose maximum

# Approach

1. DFS get total tree sum
2. postorder DFS to get every possible left and right half sum
3. choose max product during traversal
4. return max product after modulo operation

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(recursion)$$
