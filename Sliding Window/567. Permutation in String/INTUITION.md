# Intuition

since we want to find if `s2` includes any permutation of `s1`, we don't need to care about the order of characters in `s1`.

we only need to check if we have all the exact characters in `s1`.

we can use two pointers `l`, `r` and a **hashmap** to check if substring `s2[l:r]` is permutation of `s1`

I use `r` pointer to explore as much as possible:
- once we found a character in `s1`, check if we've already had all the characters in `s1`
- if I found a character in `s1` but the frequency didn't match, move `l` pointer to shrink `s2[l:r]` until we match
- also, if I found a character **NOT** in `s1`, it's impossible for `s2[l:r]` to be a permutation of `s1`. thus, reset **hashmap** and move `l` pointer to `r` pointer.

# Complexity
- Time complexity:
$$O(26 * len(s2))$$

- Space complexity:
$$O(26)$$

# Code
```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        l, r = 0, 0
        has = defaultdict(int)
        while r < len(s2):
            ch = s2[r]
            if ch in counter:
                has[ch] += 1
                if all(has[k] == counter[k] for k in counter.keys()): return True
            else:
                l = r
                has = defaultdict(int)
            r += 1

            while l < r and has[ch] > counter[ch]:
                has[s2[l]] -= 1
                l += 1
        return False
```