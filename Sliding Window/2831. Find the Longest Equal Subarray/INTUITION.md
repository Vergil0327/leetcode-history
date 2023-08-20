# Intuition

first, I come up with sliding window.

if we only want to check one specific nums[i]'s longest equal subarray, we just maintain a valid sliding window for nums[i] where deletion is <= k.

and we can use a hashmap to store count of nums[i] and calculate our `deletion = window size - hashmap[nums[i]]`

since longest equal subarray can be any distinct nums[i], we maintain every nums[i]'s valid window.

we can use a hashmap to store every nums[i]'s sliding window: `hashmap = {nums[i]: array of index of nums[i]}` and for each nums[i] we know:
- `l, r = MAP[nums[i]][0], MAP[nums[i]][-1]`
- subarray size = `r-l+1`
- subarray size after deletion = `len(MAP[nums[i]])`
- deletion = subarray size - subarray size after deletion = `r-l+1 - len(MAP[nums[i]])`

thus, while deletion for nums[i] > k, we just popleft index to maintain valid sliding window for nums[i]
then we update our global maximum result `res = max(res, len(MAP[nums[i]]))`

# Complexity

- time complexity

    $$O(n)$$

- space compelxity

    $$O(n)$$