# Intuition

1. find lexicographically largest character by hashmap {ch: [...indices]}
2. find its index from hashmap and we can get `s[i:] for i in hashmap[biggest_ch]`
3. get largest one by brute force

```py
class Solution:
    def lastSubstring(self, s):
        index = defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        biggestCh = list(sorted(index))[-1]

        res = ""
        for i in index[biggestCh]:
            res = max(res, s[i:])
        return res
```

but if `s="aaaaa.......aaaaa"`, it'll be MLE

since answer must be within every possible suffix string `s[i:] where i in index[biggestCh] `

let's choose first 2 smallest indices since the longer the larger and maintain `i` always smaller than `j`

```
[XXXXXXXXX]XXXXXXX
 i       k
______[XXXXXXXXX]XXXXXX
       j       k
```

and we move these two pointers by a distance `k` and keep comparing s[i+k] with s[j+k]

- if s[i+k] == s[j+k]:
  - compare next character by incrementing k
- if s[i+k] > s[j+k]:
  - it means all the s[jj:] where j < jj <= j+k are smaller than s[i:]
  - `j` start from `j+k+1` and move to next biggest character and keep comaparing s[i+k] and s[j+k]
  - reset k to 0
- if s[i+k] > s[j+k], same as bove:
  - it means all the s[ii:] where i < ii <= i+k are smaller than s[j:]
  - `i` start from `i+k+1` and move to next biggest character and keep comaparing s[i+k] and s[j+k]
  - reset k to 0
  - special case:
    - if i == j, move j to next biggest character position since we want to compare two different suffix string

as for biggest character, we can use a hashmap with iteration to find it.