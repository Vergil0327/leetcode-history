# Trie + Priority Queue
## Intuition

points:
found positive word += 3
found negative word -= 1

雖然透過Trie與Priority可以解，但其實不用那麼麻煩
用`hashset`就好，不需要用到`Trie`

不過使用`Trie`的好處是可以節省多點記憶體空間，減少空間複雜度

## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n*L + nlogn)$$

L: word.length

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(26 * L + n)$$
(trie and array)

$$O(n*L + n)$$
(hashset and array)