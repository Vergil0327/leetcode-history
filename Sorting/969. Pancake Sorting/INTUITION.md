# Straight-forward Solution

## Intuition

some observations:
1. we can only reverse [:k-1], so we start sorting from `index=n-1` to `index=0`.

2. we can swap head & tail by reverse
   1. thus, we can swap each nums[i] to `index=0` first by do `operation(index of nums[i])`
   2. then we swap head & tail to make nums[i] in right position by doing `operation(i+1)` to move nums[i] from 0 to i

3. once we finish current index, we move pointer `index` to `index-1`

Example.
``` python
nums = [3,2,4,1]
# start moving 4 to i=3 position
4231 # move 4 to i=0 first
1324 # swap head & tail to make 4 right
# start moving 3 to i=2 position
3124
2134
1234
target = [1,2,3,4]
```

## Approach

- use hashmap to store each value's index
- swap to i=0 first
- swap head & tail
- keep processing

## Complexity

time complexity: O($n^2$) since we need to update hashmap in linear time
space complexity: $$O(n)$$

# Space-Optimized

actually, we only sort index one by one, so we don't need to use `hashmap` to store every other's index

we only need to find index of current `i` position's right value
```python
j = arr.index(i+1)
```

## Complexity

time complexity: O($n^2$) since we need to update hashmap in linear time
space complexity: $$O(n)$$