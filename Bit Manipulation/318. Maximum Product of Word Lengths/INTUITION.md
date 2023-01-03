# Brute Force

## Intuition

put words into **set** to remove duplicate first.

then, use $O(n^2)$ to brute force every combination and use **set** to determine if they are intersected

## Complexity

- time complexity

$$O(n^2 * min(len(s), len(t)))$$

- space complexity

$$O(n)$$

# Bit Manipulation

## Intuition

whenever we can use **set** to check intersection, we can always think that if we can use **bitmask** or not.

since only **26** lowercase English characters, we can use 32-bit mask to represent a word and use bit operation to determine if they intersect each other or not.

we can see that the determination step is same as brute force

```py
# use bitmask
if not mask1&mask2:
    maxProduct = max(maxProduct, bits[mask1] * bits[mask2])

# use set
if not a&b:
    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
```

**one thing easy to miss:**

since different words can have same bitmask if they have same characters set.

therefore, when we use hashmap to store bitmask-len(word) relation, we need to store `{bitmask: max(len(word)) }`

```py
bits = defaultdict(int) # { bitmask: len(word)}

# ...

bitmask = 0
for c in word:
    bitmask |= 1<<(ord(c)-ord("a"))
bits[bitmask] = max(bits[bitmask], len(word))
```

## Complexity

- time complexity

$$O(n^2)$$

- space complexity

$$O(n)$$