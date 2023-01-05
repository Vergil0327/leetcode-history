# Intuition

to make every num equal, we must increase minimum value to equal current maximum one

but we still have the save difference between minimum value and next maximum one i.e. original second maximum one.

thus, we need to increment every gap between minimum value and every other larger num

```
1,2,3,4,5,6
+5
6,7,8,9,10,6
+4
...
+ difference between minimal number and other
```

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(1)$$