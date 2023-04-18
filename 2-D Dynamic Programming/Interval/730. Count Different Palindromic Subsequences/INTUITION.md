# Intuition

dfs(l, r): s[l:r+1]這段區間所能組成的palindromic subsequence數目

```                   l > r -> 區間不合法
             Y        l = r -> 1
        Y         Y   l < r, 0 X -> dfs(l+1, r-1) + 2 (only Y and YY)
        Y    X    Y   l < r, 1 X -> dfs(l+1, r-1) + 2
        Y   X X   Y   l < r, 2 X -> dfs(l+1, r-1) + 2
        Y  X X X  Y   l < r, 3 X -> dfs(l+1, r-1) + 2
        Y X X X X Y   當s[l] == s[r]時,
                      dfs(l+1, r-1)這些合法palindromic subseq都可以跟s[l], s[r]組成palindromic subsequence
                      額外`+2`是加上Y跟YY這兩種情況

                      並且根據constraints, Y 只可能是"a", "b", "c", "d"
        a         a
        b         b
        c         c
        d         d
```