# Intuition

use top-down dp and try 3 types of operation.

start from index 0, let's try every possible partition, and each partition try:

1. reverse
2. swap
3. replace

first, we had better use swap since it can settle down 2 characters by 1 operation.
therefore, we count every `(word1[i],word2[i])` pair where `word1[i] != word2[i]`
then we can know how many swap we can use to deal with `(word1[i], word2[i])` and `(word2[i], word1[i])`
after swapping, the rest of `(word1[i], word2[i])` and `(word2[i], word1[i])` should use replace operation

also, we need to reverse word1 and check it like above again!
and don't forget that reverse operation already cost 1 operation.

based on idea above, we can have:

```py
def dfs(l):
    if l >= n: return 0

    res = inf
    for r in range(l, n):
        s, sr, t = word1[l:r+1], word1[l:r+1][::-1], word2[l:r+1]

        # better use swap. one operation for 2 letters
        # otherwise, use replace
        count1, count2 = Counter(), Counter()
        for i in range(len(s)):
            # skip already the same
            if s[i] != t[i]:
                count1[s[i], t[i]] += 1
            if sr[i] != t[i]:
                count2[sr[i], t[i]] += 1
        
        processed = set()
        swp = replace = 0
        for a, b in count1:
            if (max(a, b), min(a, b)) in processed: continue
            processed.add((max(a, b), min(a, b)))

            x = min(count1[a,b], count1[b,a])
            swp += x
            replace += count1[a,b]-x + count1[b,a]-x
        res = min(res, swp + replace + dfs(r+1))

        # reversed
        processed = set()
        swp = replace = 0
        for a, b in count2:
            if (max(a, b), min(a, b)) in processed: continue
            processed.add((max(a, b), min(a, b)))

            x = min(count2[a,b], count2[b,a])
            swp += x
            replace += count2[a,b]-x + count2[b,a]-x
        res = min(res, 1 + swp + replace + dfs(r+1))
    return res
```