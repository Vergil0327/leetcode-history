# Intuition

```
* * | * * * | * * | * * * * * *
  l               ^       <-r
  l         ^ <-r
  l               r
```

- 找出位於`queries = [left,right]`內的左右candle位置
  - 可以用`bisect_left`找出left_candle
  - 用`bisect_right-1`找出right_candle
- 然後再透過prefix sum求出兩candle內的plate個數

# Complexity

- time complexity
$$O(queries.length * logn)$$

- space complexity
$$O(n)$$