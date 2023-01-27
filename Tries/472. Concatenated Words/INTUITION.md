# Intuition

if **prefix of words[i]** exists in words, then I can continue to check **suffix of words[i]**.

`only if both prefix and suffix of words[i] exists, I can say this is a concatenated word`

i.e. words[i] is concatenated word if words[i][:k] and words[i][k:] exists in words

thus, I construct a **Trie** for checking if part of word exists in words
then, just use DFS to explore every `words[i]` and count how many word exists in `words[i]`

# Complexity
- Time complexity:
$$O(N*L + N*L * L(string \ slicing))$$
, where L = words[i].length and 1 <= L <= 30

- Space complexity:
$$O(26L)$$
