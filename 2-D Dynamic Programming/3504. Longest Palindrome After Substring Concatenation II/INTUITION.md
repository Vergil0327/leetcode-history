# Intuition

it's hard, but it's also a great problem. here is my thought process shared with you.

- our target: we want to find the maximum length of palindrome which combined substring of s and t **in order**.
- the constraint:  **1 <= s.length, t.length <= 1000**, the constraint works for O(n^2)

- the brute force is trying all the substring from `s` and `t` to find maximum. O(n^4)


```
s = X X X X {X X X X X X} X X X
             i         j
t = O O O O O O O {O O O O O} O
                   l       r
```

combined = s[i:j] + t[l:r]

see example, we have 3 conditions for combined string:

1. s[i:j] is palindrome, t[l:r] empty
2. s[i:j] empty, t[l:r] is palindrome
3. s[i:j] + t[l:r] is palindrome

for condition 1&2, we can preprocess the maximum length of palindrome starting from `i` for `s` and `l` for `t`

```py
m = len(s)

max_pal_len = [1]*m
for length in range(2, m+1):
    for i in range(m-length+1):
        # check if s[i:i+length] is palindrome
        if s[i:i+length] == s[i:i+length][::-1]:
            max_pal_len[i] = length
```

then, we can easily solve condition 1 and 2 by iterating `i` and `l`

and I see condition 3, I find that we can use the same logic to find the maximum length of palindrome for `s[i:j] + t[l:r]` but change a little bit.

instead find max_pal_len starting from `i` or `l` for both `s` and `t`, we need to find max_pal_len starting from `i` for `s` and ending at `r` for `t`

```py
n = len(t)

max_pal_len_t = [1]*n
for length in range(2, n+1):
    for j in range(length-1, n):
        i = j-length+1
        # check if t[i:i+length] is palindrome
        if t[i:j+1] == t[i:j+1][::-1]:
            max_pal_len_t[j] = length
```

then we can iterate `i` and `r` to define a combined string and use `max_pal_len_s[i]`, `max_pal_len_t[r]` above to find palindrome starting from `i` and ending at `r` by dynamic programming.

```
combined = {X X X X X X X X} {O O O O O O O O O O}
            i                                   r
```

define dp[i][j]: the maximum length of palindrome which combined substring of s[i:] and t[:j]

- if s[i] != t[j]:
  1. condition 1: s[i:] is palindrome, t[:r] empty
  2. condition 2: s[i:] empty, t[:j] is palindrome
  3. find maximum from these two conditions: `dp[i][j] = max(max_pal_len_s[i], max_pal_len_t[j])`

- if s[i] == t[j]
   1. still check condition 1 and 2: `dp[i][j] = max(max_pal_len_s[i], max_pal_len_t[j])`
   2. consider state transition:
       - since s[i] == t[j], we can update `dp[i][j] = dp[i+1][j-1] + 2`
       - we can see that `i+1` and `j-1` may be **out-of-bounds**, we should handle this case:
         1. only `i+1` in bounds which means t[:r] doesn't exist: `dp[i][j] = 2+max_pal_len_s[i+1]`
         2. only `j-1` in bounds which means s[i:] doesn't exist: `dp[i][j] = 2+max_pal_len_t[j-1]`
         3. both out-of-bounds which means only `s[i]` and `t[j]` exist: `dp[i][j] = 2`

summarize all above, we can write the following code, and iterate all possible answer in dp[i][j] to find the answer.

# Opitimization

we can apply `leetcode. 647` to optimize `max_pal_len_s` and `max_pal_len_t` building preprocess:

```py
# leetcode 647
def checkPalindrome(self, s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                if length <= 3 or dp[i+1][j-1]:
                    dp[i][j] = True
    return dp

def longestPalindrome(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    is_palindrome1 = self.checkPalindrome(s)
    is_palindrome2 = self.checkPalindrome(t)

    max_pal_len_s = [1]*m
    for length in range(2, m+1):
        for i in range(m-length+1):
            # check if s[i:i+length] is palindrome
            if is_palindrome1[i][i+length-1]:
                max_pal_len_s[i] = length

    max_pal_len_t = [1]*n
    for length in range(2, n+1):
        for j in range(length-1, n):
            i = j-length+1
            # check if t[i:i+length] is palindrome
            if is_palindrome2[i][j]:
                max_pal_len_t[j] = length
```

# Complexity

time: O(s.length * t.length)
space: O(s.length * t.length)