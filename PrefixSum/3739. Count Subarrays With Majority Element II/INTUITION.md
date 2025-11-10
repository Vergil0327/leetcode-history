# Intuition

We want to count all subarrays in which the element target appears more than half of the time.
We can represent each element of the array as:
- Each occurrence of target contributes +1.
- Each non-target element contributes -1.
- "More than half" means there are more +1s than -1s, so the total sum is positive.

### Using Prefix Sums

Let the prefix sum array be defined as: prefix[i]=a0+a1+⋯+ai-1

Then, for any subarray from index l to r, we have:
sum(l,r)=prefix[r+1]−prefix[l]

The condition sum(l, r) > 0 becomes: prefix[r+1]>prefix[l]
Therefore, we just need to count how many earlier prefix sums are smaller than the current prefix value.

### Using Fenwick Tree

same idea but using fenwick tree rather than prefix sum

```py
# Prefix sums, with pref[0] = 0
presum = list(accumulate(arr, initial=0))

# Coordinate compression
vals = sorted(set(presum))
idx = {v: i for i, v in enumerate(vals, start=1)}  # 1-based

# Fenwick Tree
size = len(vals)
bit = [0] * (size + 2)

def update(i: int, delta: int) -> None:
    while i <= size:
        bit[i] += delta
        i += i & -i

def query(i: int) -> int:
    res = 0
    while i > 0:
        res += bit[i]
        i -= i & -i
    return res

# Count pairs with pref[j] > pref[i]
res = 0
for cnt in presum:
    pos = idx[cnt]
    res += query(pos - 1)
    update(pos, 1)
```