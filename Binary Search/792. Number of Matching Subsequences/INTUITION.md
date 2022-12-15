# Binary Search

## Intuition

*follow-up of 392. Is Subsequence*

if we use approach of 392., time complexity would be O($n^2$). it's not efficient.

once we see the linear search, we should think if we can replace it with **binary search**

first, we use a hashmap called `indexMap` to store every character's index in `s`.

then we iterate through `words` array and use **binary search** to find if every word's character exists in `s`.

once we found a character's index, we also use extra variable `prevIdx` to store this index to make sure next character's index is greater than current index. this is constraint of subsequence.

don't forget to increment `prevIdx` to make sure we don't count index twice. each time we found a valid index, we should exclude it in next round of binary search.

we can use a flag variable `found` or check if `prevIdx` is equal to length of subseq. in the end of for-loop to tell us we found a subseq. !

## Approach

- use binary search to find each word's every character's index in `s`
- if character not in `s` (not in our hashmap), current word is not a subseq.
- if index returned by bisect_left is invalid, current world is also not a subseq.
- after we finish iteration, we can check if current word is subseq. or not by checking whether `prevIdx` is equal to length of subseq. or not. (or checking flag variable `found`)

## Complexity
- Time complexity:

$$O(nlogm)$$, where n is words.length and m is length of s

- Space complexity:

$$O(n)$$ since we use a hashmap to store all the character's index

## Code
```
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexMap = defaultdict(list)
        for i, c in enumerate(s):
            indexMap[c].append(i)
        res = 0
        for word in words:
            found = True
            prevIdx = -1
            for c in word:
                if not indexMap[c]:
                    found = False
                    break
                i = bisect.bisect_left(indexMap[c], prevIdx)

                if i == len(indexMap[c]):
                    found = False
                    break
                prevIdx = indexMap[c][i]+1
            if found:
                res += 1
            
        return res


```