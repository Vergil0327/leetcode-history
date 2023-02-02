# Intuition

**observation**

```
arr[1] = 2 * arr[0]
arr[3] = 2 * arr[2]
arr[5] = 2 * arr[4]
```

what we want is pair up every num with its double

thus, we just sort the array and store each num's count in hashmap

if its double doesn't exist return `False`

if `every num` found its double successfully, return `True`

since negative will sort in reverse order, we handle positive and negative value separately

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(n)$$

# Optimized

what we really care about is if double is enough for pairing.

thus, we can iterate key in counter in sorted order and see if its double is enough.

```py
for num in sorted(counter.keys(), key=abs):
    counter[2*num] -= counter[num]
    if counter[2*num] < 0: return False
return True
```