# Intuition

deal with leftmost and rightmost first, then we won't bother we swap cross palindrome pair.

if we want minimum number of moves, we want move character to its position once for all,
or we'll need to swap more steps to adjust, see this:

```
X X X P A X X P A X X -> X X X P A X P X A X X -> X X X P A X P A X X X -> X X X P A X A P X X X
```

if we swap across some already-in-position character, it'll take more swaps.

so, there is a conclusion:
if we start to deal with 0 and n-1 position, we want swap s[0] with others to equal s[n-1] or vice versa.
thus, we have this two possible options:
1. replace s[0] with s[i] to make s[0] == s[-1]
2. replace s[-1] with s[i] to make s[0] == s[-1]

there is brute force version:
```py
def minMovesToMakePalindrome(self, s: str) -> int:
    n = len(s)

    @cache
    def dfs(s):
        if len(s) <= 2: return 0

        # swap s[0] to become s[-1]
        n = len(s)
        res = inf
        for j in range(n):
            if s[j] == s[-1]:
                nxt = s[:j] + s[j+1:n-1]
                res = min(res, dfs(nxt) + j)
                break

        for j in range(n-1, -1, -1):
            if s[j] == s[0]:
                nxt = s[1:j] + s[j+1:]
                res = min(res, dfs(nxt) + n-1-j)
                break

        return res

    return dfs(s)
```

but actually, we can use two pointers to search in more efficient way:
```py
# L X L X R X X X X R
# l ->           <- r
#     l         r

L, R = 0, len(s)-1
l, r = 0, len(s)-1
swap = 0
while s[l] != s[R] and s[r] != s[L]:
    swap += 1
    l, r = l+1, r-1
```

choose minimum swap in `l` or `r` pointer

```py
if s[l] == s[R] and s[r] == s[L]: # choose either s[l] or s[r]
    # swap s[l] to s[0]
    s1 = s[:l] + s[l+1:n-1]
    res = min(res, dfs(s1)+swap)

    # swap s[r] to s[-1]
    # s2 = s[1:r] + s[r+1:]
    # res = min(res, dfs(s2)+swap)
    
    # don't need to, just choose one of them
    # res = min(res, dfs(s1)+swap, dfs(s2)+swap)
elif s[l] == s[R]:
    s1 = s[:l] + s[l+1:n-1]
    res = min(res, dfs(s1) + swap)
else:
    s2 = s[1:r] + s[r+1:]
    res = min(res, dfs(s2) + swap)
```

time: $O(n^2)$

# don't need recursion

we'll find that we don't need recursion anymore. only one clear path to find minimum swap.

for any s[i], its minimum swap is its match prefix index

`X X X X X A X X X X X A X` -> `X A X X X X X X X X X A X`
`X X X X X A X X X X X A B` -> `B A X X X X X X X X X A B` or `A B X X X X X X X X X B A` depends on another `B`'s position.

thus, for s[-1], its minimum step is to find s[i] from left

time: still $O(n^2)$, but without overhead of recursion