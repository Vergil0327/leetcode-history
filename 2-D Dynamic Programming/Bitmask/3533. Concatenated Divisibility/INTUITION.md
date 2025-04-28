# Intuition

brute force => check all permutations

1. see constraint `1 <= nums.length <= 13`: we can use bitmask to show which nums[i] has already been taken
2. we can use DFS to check every possible permutation with use bitmask to represent current chosen state => **top-down dp with bitmask**

3. how to check if current permutation is valid or not?
   - check its **remainder**: remainder' = (remainder * pow(10, nums[i].digit_length) + nums[i]) % k

```py
final = (1<<n)-1
@cache
def dfs(state, remainder):
    if state == final:
        return [] if remainder == 0 else None

    res = None
    for i in range(n):
        if (state>>i)&1: continue

        new_remainder = (remainder * pow(10, digit_len[i]) + nums[i]) % k
        arr = dfs(state | (1<<i), new_remainder)
        if arr is None: continue

        if res is None:
            res = [nums[i], *arr]
        else:
            res = min(res, [nums[i], *arr])
        
    return res
```