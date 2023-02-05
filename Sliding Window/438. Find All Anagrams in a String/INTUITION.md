# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
maintain a window whose size is same as `p`

if every character's frequency in window is same as `p`, it's a anagram and we can append left pointer `l` to answer

and we can use a `valid` variable to help us from iterating through hashmap again and again for checking equality of character's frequency.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(26)$$

# Code
```
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        window = defaultdict(int)

        n = len(s)
        l = r = 0
        valid = 0
        res = []
        while r < n:
            ch = s[r]
            r += 1
            if ch in counter:
                window[ch] += 1
                if window[ch] == counter[ch]:
                    valid += 1
            
            while r-l >= len(p):
                if valid == len(counter): res.append(l)

                ch = s[l]
                l += 1

                if ch in counter:
                    if window[ch] == counter[ch]:
                        valid -= 1
                    window[ch] -= 1
        return res     
```