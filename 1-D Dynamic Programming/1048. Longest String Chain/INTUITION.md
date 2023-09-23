### Intuition

first I saw this, it's just like LIS problem with additional condition to group increasing subsequence together

so, the naive way it's O(n^3). two for-loop just like LIS with extra `check` function

but can we do better ?

- since we must iterate through `words` once, O(n) is a must
- `check` function looks like required too
- thus, the last thing we can try to do better is the nested loop which is used to find predecessor.

and looks our recursive eq.
```
dp[i] = max(dp[i], dp[j]+1)
```
we can observe that our `dp[i]` only depends on `dp[j]` but `i` is not related to `j`. `j` can be any previous index.

this makes me think maybe we can use `hashmap` to find predecessor in `O(1)` time complexity.

therefore, our algorithm becomes:

```
dp[word] = max(dp[word], dp[predecessor]+1), where dp is a hashmap
```

now, we can use `dp` with `check function` to find if there is a valid predecessor in our `dp`

since **len(word) = len(predecessor)+1**, we can sort words first, then find predecessor by remove one character from words[i].

therefore:

```py
for word in sorted(words, key=len):
    for i in range(len(word)):
        if (pre := word[:i] + word[i+1:]) in dp:
            dp[word] = max(dp[word], dp[pre]+1)
```
