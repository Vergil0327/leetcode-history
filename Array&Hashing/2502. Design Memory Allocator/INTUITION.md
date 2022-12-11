# Brute Force

## Intuition

just brute force to simulate the process

maintain current available total memory size for early return from lack of available memeroy capacity.

`if self.size + size > self.cap: return -1`

## Complexity
- Time complexity:
O($n^2$) for allocate
O($n$) for free

- Space complexity:
$$O(n)$$

# Sliding Window

## Intuition

we can optimize `allocate` by using sliding window

`if self.size + size > self.cap: return -1`

## Complexity
- Time complexity:
$$O(n)$$ for allocate
$$O(n)$$ for free

- Space complexity:
$$O(n)$$

# More Practical Solution - Two Hashmaps

[Original Post](https://leetcode.com/problems/design-memory-allocator/solutions/2899668/two-maps/?orderBy=most_votes)

1. track the available memory intervals in a sorted map `avail`
2. allocated chunks in a hash map `alloc`.

Since `avail` is sorted, we go left-to-right to find the smallest index of a chunk with the requried size.

```
We could use something like segment tree to find the smallest index faster.
```

When we free the memory, we join all chunks back into avail.