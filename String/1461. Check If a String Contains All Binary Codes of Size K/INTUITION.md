# Hashset

## Intuition

since binary code with `k` size has $2^k$ totally.

we can slide window with fixed size `k` and put every window substring into hashset

if len(hashset) == 2^k, then we know we have all the binary codes.

## Complexity

- time

$$O(nk)$$

- space

$$O(nk)$$

# Rolling Hash

## Intuition

we can remove left-most and add one to right-most to maintain a k size bitmask.

time complexity for removal or add is O(1).

**How to remove left-most bit?**

we can use k-size `111...1` with AND (`&`) operation

we can get k-size all one bitmask by:

ex. k=2
1<<(k+1) = 1000
1<<(k+1)-1 = 111

**How to add bit to right most?**

just use OR (`|`) operation


ex. bitmask=1101 and we want to add 1 to right-most position

bitmask = (bitmask << 1) | 1 = 11011
bitmask = bitmask & 1111 = 1011

- time

$$O(n)$$

- space

$$O(2^k)$$